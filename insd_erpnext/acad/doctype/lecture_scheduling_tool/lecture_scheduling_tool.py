# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import calendar
from frappe import _
from frappe.model.document import Document
from frappe.utils import add_days, getdate
from erpnext.education.utils import OverlapError
import datetime
from datetime import datetime as _datetime
from six import string_types
from frappe.utils.data import format_time

class LectureSchedulingTool(Document):

	@frappe.whitelist()
	def schedule_course(self):
		"""Creates course schedules as per specified parameters"""

		course_schedules = []
		course_schedules_errors = []
		rescheduled = []
		reschedule_errors = []

		# self.validate_mandatory()
		self.validate_date()
		# self.instructor_name = frappe.db.get_value(
		# 	"Instructor", self.instructor, "instructor_name")

		student_group = self.student_group
		# course = self.course
		# instructor = self.instructor
		# from_time = self.from_time
		# to_time = self.to_time
		_input_day_array = self.repeats_every.split(',')
		start_date =  _datetime.strptime(self.from_date, "%Y-%m-%d") if isinstance(self.from_date, string_types) else self.from_date
		end_date =   _datetime.strptime(self.to_date, "%Y-%m-%d") if isinstance(self.to_date, string_types) else self.to_date
		delta = datetime.timedelta(days=1)
		day_name= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
		while start_date<=end_date:
			
			date = str(start_date.strftime('%Y-%m-%d'))
			day = day_name[start_date.weekday()]
			if day in _input_day_array or _input_day_array[0]=='Everyday':
				# subject_lecture_list = frappe.get_all('Schedule Subject Lecture',filters={'student_group':student_group,'schedule_date':date,'from_time':self.from_time})
				# if len(subject_lecture_list)>0:
				# 	frappe.throw(f"{student_group} already has a lecture scheduled on {startdate} and time {from_time}")
				# else:
				lecture = self.create_lecture_doc(date)
				try:
						if lecture:
							lecture.save()
							frappe.db.commit()
										
				except OverlapError:
						frappe.throw('Cannot Create Lecture')
			start_date += delta


		# group_based_on, course = frappe.db.get_value(
		# 	"Student Group", self.student_group, ["group_based_on", "course"])

		# if group_based_on == "Course":
		# 	self.course = course

		# if self.reschedule:
		# 	rescheduled, reschedule_errors = self.delete_course_schedule(
		# 		rescheduled, reschedule_errors)

		# date = self.course_start_date
		# while date < self.course_end_date:
		# 	if self.day == calendar.day_name[getdate(date).weekday()]:
		# 		course_schedule = self.make_course_schedule(date)
		# 		try:
		# 			print('pass')
		# 			course_schedule.save()
		# 		except OverlapError:
		# 			print('fail')
		# 			course_schedules_errors.append(date)
		# 		else:
		# 			course_schedules.append(course_schedule)

		# 		date = add_days(date, 7)
		# 	else:
		# 		date = add_days(date, 1)
		# return dict(
		# 	course_schedules=course_schedules,
		# 	course_schedules_errors=course_schedules_errors,
		# 	rescheduled=rescheduled,
		# 	reschedule_errors=reschedule_errors
		# )
	def create_lecture_doc(self,start_date):
		lecture = frappe.new_doc("Schedule Subject Lecture")
		lecture.student_group = self.student_group
		lecture.course = self.course
		lecture.schedule_date = start_date
		lecture.from_time = self.from_time
		lecture.to_time = self.to_time
		lecture.instructor = self.instructor
		return lecture


	
	def validate_mandatory(self):
		"""Validates all mandatory fields"""

		fields = ['course', 'room', 'instructor', 'from_time',
				  'to_time', 'course_start_date', 'course_end_date', 'day']
		for d in fields:
			if not self.get(d):
				frappe.throw(_("{0} is mandatory").format(
					self.meta.get_label(d)))

	def validate_date(self):
		"""Validates if Course Start Date is greater than Course End Date"""
		if self.from_date > self.to_date:
			frappe.throw(
				_("Course Start Date cannot be greater than Course End Date."))

	def delete_course_schedule(self, rescheduled, reschedule_errors):
		"""Delete all course schedule within the Date range and specified filters"""

		schedules = frappe.get_list("Course Schedule",
			fields=["name", "schedule_date"],
			filters=[
				["student_group", "=", self.student_group],
				["course", "=", self.course],
				["schedule_date", ">=", self.course_start_date],
				["schedule_date", "<=", self.course_end_date]
			]
		)

		for d in schedules:
			try:
				if self.day == calendar.day_name[getdate(d.schedule_date).weekday()]:
					frappe.delete_doc("Course Schedule", d.name)
					rescheduled.append(d.name)
			except:
				reschedule_errors.append(d.name)
		return rescheduled, reschedule_errors

	def make_course_schedule(self, date):
		"""Makes a new Course Schedule.
		:param date: Date on which Course Schedule will be created."""

		course_schedule = frappe.new_doc("Course Schedule")
		course_schedule.student_group = self.student_group
		course_schedule.course = self.course
		course_schedule.instructor = self.instructor
		course_schedule.instructor_name = self.instructor_name
		course_schedule.room = self.room
		course_schedule.schedule_date = date
		course_schedule.from_time = self.from_time
		course_schedule.to_time = self.to_time
		return course_schedule
