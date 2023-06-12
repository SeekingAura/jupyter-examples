- [Requirements](#requirements)
  - [System requirements](#system-requirements)
  - [Modules](#modules)
  - [Env vars](#env-vars)
- [Run command](#run-command)
- [Run tests](#run-tests)


# Requirements

## System requirements
- Python 3.9 


## Modules
install requirements
```
pip install -r requirements.txt
```

## Env vars
**.env-base** is a base file for expected environment

- GITHUB_TOKEN: token of github account that will get user info
- FRESHDESK_TOKEN: api token of freshdesk account that the contact info will stored
- FRESHDESK_SUBDOMAIN: Subdomain where the freshdesk account is
- LOG_LEVEL: log level, default "INFO"


# Run command
To get command manual/description run
```bash
python main.py --help
```

To add contact info from github user account from Token run:
```bash
python main.py
```

# Run tests
```bash
python -m tests
```
