# Copyright (c) 2025, suonvicheak and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname

class Airplane(Document):
	def autoname(self):
		# get linked airline name from the linked field
		airline_doc = frappe.get_doc("Airline", self.airline)
		airline_name = airline_doc.name.replace(" ", "")

		# create unique series for each airline
		series = f"{airline_name}-.###"

		# generate name with sequence that resets per airline
		self.name = make_autoname(series)
