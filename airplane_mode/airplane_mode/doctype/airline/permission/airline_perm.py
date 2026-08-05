import frappe


def airline_query(user):
    user = user or frappe.session.user
    if user == "Administrator":
        return ""
    # Airline that belong to user or assigned by user
    return "(`tabAirline`.owner = {user})".format(user=frappe.db.escape(user))


def airline_has_permission(doc, user=None, permission_type=None):
    user = user or frappe.session.user
    if user == "Administrator":
        return True
    # if permission_type == "read":
        # return doc.owner == user
    # return None
    return doc.owner == user
