# Copyright (c) 2021, INSD and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import getdate,today
from frappe.model.document import Document
import re
class EnrollStudent(Document):
	def before_naming(self):
		self.title = f"{self.first_name} {self.middle_name} {self.last_name}"
	def validate(self):
		regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
		if len(self.mobile_number)<10 or len(self.parents_mobile_number)<10 :
			frappe.throw('Please enter a valid mobile number')
		if self.date_of_birth and getdate(self.date_of_birth) >= getdate(today()):
			frappe.throw("Date of Birth cannot be greater than today.")
		if not (re.fullmatch(regex, self.email_id)):
			frappe.throw('Please enter a valid email id')
