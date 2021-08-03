# Copyright (c) 2021, INSD and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class Stream(Document):
	def before_naming(self):
		if self.stream_name == 'Fashion Design':
			self.stream_abbreviation = 'FD'
		if self.stream_name == 'Interior Design':
			self.stream_abbreviation = 'ID'
		if self.stream_name == 'Graphic Design':
			self.stream_abbreviation = 'GD'
		if self.stream_name == 'Jewellery Design':
			self.stream_abbreviation = 'JD'
		if self.stream_name == 'Textile Design':
			self.stream_abbreviation = 'TD'
		if self.stream_name == 'Animation':
			self.stream_abbreviation = 'Animation'
		if self.stream_name == 'User Interface / User Experience':
			self.stream_abbreviation = 'UI/UX'
		if self.stream_name == 'Fashion Styling':
			self.stream_abbreviation = 'FS'
