import frappe

def execute():
	# airplanes = frappe.get_all("Airplane")
	airplanes = frappe.get_list("Airplane", fields=["*"])
	print("="*20)
	print(airplanes)
	print("="*20)
