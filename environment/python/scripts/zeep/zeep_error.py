from zeep import Client, Settings
from zeep.plugins import HistoryPlugin
from zeep.wsse.username import UsernameToken

settings = Settings(strict=False, xml_huge_tree=True)
history = HistoryPlugin()
client = Client(wsdl='https://e-factura.sunat.gob.pe/ol-ti-itcpfegem/billService?wsdl',
                wsse=UsernameToken('MODDATOS','MODDATOS'), settings=settings, plugins=[history])
