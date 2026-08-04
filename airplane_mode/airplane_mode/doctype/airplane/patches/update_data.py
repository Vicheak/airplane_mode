import frappe

def execute():
	airplane = frappe.get_doc("Airplane", "Airline1-001")
	airplane.capacity = 40
	airplane.save()
	frappe.db.commit()
