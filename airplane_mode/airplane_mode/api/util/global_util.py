import frappe
from frappe.utils import now
from frappe.utils.pdf import get_pdf

# now
def get_now():
	return now()

# generate PDF
@frappe.whitelist(allow_guest=True)
def generate_invoice():
	cart = {
		"Samsung Galaxy S20": 10,
		"iPhone 13": 80
	}

	html = "<h1>Invoice from Star Electronics e-Store!</h1>"

	# add items to PDF HTML
	html += '<ol>'
	for item, qty in cart.items():
		html += f'<li>{item} - {qty}</li>'
	html += '</ol>'

	# attaching PDF to response
	frappe.local.response.filename = "invoice.pdf"
	frappe.local.response.filecontent = get_pdf(html)
	frappe.local.response.type = "pdf"
