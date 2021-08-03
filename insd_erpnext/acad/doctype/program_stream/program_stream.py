# Copyright (c) 2021, INSD and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class ProgramStream(Document):
	def before_save(self):
		self.program_stream_name = f"{self.program} {self.stream}"
