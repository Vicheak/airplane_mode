from frappe import _

def get_data():
	return {
		"fieldname": "airline", # field in doctype that link to
		"transactions": [
			{
				"label": _("Related Airplanes"),
				"items": ["Airplane"] # doctype to link
			}
		]
	}
