from zipfile import ZipFile
from lxml import etree
    @api.multi
    def create_zipfile(self, attachment_id, xml_signed):
        chars = string.ascii_uppercase + string.digits
        path = "/tmp/"
        zip_filename = ''.join(random.choice(chars) for _ in range(16))
        fullpath = path+zip_filename+".zip"
        zip_name = str(attachment_id.name)
        zip_file = ZipFile(fullpath, 'w')
        zip_file.writestr(zip_name, xml_signed)
        zip_file.writestr('dummy/', '')
        zip_file.close()

        with open(fullpath, "rb") as zip_data:
            _bytes = zip_data.read()
            encoded = base64.b64encode(_bytes)
        zip_name = os.path.splitext(xml_signed)[0]

        attachment_id.write({
            'datas': encoded,
            'mimetype': 'application/zip',
            'name': attachment_id.name.replace('xml', 'zip'),
            'datas_fname': attachment_id.name.replace('xml', 'zip'),
})



