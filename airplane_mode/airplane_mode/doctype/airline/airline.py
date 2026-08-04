# Copyright (c) 2025, suonvicheak and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _

class Airline(Document):
	def on_change(self):
		# print("exeucting on_change for Airline")
		# self.send_alert_airline()
		pass

	def before_validate(self):
		# print("executing before_validate for Airline")
		# self.send_alert_airline()
		# if self.founding_year < 2000:
		# 	frappe.throw(
		# 		title="Error",
		# 		msg="Invalid founding year"
		# 	)
		pass

	def before_save(self):
		# print("executing before_save for Airline")
		# self.send_alert_airline()
		pass

	def send_alert_airline(self):
		# print("alerting airline:", self.name)
		frappe.msgprint(
			msg=f"alerting airline: {self.name}",
			title="Info",
			is_minimizable=True
		)

	def print_info(self):
		print("="*20)
		print(f"Airline info: {self.name} {self.founding_year} {self.customer_care_number} {self.headquarters}")
		print("="*20)
