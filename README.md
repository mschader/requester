# Requester

_requester_ is a small helper script to create [Python Requests](https://requests.readthedocs.io) templates to build your POC on.
The script wants to achieve two basic aspects:

1. Never have to lose time looking up the documentation for simple POC templates
2. Never have to write the script from scratch again and again and again, ....

## Installation

```bash
git clone https://github.com/mschader/requester.git
cd requester
python setup.py sdist
pip3 install dist/* --user
```

## Usage

```python
requester --help
Usage: requester.py [OPTIONS]

Options:
  -u, --url TEXT     Web Request URL
  -o, --output TEXT  Specify path where the generated shall be stored (default
                     ./exploit.py)

  -c, --cookie TEXT  Add cookie in the format cookie=cookievalue, repeat with
                     --cookie for multiple cookies

  --proxy TEXT       Specify if proxy is present
  --noverify         If set, any SSL certificates will be trusted
  --filter TEXT      Specify filter to look for inside response
  --wordlist TEXT    Specify a wordlist for bruteforce attacks
  --charlist         Specify if a dictionary of printable characters shall be
                     set up

  --verbose          If verbosity is set to True, the script will add output
                     for the response

  --help             Show this message and exit.
  ```