from requests import Session
from requests.auth import HTTPBasicAuth  # or HTTPDigestAuth, or OAuth1, etc.
from zeep import Client
from zeep.transports import Transport
import logging.config


logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(name)s: %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'zeep.transports': {
            'level': 'DEBUG',
            'propagate': True,
            'handlers': ['console'],
        },
    }
})

session = Session()
session.auth = HTTPBasicAuth(username='hari',password='123')
client = Client('http://my-endpoint.com/production.svc?wsdl',
    transport=Transport(session=session))


transport = Transport()
client = Client(
    'http://www.webservicex.net/ConvertSpeed.asmx?WSDL',
    transport=transport)

print(logging)