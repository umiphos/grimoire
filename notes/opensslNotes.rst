Auto generated cert brought from comodossl

create a csr
openssl req -new -newkey rsa:2048 -nodes -keyout server.key -out server.csr

read the csr
openssl req -in server.csr  -noout -text

create pfx using the key we generated
openssl pkcs12 -export -out certificate.pfx -inkey server.key -in new_just_brought_certicicate.crt

crt to cer
openssl x509 -inform PEM -in new_just_brought_certificate.crt -out new_just_converted_same_certificate_pe.cer

read cer
openssl x509 -in file.cer -noout -text

p12 to cer
openssl pkcs12 -in file.p12 -clcerts -out file.cer


Certificate brought from camara de comercio

p12 to cer
openssl pkcs12 -in file.p12 -clcerts -out file.cer

cer to pfx
openssl pkcs12 -export -out kukyflor.pfx -in kuky_2019.cer

read pfx
openssl pkcs12 -in file.pfx -nodes

pem to pfx without key
openssl pkcs12 -export -out DIGIFLOW.pfx -in DIGIFLOW.pem

pem check expiration date
openssl x509 -enddate -noout -in file.pem

pfx check expiration date
openssl pkcs12 -in DIGIFLOW.pfx -nokeys | openssl x509 -noout -enddate
