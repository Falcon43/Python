import urllib.parse , ssl
from OpenSSL import crypto   # pip install pyopenssl


url = "https://www.google.co.in/"
spliturl = urllib.parse.urlsplit(url)
HOST = spliturl.hostname
if not spliturl.port == None:
    PORT = spliturl.port
else:
    PORT = 443
print("Hostname:  "+str(HOST))
print("Port:  "+str(PORT))

certificate = ssl.get_server_certificate((HOST,PORT))
print("\n\nPEM formatted key -  the base64 encoded x509 ASN.1 key.\n")
print(certificate)




print("\n\n\n Decoding it lets us read it:")
cert = crypto.load_certificate(crypto.FILETYPE_PEM,certificate)

print("\n\n\n The signer of the server's certificate:")
issuer = cert.get_issuer()
print(issuer.get_components())


print("\n\n\n The company's business information")
subject = cert.get_subject()
components = dict(subject.get_components())
print(components)