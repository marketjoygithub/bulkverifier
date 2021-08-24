import requests
import json
def verifier(email):
    url ='https://marketjoyemailverifier.azurewebsites.net/up/'+ email
    r=  requests.get(url)
    data = (r.json())
    delivery = data['deliverable'] 
    catch_all = data['catch_all']
    if delivery==True and catch_all==False:
        return 'Valid Email'
    elif delivery==True and catch_all == True:
        return '50:50'
    else:
        return 'Invalid Email'
