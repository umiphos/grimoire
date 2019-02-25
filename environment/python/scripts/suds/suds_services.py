from suds.client import Client
url = 'http://localhost:1234/sami/2009/08/reporting?wsdl'
client = Client(url)
functions = [m for m in client.wsdl.services[0].ports[0].methods]
count = 0
for function_name in functions:
    print (function_name)
    count+=1
print ("\nNumber of services exposed : " ,count)
