from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Student & Instructor"),
			"items": [
				{
					"type": "doctype",
					"name": "Enroll Student",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Student Batch",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Student Attendance Tool",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Instructor",
					"onboard": 1,
				},

				

			]
		},
		{
			"label": _("Syllabus & Lecture"),
			"items": [
				{
					"type": "doctype",
					"name": "Subject",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Program Stream Semester Wise Syllabus",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Schedule Subject Lecture",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Lecture Scheduling Tool",
					"onboard": 1,
				},

				

			]
		},
		{
			"label": _("Data Filling"),
			"items": [
				{
					"type": "doctype",
					"name": "Academic Year",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Academic Term",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Programs",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Stream",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Program Stream",
					"onboard": 1,
				},

				

			]
		},
				{
			"label": _("Reports"),
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Generate Timetable",
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Student Attendance",
				},

				

			]
		},
	
	]
