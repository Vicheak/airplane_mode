// Copyright (c) 2025, suonvicheak and contributors
// For license information, please see license.txt

frappe.ui.form.on("Flight Passenger", {
	refresh(frm) {
        frappe.realtime.on('my_event', (data) => {
            console.log(data)
        })
	},
});
