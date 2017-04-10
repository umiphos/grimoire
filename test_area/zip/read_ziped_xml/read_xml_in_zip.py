import zipfile
import base64

# from lxml import etree
import lxml
from lxml.objectify import fromstring

"""Links and comments
https://pymotw.com/2/zipfile/


"""

this = open('file.zip')
decode_this = base64.b64decode(this.read())

zr = zipfile.ZipFile('file.zip','r')
# decode_zr = base64.b64decode(zr.read())
name_cableao = zr.namelist()
readed = zr.read(name_cableao[1])
doc = lxml.objectify.XML(readed)
rawxDdX = raw_input("write the cbc to return")
# doc.xpath("//cbc:ResponseCode",
#           namespaces={'cac':'urn.oasis:names:specification:
#                       ubl:schema:xsd:CommonAggregateComponents-2',
#                       'cbc':'urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2'
#                       })
print doc.xpath("//cbc:"+rawxDdX,
          namespaces={'cac':'urn.oasis:names:specification: ubl:schema:xsd:CommonAggregateComponents-2',
                      'cbc':'urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2'
                      })
import ipdb;ipdb.set_trace()
