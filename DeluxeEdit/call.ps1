pyinstaller.exe -n PyDeluxeEdit .\main.py --specpath . -i deluxeedit.ico --clean
 
New-SelfSignedCertificate `
     -Type Custom `
     -Subject "CN=Pierre Signing Cert, C=SE" `
     -KeyUsage DigitalSignature `
     -FriendlyName "Pierre Cert" `
     -CertStoreLocation "Cert:\LocalMachine\My" `

#Thumbprint                                Subject
# 92C6FFA8B964586B45B642528315870AEB22C03B  CN=Pierre Signing Cert, C=SE