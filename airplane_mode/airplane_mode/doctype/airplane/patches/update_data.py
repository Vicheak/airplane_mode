import frappe

def execute():
	airplane = frappe.get_doc("Airplane", "PhnomPenhAirway-010")
	airplane.capacity = 40
	airplane.save()
	frappe.db.commit()
