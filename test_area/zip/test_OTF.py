from zipfile import ZipFile
from StringIO import StringIO
import time
inMemoryOutputFile = StringIO()

zipFile = ZipFile("inMemoryOutputFile", 'w')
raw_input("Before write")
zipFile.writestr('OEBPS/content.xhtml', 'hello world')
raw_input("After write")
zipFile.close()
raw_input("After close")

inMemoryOutputFile.seek(0)
print zipFile, inMemoryOutputFile
