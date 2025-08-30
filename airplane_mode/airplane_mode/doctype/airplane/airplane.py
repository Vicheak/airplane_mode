# Copyright (c) 2025, suonvicheak and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.naming import make_autoname

class Airplane(WebsiteGenerator):
	def autoname(self):
		# get linked airline name from the linked field
		airline_doc = frappe.get_doc("Airline", self.airline)
		airline_name = airline_doc.name.replace(" ", "")

		# create unique series for each airline
		series = f"{airline_name}-.###"

		# generate name with sequence that resets per airline
		self.name = make_autoname(series)

	def before_save(self):
		self.set_route()

	def before_insert(self):
		print("executing before_insert for Airplane")

	def validate(self):
		print("executing validate for Airplane")

	def on_update(self):
		print("executing on_update for Airplane")

	def after_insert(self):
		print("executing after_insert for Airplane")

	def set_route(self):
		# if not self.route:
		# 	self.route = f"airplanes/{self.name}"
		self.route = f"airplanes/{self.name}"
