# Copyright (c) 2025, suonvicheak and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.naming import make_autoname

class Airplane(WebsiteGenerator):
	def autoname(self):
		# print("executing autoname for Airplane")

		# get linked airline name from the linked field
		airline_doc = frappe.get_doc("Airline", self.airline)
		airline_name = airline_doc.name.replace(" ", "")

		# create unique series for each airline
		series = f"{airline_name}-.###"

		# generate name with sequence that resets per airline
		self.name = make_autoname(series)

	def before_save(self):
		# print("executing before_save for Airplane")
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

	def do_something(self, param=None):
		print(f"executing do_something for {self.name} with param={param}")
		import time
		time.sleep(5)
		print("="*20)
		print("Task completed")
		print("="*20)
