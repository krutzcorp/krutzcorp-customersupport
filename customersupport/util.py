from flask import request

"""This is a utils file for common utility functions"""

def get_param_from_request_if_not_empty(param_name):
    """Get a query parameter from the request, or None if the parameter is empty or missing."""
    value = request.args.get(param_name)
    if value is not None and value != "":
        return value
    else:
        return None

def get_post_data(data_name):
    if data_name in request.form:
        return request.form[data_name]
    else:
        return None


