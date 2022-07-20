import frappe
from frappe import _
from frappe.utils import getdate, flt
from rfdesign.nexar.nexarClient import NexarClient

QUERY_MPN = '''
query Search($mpn: String) {
  supSearchMpn(q: $mpn, inStockOnly: true, currency: "AUD") {
    results {
      part {
        mpn
        manufacturer {
          name
        }
        specs {
          attribute {
            name
          }
          displayValue
        }
        sellers(authorizedOnly: true) {
          company {
            name
          }
          offers {
            sku
            inventoryLevel
            factoryLeadDays
            moq
            prices {
              quantity
              convertedPrice
            }
          }
        }
      }
    }
  }
}
'''

@frappe.whitelist()
def update_item_solutions():
  octopart_settings = frappe.get_doc('Octopart Settings')
  clientId = octopart_settings.nexar_client_id
  clientSecret = octopart_settings.get_password('nexar_client_secret')
  nexar = NexarClient(clientId, clientSecret)

  ep_items = frappe.db.get_all("Item", filters = {"item_group": "Electronic Parts", "Disabled": 0})
  # frappe.logger("frappe.web").debug({"Items": ep_items})
  approved_suppliers = frappe.db.get_all("Supplier", filters = {"Disabled": 0}, pluck="name")
  # frappe.logger("frappe.web").debug({"Approved Suppliers": approved_suppliers})

  for ep_item in ep_items:
    update_item = frappe.get_doc("Item", ep_item, as_dict=1)
    default_supplier = {}
    # Clear supplier item table
    frappe.db.delete("Item Supplier", {
        "parent" : update_item.name,
        "parentfield" : "supplier_items"
    })
    update_item.save()
    frappe.db.commit()
    update_item.reload()
    for i in range(1,5):
      mpn="manufacturer_part_number" + str(i)
      if update_item.get(mpn):
          variables = {
              'mpn': update_item.get(mpn)
          }
          results = nexar.get_query(QUERY_MPN, variables)
          # frappe.logger("frappe.web").debug({"Results": results})

          if results:
            for it in results.get("supSearchMpn",{}).get("results",{}):
              mfg = update_item.get("manufacturer_name" + str(i))
              if mfg and it.get("part",{}).get("manufacturer",{}).get("name",{}) == mfg:
                # Specs Iteration to setup Manufacturer Lifecycle Status & RoHS
                manufacturer_lifecycle_status = rohs = ""
                for spec in it.get("part",{}).get("specs",{}):
                  if spec.get("attribute",{}).get("name",{}) == "Manufacturer Lifecycle Status":
                      # frappe.logger("frappe.web").debug({"Manufacturer Lifecycle Status": spec.get("displayValue",{})})
                      manufacturer_lifecycle_status = spec.get("displayValue",{})
                      update_item.db_set("manufacturer_lifecycle" + str(i), manufacturer_lifecycle_status)
                  elif spec.get("attribute",{}).get("name",{}) == "RoHS":
                      # frappe.logger("frappe.web").debug({"RoHS": spec.get("displayValue",{})})
                      rohs = spec.get("displayValue",{})
                      update_item.db_set("rohs" + str(i), rohs)
                
                if manufacturer_lifecycle_status == "":
                  update_item.db_set("manufacturer_lifecycle" + str(i), "Not Found")
                if rohs == "":
                  update_item.db_set("rohs" + str(i), "Not Found")

                supplier_items_mpn = "supplier_options" + str(i)
                last_sync_date = "last_sync_date" + str(i)
                update_item.db_set(last_sync_date, getdate())
                # Clear supplier item table
                frappe.db.delete("Item Supplier", {
                    "parent" : update_item.name,
                    "parentfield" : supplier_items_mpn
                })
                update_item.save()
                frappe.db.commit()
                update_item.reload()

                for seller in it.get("part",{}).get("sellers",{}):
                  # frappe.logger("frappe.web").debug({"Seller": seller})
                  if(seller.get("company",{}).get("name",{}) in approved_suppliers):
                    for offer in seller.get("offers",{}):
                        if (flt(offer.get("inventoryLevel",{})) > 0):
                          if (default_supplier and (flt(default_supplier.get("price")) > flt( offer.get("prices",{})[-1].get("convertedPrice",{}) )) ):
                            default_supplier = {
                              "supplier": seller.get("company",{}).get("name",{}),
                              "supplier_part_no": offer.get("sku",{}),
                              "supplier_stock": offer.get("inventoryLevel",{}),
                              "lead_time": offer.get("factoryLeadDays",{}),
                              "moq": offer.get("moq",{}),
                              "price": offer.get("prices",{})[-1].get("convertedPrice",{})
                            }
                          elif (not default_supplier):
                            default_supplier = {
                              "supplier": seller.get("company",{}).get("name",{}),
                              "supplier_part_no": offer.get("sku",{}),
                              "supplier_stock": offer.get("inventoryLevel",{}),
                              "lead_time": offer.get("factoryLeadDays",{}),
                              "moq": offer.get("moq",{}),
                              "price": offer.get("prices",{})[-1].get("convertedPrice",{})
                            }
                          # frappe.logger("frappe.web").debug({"Deafult Supplier": default_supplier})

                        # frappe.logger("frappe.web").debug({"Supplier Options": supplier_items_mpn})
                        price = 0
                        for j in range(len(offer.get("prices",{}))-1, -1, -1):
                          if flt(offer.get("prices",{})[j].get("quantity",{})) <= 1000:
                            price = offer.get("prices",{})[j].get("convertedPrice",{})
                            break

                        update_item.append(supplier_items_mpn, {
                            "supplier": seller.get("company",{}).get("name",{}),
                            "supplier_part_no": offer.get("sku",{}),
                            "supplier_stock": offer.get("inventoryLevel",{}),
                            "lead_time": offer.get("factoryLeadDays",{}),
                            "moq": offer.get("moq",{}),
                            "price": price
                        })
                    update_item.save()
                frappe.db.commit()
                update_item.reload()
    if default_supplier:
      # frappe.logger("frappe.web").debug({"Deafult Supplier": default_supplier})
      update_item.item_defaults[0].default_supplier = default_supplier.get("supplier",{})
      update_item.db_set("lead_time_days", default_supplier.get("lead_time",{}))
      update_item.append("supplier_items", default_supplier)
      update_item.save()
      frappe.db.commit()
      update_item.reload()

      
  frappe.msgprint("Octopart Update Finished", alert=True)