// Copyright (c) 2016, INSD and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Generate Timetable"] = {
	"filters": [
		{
			"fieldname": "timetable_for",
			"fieldtype": "Link",
			"label": "timetable_for",
			"options": "Student Batch",
			"reqd": 1
		
		   },
		   {
			"fieldname": "from_date",
			"fieldtype": "Date",
			"label": "from_date",
			"reqd": 1
		
		   },
		   {
			"fieldname": "to_date",
			"fieldtype": "Date",
			"label": "to_date",
			"reqd": 1
		   }
	]
};
