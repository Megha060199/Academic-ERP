	# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class StudentAttendanceTool(Document):
	pass

@frappe.whitelist()
def get_student_attendance_records(date=None, student_group=None, course_schedule=None):
	student_list = []
	student_attendance_list = []

	student_group = frappe.db.get_value("Schedule Subject Lecture", course_schedule, "student_group")
	lecture_conducted = frappe.db.get_value("Schedule Subject Lecture",course_schedule,'lecture_conducted')
	if lecture_conducted:
		if student_group:
			student_list = frappe.get_list("Student Group Student", fields=["student","parent"] ,
			filters={"parent": student_group })
		# if not student_list:
		# 	student_list = frappe.get_list("Student Group Student", fields=["student", "student_name", "group_roll_number"] ,
		# 		filters={"parent": student_group, "active": 1}, order_by= "group_roll_number")
		# else:
			student_attendance_list= frappe.db.sql('''select student, status from `tabStudent Attendance` where 
				student_group= %s and date= %s and \
				(course_schedule is Null or course_schedule='')''',
				(student_group, date), as_dict=1)

		for attendance in student_attendance_list:
			for student in student_list:
				if student.student == attendance.student:
					student.status = attendance.status	
		return student_list
	else:
		return []