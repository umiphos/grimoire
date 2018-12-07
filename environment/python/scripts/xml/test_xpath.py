from lxml import etree, objectify

xml = open('factura.xml')

import ipdb;ipdb.set_trace()
document = objectify.XML(xml)
# xpath_1 = '//ar:ApplicationResponse/cac:DocumentResponse/cbc:ResponseCode'
# xpath_2 = '//ar:ApplicationResponse/cac:DocumentResponse/cbc:Description'
xpath_1 = '//cbc:ResponseCode'
xpath_2 = '//cbc:Description'

namespaces = {'cbc': 'urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2', 'ar': 'urn:oasis:names:specification:ubl:schema:xsd:ApplicationResponse-2', 'cac': 'urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2'}


value = document.xpath(xpath_1, namespaces=namespaces)


# This is a small method to set a given dict of values into a given XML
def set_values(values, namespaces, xml):
    for value in values:
        xml.xpath(value, namespaces=namespaces)[0]._setText(values.get(
            value
        ))
