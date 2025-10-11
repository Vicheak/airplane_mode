import frappe

def long_running_job(param1, param2):
	print("="*20)
	print("executing long_running_job under module path")
	print("="*20)

def hook_job():
	print("="*20)
	print("executing hook_job")
	print("="*20)

	# write to a doctype for debugging
	frappe.get_doc({
		"doctype": "Error Log",
		"error": "executing hook_job"
	}).insert(ignore_permissions=True)

def alert_job():
	print("="*20)
	print("executing alert_job")
	print("="*20)

@frappe.whitelist()
def custom_schedule_event():
	# check if Scheduler Event already exists
	sch_eve_name = frappe.db.exists("Scheduler Event", {"scheduled_against": "Airplane"})
	if not sch_eve_name:
		sch_eve = frappe.new_doc("Scheduler Event")
		sch_eve.scheduled_against = "Airplane"
		sch_eve.save(ignore_permissions=True)
		print(f"Created Scheduler Event: {sch_eve.name}")
	else:
		sch_eve = frappe.get_doc("Scheduler Event", sch_eve_name)
		print(f"Scheduler Event already exists: {sch_eve.name}")

	# check if Scheduled Job Type already exists
	job_name = frappe.db.exists("Scheduled Job Type", {"scheduler_event": sch_eve.name})
	if not job_name:
		job = frappe.new_doc("Scheduled Job Type")
		job.frequency = "Cron"
		job.scheduler_event = sch_eve.name
		job.cron_format = "* * * * *"  # every minute
		job.method = "airplane_mode.airplane_mode.api.cron.schedule.alert_job"
		job.save(ignore_permissions=True)
		print(f"Created Scheduled Job Type: {job.name}")
	else:
		job = frappe.get_doc("Scheduled Job Type", job_name)
		print(f"Scheduled Job Type already exists: {job.name}")

	frappe.msgprint(
		f"Scheduler successfully created or already exists. Event: {sch_eve.name} and Job: {job.name}")
