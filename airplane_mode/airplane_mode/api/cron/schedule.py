import frappe

def long_running_job(param1, param2):
    print("="*20)
    print("executing long_running_job under module path")
    print("="*20)

def alert_job():
    frappe.publish_realtime(
        event='msgprint',
        message='This is an alert from the background job!',
        user=None
    )
