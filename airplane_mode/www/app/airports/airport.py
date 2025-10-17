import frappe

def get_context(context):
    print("="*20)
    print("executing get_context:", frappe.form_dict.name)
    airport_name = frappe.form_dict.name
    airport = frappe.get_doc("Airport", airport_name)
    print("airport:", airport.as_dict())
    context.airport = airport
