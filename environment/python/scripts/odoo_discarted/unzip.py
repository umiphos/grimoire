def unzip(self, file_name=False):
    """ basically this module will search for any attachment given a name
        it should be or not be the full name, also, we expect to be a partial name, not a fullname
        at the end it will return any unziped XML inside the ZIP

        Receive a name
        search any atachment similar to it given name
        Extract any file similar to it given name
        return a list of attachments, {name:file.xml}
    """
    encoded_files = self.env['ir.attachment'].search([
        ('res_model', '=', 'account.invoice'),
        ('res_id', '=', self.invoice.id),
        ('name', 'ilike', '%s' % (file_name))])
    document = {}
    file_name = splitext(self.invoice.l10n_pe_edi_ublpe_name)[0]
    for files in encoded_files:
        with tempfile.TemporaryFile() as zip_file:
            zip_decoded = base64.b64decode(files.datas)
            zip_file.write(zip_decoded)
            temp_zip = zipfile.ZipFile(zip_file, 'r')
            zip_name = filter(lambda x: file_name in x,
                            temp_zip.namelist())[0]
            readed_file = temp_zip.read(zip_name)
            document.update({files.name: objectify.XML(readed_file)})
    return document
