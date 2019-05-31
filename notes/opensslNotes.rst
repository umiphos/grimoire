create a csr
openssl req -new -newkey rsa:2048 -nodes -keyout server.key -out server.csr

read the csr
openssl req -in server.csr  -noout -text

create pfx using the key we generated
openssl pkcs12 -export -out certificate.pfx -inkey server.key -in new_just_brought_certicicate.crt

crt to cer
openssl x509 -inform PEM -in new_just_brought_certificate.crt -out new_just_converted_same_certificate_pe.cer
