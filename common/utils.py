



def custom_response(
    data=None, status_code=None, message=None, error=None, response=None
):
    if status_code == 200:

        response.status_code = 200
    elif status_code == 400:
        response.status_code = 400
    else:
        response.status_code = 500

    result = {
        "data": data,
        "status_code": status_code,
        "message": message,
        "error": error,
    }
    return result