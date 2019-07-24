from zeep import Client
from zeep import xsd
client = Client('http://my-endpoint.com/production.svc?wsdl')
# service is a ServiceProxy object. It will check if there
# is an operation with the name `X` defined in the binding
# and if that is the case it will return an OperationProxy
client.service.X()
# The operation can also be called via an __getitem__ call.
# This is useful if the operation name is not a valid
# python attribute name.
client.service['X-Y']()
