# Copyright (c) 2021, INSD and contributors
# For license information, please see license.txt


from frappe.model.document import Document
import frappe
from frappe import _
class ProgramStreamSemesterWiseSyllabus(Document):
	def validate(self):
		subject_data = frappe.db.sql("""
		Select subject from `tabsubjects` 
		where parent != %(selfname)s""",{
			'selfname':self.name
		},as_dict=True)
		print(subject_data)
		for sub in self.subjects:
			if sub.subject in ([present_sub.subject for present_sub in subject_data]):
				frappe.throw(f"{sub.subject} already present in syllabus of another program/stream/semester")
			if sub.subject in self.subjects:
				frappe.throw('Subject Already present in this syllabus')


