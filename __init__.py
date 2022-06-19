import logging

import azure.functions as func


def main(req: func.HttpRequest, outputBlob: func.Out[str]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    date = req.params.get('date')
    host = req.params.get('host')
    message = req.params.get('message')

    
    if not date:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            date = req_body.get('date')
    
    if not host:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            host = req_body.get('host')
  
    if not message:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            message = req_body.get('message')
    
    
    if date and host and message:
        az_output = str(date) + str(host) + str(message)
        outputBlob.set(az_output)
        return func.HttpResponse(f"Hello, {host}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
