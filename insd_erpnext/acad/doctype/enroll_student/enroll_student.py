# Copyright (c) 2021, INSD and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class EnrollStudent(Document):
	def before_naming(self):
		self.title = f"{self.first_name} {self.middle_name} {self.last_name}"
