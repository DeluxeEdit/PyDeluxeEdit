pyinstaller.exe -n DeluxeEdit .\start.py --specpath . -i deluxeedit.ico --clean
 
python .\gen_msix_xml.py --app-version 1.0.0.0 --manifest .\manifest.json --logo-dir .\logos .\dist\demo\0
--cert-subject
New-SelfSignedCertificate `
     -Type Custom `
     -Subject "CN=Pierre Signing Cert, C=SE" `
     -KeyUsage DigitalSignature `
     -FriendlyName "Pierre Cert" `
     -CertStoreLocation "Cert:\LocalMachine\My" `

#Thumbprint                                Subject
# 92C6FFA8B964586B45B642528315870AEB22C03B  CN=Pierre Signing Cert, C=SE