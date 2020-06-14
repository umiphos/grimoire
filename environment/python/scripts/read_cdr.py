from lxml import etree
from zipfile import ZipFile
from io import BytesIO
import base64

datas = "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"
response = ZipFile(BytesIO(base64.b64decode(datas)))
content_name = response.namelist()[0]
content = response.read(content_name)
element = etree.fromstring(content)
print(etree.tostring(element, pretty_print=True).decode('utf-8'))
