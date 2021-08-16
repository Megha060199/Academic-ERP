# Copyright (c) 2021, INSD and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class Programs(Document):
	def before_naming(self):
		if self.program_name == 'Bachelor Of Design':
			self.program_abbreviation = 'B.Des'
			
		if self.program_name == 'Bachelor of Science':
			self.program_abbreviation = 'B.S.C'
		
		if self.program_name == 'Masters Of Design':
			self.program_abbreviation = 'M.Des'
		
		if self.program_name == '2 year diploma':
			self.program_abbreviation = 'Diploma-2'
		
		if self.program_name == '1 year diploma':
			self.program_abbreviation = 'Diploma-1'
		
		if self.program_name == 'Certificate':
			self.program_abbreviation = 'Certificate'

		if self.program_name == 'Master of Business Administration':
			self.program_abbreviation = 'MBA'
		
	def before_save(self):
		if self.program_name == 'Bachelor Of Design':
			self.number_of_semesters = 8
		if self.program_name == 'Bachelor of Science':
			self.number_of_semesters = 6
		if self.program_name == 'Masters Of Design':
			self.number_of_semesters = 4
		if self.program_name == '2 year diploma':
			self.number_of_semesters = 4
		if self.program_name == '1 year diploma':
			self.number_of_semesters = 2
		if self.program_name == 'Certificate':
			self.number_of_semesters = 1
		if self.program_name == 'Master of Business Administration':
			self.number_of_semesters = 4
