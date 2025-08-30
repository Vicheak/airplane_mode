import frappe

@frappe.whitelist()
def execute_func(*args, **kwargs):
	print("execute func!")
	print(args)
	print(kwargs)
	print("="*20)
