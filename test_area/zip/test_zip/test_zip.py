import base64
import os
import zipfile

# Open the ZIP file with mode read "r", write "w" or append "a".
zip = zipfile.ZipFile('Python.zip', 'a')
zip.write('tex1.txt')
zip.write('tex2.txt')
zip.write('tex3.txt')
import ipdb;ipdb.set_trace()
zip.close()
