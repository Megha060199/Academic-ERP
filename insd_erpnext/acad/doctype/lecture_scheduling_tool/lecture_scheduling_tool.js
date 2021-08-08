// Copyright (c) 2016, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt


frappe.ui.form.on('Lecture Scheduling Tool', {
	setup(frm) {
		frm.add_fetch('student_group', 'program', 'program');
		frm.add_fetch('student_group', 'course', 'course');
		frm.add_fetch('student_group', 'academic_year', 'academic_year');
		frm.add_fetch('student_group', 'academic_term', 'academic_term');
	},
	refresh(frm) {
		frm.disable_save();
		frm.page.set_primary_action(__('Schedule Course'), () => {
			frm.call('schedule_course')
				.then(
					cur_frm.refresh()
				);
		});
	},
	student_group:function(frm){
		if(frm.doc.student_group){
			frm.set_query('course',()=> {
				return {
					query: 'insd_erpnext.acad.doctype.schedule_subject_lecture.schedule_subject_lecture.get_subjects',
					filters:{
						group_name:frm.doc.student_group
					}	
					
			}})
			

		}
	}
});