# -*- coding: utf-8 -*-
# Copyright (c) 2021, INSD and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class TooltochangeacademicTerm(Document):
	@frappe.whitelist()
	def change_academic_term(self):
		all_student_list = frappe.get_all('Enroll Student',filters= {'current_academic_term':self.academic_term,'campus':self.campus,'enrolled_course':self.enrolled_course})
		all_batches_list = frappe.get_all('Student Batch',filters={'academic_term':self.academic_term,'progam_and_stream':self.enrolled_course,'campus':self.campus})
		if len(all_student_list)==0:
			frappe.throw('No students to change the academic term')
		if self.academic_term == self.new_academic_term:
			frappe.throw('Current and new academic term must be different')
		for student in all_student_list:
			studentdoc = frappe.get_doc('Enroll Student',student.name)
			studentdoc.current_academic_term = self.new_academic_term
			studentdoc.save()
		# for batch in all_batches_list:
		# 	batchdoc = frappe.get_doc('Student Batch',batch.name)
		# 	batchdoc.academic_term = self.new_academic_term
		# 	batchdoc.save()
		frappe.db.commit()
		frappe.msgprint(f'Academic term changed for student of course {self.enrolled_course} from {self.academic_term} to {self.new_academic_term}')
		self.reload()