# Pretty-recon-auto
Pretty-recon-auto is an unofficial cli client for [PrettyRecon](https://prettyrecon.com/).

This tool is currently automate CustomSubScan feature only of PrettyRecon. I will update it in Future. Inspired from https://github.com/SiddharthBharadwaj/prettyrecon-cli

As PrettyRecon currently does not have any api feature available, prettyrecon Auto uses email and password for authentication. None of these are saved or shared anywhere other than your computer where it is running.

## Setup

1. Clone the repository

```bash
$ git clone https://github.com/0xAT7/Pretty-recon-auto.git
```

2. Install the dependencies

```bash
$ cd Pretty-recon-auto
$ pip3 install -r requirements.txt
```
3. Update config.py with valid credentials

4. Run Pretty-recon-auto (see [Usage](#usage) below for more detail)

```bash
$ python3 PrettyRecon.py -l google-subs.txt -sn Google
```

## Usage

```bash
$ python3 PrettyRecon.py
[*] Usage: python3 prettyRecon.py -l google.txt -sn Google
                                              
```

Tested on Python 3.8.10. Feel free to [open an issue](https://github.com/0xAT7/Pretty-recon-auto/issues) if you have bug reports,feature requests questions.
Contributions are most welcome!
