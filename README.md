# SSH Login Attempts Logger

A simple script used to log login attempts generated from the 
[SSH PAM Login Logger](https://github.com/PeterMcD/ssh-pam-login-logger) script.

The script writes to an AWS API, reading credential and URL details from config.py (currently not checked in).

```
# Unique URL for the AWS API.
URL = ""

# AWS API key.
API_Key = ""

# Path and filename for the database.
DatabasePath = "/var/log/login-attempts.db"

```

For python to have the ability to read the database /var/log requires write access for guest.
If you are uncomfortable giving such access on this folder the database will need to be moved.
Remember to update the pam module.

## Installation

```python
cd ~
git clone https://github.com/PeterMcD/SSH-Login-Attempts-Logger.git
cd SSH-Login-Attempts-Logger
nano config.py
```

Add the following contents for AWS. You will need to create a dynamoDB instance. lambda instance and lastly an API. A tutorial for this will come later.

```python
# Unique URL for the AWS API.
URL = ""

# AWS API key.
API_Key = ""

# Path and filename for the database.
DatabasePath = "/var/log/login-attempts.db"
```

run

```python
sudo crontab -e
```

and add the following to the  (remembering to change the path to match the user)

```python
*/5 * * * * python3 /home/pi/ssh-login-attempts-logger/src/LoginExtractor.py
```