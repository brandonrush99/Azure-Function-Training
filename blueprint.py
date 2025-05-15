# Register this blueprint by adding the following line of code 
# to your entry point file.  
# app.register_functions(blueprint) 
# 
# Please refer to https://aka.ms/azure-functions-python-blueprints


import azure.functions as func
import logging

blueprint = func.Blueprint()

def even_or_odd(val: int) -> str:
    if val % 2 == 0:
        return "even"
    else:
        return "odd"
    
@blueprint.route(route="blueprint_http_trigger", auth_level=func.AuthLevel.ANONYMOUS)
def blueprint_http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    num = req.params.get('number')
    if not num:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            num = req_body.get('name')

    if num:
        try:
            resp = even_or_odd(int(num))
            return func.HttpResponse(f"{num} is {resp}! Are you impressed?")
        except:
            return func.HttpResponse(f"{num} is not a number!")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a number in the query string or request body and I'll tell you if it is even or odd.",
             status_code=200
        )