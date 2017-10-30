### To list all the errors inside errno

Useful when we try to make reference to certain errors
=====================================================

```python

import os
import errno

print {i:os.strerror(i) for i in sorted(errno.errorcode)}

```
import pysimplesoap
import errno
import logging

this = pysimplesoap
this.client.logging.basicConfig(level=logging.INFO)
pysimplesoap.helpers.logging.disable( errno.ECONNREFUSED)
pysimplesoap.helpers.logging.exception(errno.ECONNREFUSED)
pysimplesoap.helpers.logging.disable( errno.ECONNREFUSED )
this.client.SoapClient(wsdl='https://e-beta.sunat.gob.pe/ol-ti-itcpfegem-beta/billService?wsdl')
_logger = logging.getLogger(__name__)

====================
 with tempfile.TemporaryFile() as zip_file:
            zip_decoded = base64.b64decode(encoded_file)
            zip_file.write(zip_decoded)
            temp_zip = zipfile.ZipFile(zip_file, 'r')
            file_name = 'R-%s.xml' % splitext(self.l10n_pe_edi_ublpe_name)[0]
            readed_file = temp_zip.read(file_name)
            document = lxml.objectify.XML(readed_file)

            response_code_property = '//cbc:ResponseCode'
            description_code_property = '//cbc:Description'

            namespaces = {
                'cbc': 'urn:oasis:names:specification:ubl:schema:xsd:'
                'CommonBasicComponents-2'
            }
            try:
                response_code = document.xpath(
                    response_code_property, namespaces=namespaces)[0]

                response_description = document.xpath(
                    description_code_property, namespaces=namespaces)[0]
                self.l10n_pe_edi_response_code = response_code
                self.l10n_pe_edi_response_descr = response_description
            except IndexError as e:
                _logger.error('There was an error of %s', e)
                self.message_post(subject=_("Bad XML from the SUNAT"),
                                  body=_('There is no items inside de xml: '
                                         '%s<br>') % (e),
                                  subtype='account.mt_invoice_validated')


New ways to use an if statement
===============================
# Case II
-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
if self.type in ('in_refund', 'out_refund'):
    sign = -1
else:
    sign = 1
>>>>>>>>>>>>>>>>>>>>>>>>>Exchange<<<<<<<<<<<<<<<<<<<<<<<<<
sign = 1 if self.type in ('in_refund', 'out_refund') else -1

>>>>>>>>>>>>>>>>>>>>>>>>Explanation<<<<<<<<<<<<<<<<<<<
If at the end is a simple IF statement we can make it simple with the previous line, so we read it like:
sign equals to 1 if the type is within this tuple, else, sign will be -1


# Case II
-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
if post.get('referenceCode'):
    reference = post.get('referenceCode')
else:
    reference = post['reference_sale']
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Exchange<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
reference = post.get('referenceCode', post['reference_sale'])
>>>>>>>>>>>>>>>>>>>>>>>>Explanation<<<<<<<<<<<<<<<<<<<
Basically



