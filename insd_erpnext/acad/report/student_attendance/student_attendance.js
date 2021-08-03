// Copyright (c) 2016, INSD and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Student Attendance"] = {
	"filters": [
		{
			"fieldname": "from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"reqd": 1
		},
		{
			"fieldname": "to_date",
			"label": __("to_date"),
			"fieldtype": "Date",
			"reqd": 1
		},
		{
			"fieldname": "student",
			"label": __("student"),
			"fieldtype": "Link",
			"options":"Enroll Student",
			"reqd": 1
		},
	]
};
