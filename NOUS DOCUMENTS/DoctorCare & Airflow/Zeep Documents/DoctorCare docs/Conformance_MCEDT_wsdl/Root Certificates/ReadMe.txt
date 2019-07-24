go-pki_cacert.arm: 

The CA signing certificate for the (OPS) GO-PKI Certificate Authority.  It signs the certificate used by the service for encryption and verification.  The public key for the ministry, included in the certificate we return in a response, is signed by the GO-PKI CA.



Entrust L1C Chain Certificate.arm:  

The Entrust certificates constitute the certificate signer chain that authenticates the service’s SSL certificate. The L1C one is an intermediate signer (the immediate signer of the EBS SSL certificate).



Entrust.netCertificationAuthority(2048).arm: 

The Entrust root CA signing certificate.



To install the certificates you can import the arm files in your keystores or following the guidelines below.

Copy the arm files and give them a .cer extension, double click on the files. Click on the install button on the bottom of the popup.
 
Entrust issues the SSL cert, and MBS-CA1 (GO-PKI) issues the signing certificate, both issuers should be installed as Trusted Root Certification Authorities. 
 


