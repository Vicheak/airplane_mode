import frappe

def execute():
	airplanes = frappe.get_all("Airplane", pluck="name")
	for airplane in airplanes:
		airplane_doc = frappe.get_doc("Airplane", airplane)
		# if not airplane_doc.route:
		# 	airplane_doc.route = airplane_doc.name
		airplane_doc.set_route()
		airplane_doc.save()
	frappe.db.commit()
