from . import __version__ as app_version

app_name = "rfdesign"
app_title = "RFDesign"
app_publisher = "4C Solutions"
app_description = "ERPNext Customizations for RFDesign"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@4csolutions.in"
app_license = "MIT"

fixtures = [
	{
		"doctype": "Custom Field",
		"filters" : [
            [
                "name",
                "in",
                [
					'Item Supplier-moq',
					'Item Supplier-supplier_stock',
					'Item Supplier-lead_time',
					'Item Supplier-price',
					'Item-supplier_options4',
					'Item-last_sync_date4',
					'Item-rohs4',
					'Item-manufacturer_lifecycle4',
					'Item-manufacturer_part_number4',
					'Item-manufacturer_name4',
					'Item-solution_4',
					'Item-supplier_options3',
					'Item-last_sync_date3',
					'Item-rohs3',
					'Item-manufacturer_lifecycle3',
					'Item-manufacturer_part_number3',
					'Item-manufacturer_name3',
					'Item-solution_3',
					'Item-last_sync_date2',
					'Item-supplier_options2',
					'Item-rohs2',
					'Item-manufacturer_lifecycle2',
					'Item-manufacturer_part_number2',
					'Item-manufacturer_name2',
					'Item-solution_2',
					'Item-supplier_options1',
					'Item-last_sync_date1',
					'Item-rohs1',
					'Item-manufacturer_lifecycle1',
					'Item-manufacturer_part_number1',
					'Item-manufacturer_name1',
					'Item-solution_1'
				]
			]
		]
	}
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/rfdesign/css/rfdesign.css"
# app_include_js = "/assets/rfdesign/js/rfdesign.js"

# include js, css files in header of web template
# web_include_css = "/assets/rfdesign/css/rfdesign.css"
# web_include_js = "/assets/rfdesign/js/rfdesign.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "rfdesign/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}
doctype_list_js = {"Item" : "public/js/item_list.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "rfdesign.install.before_install"
# after_install = "rfdesign.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "rfdesign.uninstall.before_uninstall"
# after_uninstall = "rfdesign.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "rfdesign.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"rfdesign.tasks.all"
# 	],
# 	"daily": [
# 		"rfdesign.tasks.daily"
# 	],
# 	"hourly": [
# 		"rfdesign.tasks.hourly"
# 	],
# 	"weekly": [
# 		"rfdesign.tasks.weekly"
# 	]
# 	"monthly": [
# 		"rfdesign.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "rfdesign.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "rfdesign.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "rfdesign.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"rfdesign.auth.validate"
# ]

# Translation
# --------------------------------

# Make link fields search translated document names for these DocTypes
# Recommended only for DocTypes which have limited documents with untranslated names
# For example: Role, Gender, etc.
# translated_search_doctypes = []
