# regex_email_address
the regex could be used to extract most email addresses, and also some avoid-spammers email address

those email addresses include: <\br>
abc [at] ahdg [dot] edu <\br>
abc [[AT]] ansg [{DOT}] edu <\br>
...<\br>

input</br>
webpages include email addresses or not, email addresses are look like things above </br>

output</br>
abc@ahdg.edu
None(if not email address found)
