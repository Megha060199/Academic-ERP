# Copyright (c) 2013, INSD and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = ['subject','attendance_percent'], get_data(filters) or []
	return columns, data

def get_data(filters):
	from_date = filters.from_date
	to_date = filters.to_date
	student = filters.student
	all = get_total_lects(from_date,to_date,student)
	attended = get_attended_lects(from_date,to_date,student)
	attended_subjects = [item.subject_name for item in attended]
	lectures_all_and_attended = []
	lecture_wise_att = []
	for all_lect in all:
		for att in attended:
			if all_lect.subject_name in attended_subjects:
				if all_lect.subject_name == att.subject_name:
					lectures_all_and_attended.append({'subject_name':all_lect.subject_name,'total':all_lect.total_conducted,'attended':att.no_of_days_pesent})
					break
			else:
				lectures_all_and_attended.append({'subject_name':all_lect.subject_name,'total':all_lect.total_conducted,'attended':0})
	for lect in lectures_all_and_attended:
		percent = (lect['attended']/lect['total'])*100
		lecture_wise_att.append({'subject':lect['subject_name'],'attendance_percent':percent})
	return lecture_wise_att



def get_total_lects(fromdate,todate,student):
	print(student,'student')
	alllectlist = frappe.db.sql("""Select indsub.subject_name,count(ssll.name) as total_conducted
from `tabEnroll Student` as es
JOIN
`tabAcademic Term` as att
ON
es.current_academic_term = att.name
JOIN
`tabProgram Stream Semester Wise Syllabus` as pssws
ON 
es.enrolled_course = pssws.program_and_stream
AND 
SUBSTRING(es.current_academic_term,LENGTH(es.current_academic_term),LENGTH(es.current_academic_term)) = pssws.semester
JOIN 
`tabsubjects` as s
ON 
s.parent = pssws.name
JOIN 
`tabSubject` as indsub
ON 
s.subject = indsub.name
JOIN 
`tabSchedule Subject Lecture` as ssll
ON 
ssll.course = s.subject
WHERE 
es.name = %(student)s
AND
ssll.lecture_conducted = 1
AND ssll.schedule_date BETWEEN %(fromdate)s AND %(todate)s
GROUP BY indsub.subject_name""",{"student":student,"fromdate":fromdate,"todate":todate},as_dict=True)
	return alllectlist 

def get_attended_lects(fromdate,todate,student):
	attended_lect = frappe.db.sql("""        Select indsub.subject_name,count(st.name) as no_of_days_pesent
        from `tabEnroll Student` as es
        JOIN
        `tabAcademic Term` as att
        ON
        es.current_academic_term = att.name
        JOIN
        `tabProgram Stream Semester Wise Syllabus` as pssws
        ON 
        es.enrolled_course = pssws.program_and_stream
        AND 
        SUBSTRING(es.current_academic_term,LENGTH(es.current_academic_term),LENGTH(es.current_academic_term)) = pssws.semester
        JOIN 
        `tabsubjects` as s
        ON 
        s.parent = pssws.name
    JOIN 
        `tabSubject` as indsub
        ON 
        s.subject = indsub.name
        JOIN 
        `tabSchedule Subject Lecture` as ssll
        ON 
        ssll.course = s.subject
     JOIN 
        `tabStudent Attendance` as st
        ON 
        ssll.name  = st.course_schedule 
        WHERE 
        es.name = %(student)s
        AND 
        st.student = %(student)s
        AND
        ssll.lecture_conducted = 1
        AND
        st.status = 'Present'
		AND ssll.schedule_date BETWEEN %(fromdate)s AND %(todate)s
        GROUP BY indsub.subject_name""",{"fromdate":fromdate,"todate":todate,"student":student},as_dict=True)
	return attended_lect