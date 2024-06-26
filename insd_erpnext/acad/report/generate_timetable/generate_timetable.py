# Copyright (c) 2013, INSD and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = ['subject','instructor','from_time','to_time','schedule_date'],get_data(filters) or []
	return columns, data

def get_data(filters):

	timetable_arr = frappe.db.sql("""Select s.course as subject, s.instructor,
s.from_time,
s.to_time,
s.schedule_date
from `tabSchedule Subject Lecture` as s 
where s.student_group = %(timetable_for)s
AND 
s.schedule_date BETWEEN %(from_date)s AND %(to_date)s""",{
	"timetable_for":filters.timetable_for,
	"from_date":filters.from_date,
	"to_date":filters.to_date
},as_dict=True)
	print(timetable_arr,'timetable')
	return timetable_arr
