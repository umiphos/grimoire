from zipfile import ZipFile
from StringIO import StringIO

inMemoryOutputFile = StringIO()

zipFile = ZipFile(inMemoryOutputFile, 'w')
zipFile.writestr('OEBPS/content.xhtml', 'hello world')
import ipdb;ipdb.set_trace()
zipFile.close()
inMemoryOutputFile.seek(0)
