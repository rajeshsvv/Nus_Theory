from zeep import Client,Settings
from zeep import xsd
client=Client("http://www.soapclient.com/xml/soapresponder.wsdl")
with client.settings(raw_response=True):
    resp=client.service.Method1('vijay','doing good')

    assert resp.status_code==200,'Success'
    assert resp.content
    #print(resp)

'''Transport Layer Security For self signed certificates,,

##TLS verification process...'''
# from requests import Session
# from zeep import Client
#from zeep.cache import SqliteCache
# from zeep.transports import Transport
# session=Session()
# session.verify='Path to the certificate (.pem or .crt files)'

'''To disable TLS verification we use session.verify=False (not recommended)'''

# transport=Transport(session=session,  timeout=20(default timeout is 300 sec), cache=SqliteCache())
# client=Client('path to wsdl',transport)



'''HTTP AUTHENTICATION PROCESS'''

# from requests import Session
# from requests.auth import HTTPBasicAuth,HTTPDigestAuth,HTTPProxyAuth
# from zeep import Client
# from zeep.transports import Transport
# session=Session()
# session.auth=HTTPBasicAuth('user','passwd')
# transport=Transport(session=session)
# client=Client('wsdl url',transport=transport)
'''
UsernameToken and Signature together
To use UsernameToken and Signature together, then you can pass both together to the client in a list'''

# >>> from zeep import Client
# >>> from zeep.wsse.username import UsernameToken
# >>> from zeep.wsse.signature import Signature
# >>> user_name_token = UsernameToken('username', 'password')
# >>> signature = Signature(private_key_filename, public_key_filename,
# ...     optional_password)
# >>> client = Client(
# ...     'http://www.webservicex.net/ConvertSpeed.asmx?WSDL',
# ...     wsse=[user_name_token, signature])
#
# '''
'''

'''