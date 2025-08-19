# Copyright (c) 2025, suonvicheak and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname

class AirplaneTicket(Document):
	def autoname(self):
		airplane_doc = frappe.get_doc("Airplane", self.flight)
		airplane_name = airplane_doc.name.replace(" ", "")

		series = (f"{airplane_name}-{self.source_airport_code}-"
				  f"to-{self.destination_airport_code}-.##")

		self.name = make_autoname(series)
