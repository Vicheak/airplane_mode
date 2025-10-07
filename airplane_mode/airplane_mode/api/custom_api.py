import frappe
import time


@frappe.whitelist()
def execute_func(*args, **kwargs):
	print("executing func!")
	print(args)
	print(kwargs)
	print("="*20)

# test with realtime
@frappe.whitelist()
def execute_realtime(*args, **kwargs):
	print("publish realtime event")

	for i in range(1, 101):
		frappe.publish_progress(i,
			title="Processing Data",
			description=f"Step {i} of 100 completed"
		)
		time.sleep(0.05)

	frappe.publish_realtime("my_event", message={"test": "test-value"})

# test with background job
def long_running_job(param1, param2):
    print("="*20)
    print("executing long_running_job")
    print("="*20)

@frappe.whitelist()
def execute_cronjob():
	print("="*20)
	print("executing cronjob")
	# frappe.enqueue(long_running_job, queue="short", param1="param1", param2="param2")
	# frappe.enqueue("airplane_mode.airplane_mode.api.cron.schedule.long_running_job", queue="long", param1="param1", param2="param2")

	airplane_doc = frappe.get_doc("Airplane", "Airline1-001")
	frappe.enqueue_doc(
		doctype="Airplane",
		name=airplane_doc.name,
		method="do_something",
		queue="long",
		timeout=1500,
		param="param"
	)
