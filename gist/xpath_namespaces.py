# Como repetir este bonito ejercicio:
# primero partimos de que el xml ya existe descomprimido, si quieres sacarlo de un zip, pues...
# URLs de ayuda
# http://xmlprettyprint.com/
# http://www.freeformatter.com/


from lxml import etree

old_xml = etree.parse('old.xml')
new_xml = etree.parse('new.xml')

namespaces = {
    'cac': 'urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2',
    'cbc': 'urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2',
    'ccts':'urn:un:unece:uncefact:documentation:2',
    'ds': 'http://www.w3.org/2000/09/xmldsig#',
    'ext': 'urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2',
    'qdt':'urn:oasis:names:specification:ubl:schema:xsd:QualifiedDatatypes-2',
    'sac': 'urn:sunat:names:specification:ubl:peru:schema:xsd:SunatAggregateComponents-1',
    'udt':'urn:un:unece:uncefact:data:specification:UnqualifiedDataTypesSchemaModule:2',
    'xsi': 'http://www.w3.org/2001/XMLSchema-instance'}
NS = namespaces
# Lineas que cambian entre documento y documento

# original:  Es un string que viene del documento descargado CDR de la SUNAT
# contenido: new_xml.find('//ds:DigestValue',namespaces=namespaces).text
old_xml.find('//ds:DigestValue',namespaces=namespaces).text = new_xml.find('//ds:DigestValue',namespaces=namespaces).text


# original:  Es un string que viene del documento descargado CDR de la SUNAT
# contenido: new_xml.find('//cbc:ID',namespaces=namespaces).text
old_xml.find('//cbc:ID',namespaces=namespaces).text = new_xml.find('//cbc:ID',namespaces=namespaces).text

# Original: "14:51:26"
# contenido: "invoice.time"
old_xml.find('//cbc:ResponseTime',namespaces=namespaces).text = new_xml.find('//cbc:ResponseTime',namespaces=namespaces).text

# original:  'F001-00000004'
# contenido: 'invoice.number'
old_xml.find('//cac:DocumentResponse/cac:Response/cbc:ReferenceID',namespaces=namespaces).text = 'F001-00000004'

# Original: "La Nota de Debito numero F001-00000004, ha sido aceptada'" % self.debit_id.name
# contenido: "La Nota de Debito numero %s, ha sido aceptada'" % self.debit_id.name
old_xml.find('//cac:DocumentResponse/cac:Response/cbc:Description',namespaces=namespaces).text = '%s%s%s' % ('La Nota de Debito numero ', 'F001-00000004',', ha sido aceptada')

# original:  'F001-00000004'
# contenido: 'invoice.name'
old_xml.find('//cbc:IssueDate', namespaces=namespaces).text = new_xml.find('//cbc:IssueDate',namespaces=namespaces).text

# original:  '2017-05-10'
# contenido: 'we really don't know right now
old_xml.find('//cbc:ResponseDate', namespaces=namespaces).text = new_xml.find('//cbc:ResponseDate', namespaces=namespaces).text

# original:  'F001-00000004'
# contenido: 'This one will come from the main document'
old_xml.find('//cac:DocumentReference/cbc:ID', namespaces=namespaces).text = new_xml.find('//cac:DocumentReference/cbc:ID', namespaces=namespaces).text

etree.tostring(new_xml) == etree.tostring(old_xml)
# Para validar que el documento este bien






xpaths = [
    '//ds:DigestValue',
    '//cbc:ID',
    '//cbc:ResponseTime',
    '//cbc:ReferenceID',
    '//cbc:Description',
    '//cbc:IssueDate',
    '//cbc:ResponseDate',
    '//cac:DocumentReference/cbc:ID'
]









values = [
old_xml.find('//ds:DigestValue',namespaces=namespaces).text,
new_xml.find('//ds:DigestValue',namespaces=namespaces).text,
old_xml.find('//cbc:ID',namespaces=namespaces).text,
new_xml.find('//cbc:ID',namespaces=namespaces).text,
old_xml.find('//cbc:ResponseTime',namespaces=namespaces).text,
new_xml.find('//cbc:ResponseTime',namespaces=namespaces).text,
old_xml.find('//cac:DocumentResponse/cac:Response/cbc:ReferenceID',namespaces=namespaces).text,
new_xml.find('//cac:DocumentResponse/cac:Response/cbc:ReferenceID',namespaces=namespaces).text,
old_xml.find('//cac:DocumentResponse/cac:Response/cbc:Description',namespaces=namespaces).text,
new_xml.find('//cac:DocumentResponse/cac:Response/cbc:Description',namespaces=namespaces).text,
old_xml.find('//cbc:IssueDate', namespaces=namespaces).text,
new_xml.find('//cbc:IssueDate', namespaces=namespaces).text,
old_xml.find('//cbc:ResponseDate', namespaces=namespaces).text,
new_xml.find('//cbc:ResponseDate', namespaces=namespaces).text,
old_xml.find('//cac:DocumentReference/cbc:ID', namespaces=namespaces).text,
new_xml.find('//cac:DocumentReference/cbc:ID', namespaces=namespaces).text,
]

values_II = [
expected_xml.find('.//ds:DigestValue',namespaces=NS)[0],
cdr_file.find('.//ds:DigestValue',namespaces=NS).text,
expected_xml.find('.//cbc:ID',namespaces=NS)[0],
cdr_file.find('.//cbc:ID',namespaces=NS).text,
expected_xml.find('.//cbc:ResponseTime',namespaces=NS)[0],
cdr_file.find('.//cbc:ResponseTime',namespaces=NS).text,
expected_xml.find('.//cac:DocumentResponse/cac:Response/cbc:ReferenceID',namespaces=NS)[0],
cdr_file.find('.//cac:DocumentResponse/cac:Response/cbc:ReferenceID',namespaces=NS).text,
expected_xml.find('.//cac:DocumentResponse/cac:Response/cbc:Description',namespaces=NS)[0],
cdr_file.find('.//cac:DocumentResponse/cac:Response/cbc:Description',namespaces=NS).text,
expected_xml.find('.//cbc:IssueDate', namespaces=NS)[0],
cdr_file.find('.//cbc:IssueDate', namespaces=NS).text,
expected_xml.find('.//cbc:ResponseDate', namespaces=NS)[0],
cdr_file.find('.//cbc:ResponseDate', namespaces=NS).text,
expected_xml.find('.//cac:DocumentReference/cbc:ID', namespaces=NS)[0],
cdr_file.find('.//cac:DocumentReference/cbc:ID', namespaces=NS).text,
]

old_xml_file = open('old_xml.xml', 'w')
old_xml_temp = etree.tostring(old_xml)
old_xml_file.write(old_xml_temp)
old_xml_file.close()

new_xml_file = open('new_xml.xml', 'w')
new_xml_temp = etree.tostring(new_xml)
new_xml_file.write(new_xml_temp)
new_xml_file.close()


# DIFF documents

# //ds:DigestValue
# //cbc:ID
# <!-- (/descendant-or-self::node()/cbc:ID)[1] -->
# //cbc:ResponseTime
# //cac:DocumentResponse/cac:Response/cbc:ReferenceID
# //cac:DocumentResponse/cac:Response/cbc:Description
# //cac:DocumentResponse/cac:DocumentReference/cbc:ID
# //cbc:IssueDate
# //cbc:ResponseDate
# //cac:DocumentReference/cbc:ID
