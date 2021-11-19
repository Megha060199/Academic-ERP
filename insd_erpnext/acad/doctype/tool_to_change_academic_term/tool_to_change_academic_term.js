// Copyright (c) 2021, INSD and contributors
// For license information, please see license.txt

frappe.ui.form.on('Tool to change academic Term', {
	refresh(frm) {
		frm.disable_save();
		frm.page.set_primary_action(__('Change Academic Term'), () => {
			frm.call('change_academic_term')
				.then(
					frm.refresh(),
				);
		});
	}
	// refresh: function(frm) {

	// }
});
