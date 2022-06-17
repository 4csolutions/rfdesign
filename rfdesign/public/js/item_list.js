frappe.listview_settings.Item = {
	onload: function (listview) {
		listview.page.add_menu_item(__('Sync Octopart Supplier Info'), function () {
            frappe.call({
                method: "rfdesign.api.update_item_solutions",
                async: true,
                callback: function (data) {
                    console.log(data);
                    // if (data.message == "Success") {
                    //     frappe.show_alert({
                    //         message: __("Solutions Info Updated from Octopart"),
                    //         indicator: 'green'
                    //     }, 5);
                    // }
                    // else {
                    //     frappe.show_alert({
                    //         message: __("Error Updating Solutions Info from Octopart"),
                    //         indicator: 'red'
                    //     }, 5);
                    // }
                }
            });
		});
	}
};