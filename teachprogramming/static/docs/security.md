Security Projects
=================

* [gchq/CyberChef](https://github.com/gchq/CyberChef)
  * > The Cyber Swiss Army Knife - a web app for encryption, encoding, compression and data analysis 
  * Amazing! RSA! Data Decoding - I need to explore this more
  * https://github.com/mattnotmax/cyberchef-recipes
  * https://www.gaijin.at/en/infos/cyberchef-recipes

* [temp-mail.org](https://temp-mail.org/)
    * Web readonly view of received mail
* [shodan.io](https://www.shodan.io/)
  * `port:22`
  * `os:xp`
  * `exploit:dopler`
* dirbuster 
    * 
127.0.0.1
nmap -p 9000 -sC -sV -oA nmap/results 

burpsuit? man in middle

https://github.com/dzflack/ctf-challenges

https://github.com/daviddias/node-dirbuster/tree/master/lists

https://owasp.org/
https://owasp.org/projects/ Range of lab projects
https://cheatsheetseries.owasp.org/



* https://security.stackexchange.com/questions/36358/decrypt-from-cipher-text-encrypted-using-rsa
  * Use `openssl` to encode and decode rsa
  * `$ openssl enc -in ciphertext -out binarytext -d -a`
  * `$ openssl rsautl -decrypt -in binarytext -out plaintext -inkey private.pem`


