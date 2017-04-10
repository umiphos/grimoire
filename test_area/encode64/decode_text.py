import base64

with open("refund.png", 'rb') as image_file:
    encode_string = base64.b64encode(image_file.read())

fh = open("encoded.txt", "wb")
fh.write(encode_string)
fh.close()

import ipdb;ipdb.set_trace()

with open("encoded.txt", 'rb') as text_file:
    decode_string = base64.b64decode(text_file.read())


fh = open("decoded_refund.png", "wb")
fh.write(decode_string)
fh.close()
