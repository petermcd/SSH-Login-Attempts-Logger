# SSH Login Attempts Logger

A simple script used to log login attempts generated from the 
[SSH PAM Login Logger](https://github.com/PeterMcD/ssh-pam-login-logger) script.

The script writes to an AWS API, reading credential and URL details from config.py (currently not checked in).

```
# Unique URL for the AWS API.
URL:str = ""
# AWS API key.
API_Key = ""
# Path and filename for the database.
DatabasePath = '/var/log/login-attempts.db'
```

For python to have the ability to read the database /var/log requires write access for guest.
If you are uncomfortable giving such access on this folder the database will need to be removed.
Remember to update the pam module.