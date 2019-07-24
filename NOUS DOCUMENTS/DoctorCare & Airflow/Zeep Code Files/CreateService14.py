from zeep import Client
from zeep import xsd
client = Client('http://my-endpoint.com/production.svc?wsdl')

with client.settings(raw_response=True):
    response = client.service.myoperation()
# response is now a regular requests.Response object
assert response.status_code == 200
assert response.content
