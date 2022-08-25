# FizzBuzz
*My python implementation of FizzBuzz, a childhood game turned interview question*

[Inspiration]()

### Table of contents
[Back to top](#fizzbuzz)
[Here](#table-of-contents)
[Installation](#installation)
 - [Windows(Command Prompt)](#windowscommand-prompt)
 - [Windows(Powershell)](#windowspowershell)
 - [*nix(MacOS X/Linux/Unix)](#nixmacos-xlinuxunix)

[Usage](#usage)

## Installation

Requirements:
 - [Python >= 3.7](https://python.org/downloads/)
 - Poetry >= 1.2[^1]
 - [Git](https://git-scm.com)


To use the program the intended way, you must first install it by running one of the following code snippets, depending on your os and terminal.

#### Windows(Command Prompt):
```bat
git clone https://github.com/tinkering-towsperson/fizzbuzz
cd fizzbuzz
poetry config virtualenvs.create false --local
py -m venv .venv
call .\.venv\Scripts\activate.bat
poetry env use .\.venv\Scripts\python.exe
poetry install
```

#### Windows(Powershell):
```ps1
git clone https://github.com/tinkering-towsperson/fizzbuzz
cd fizzbuzz
poetry config virtualenvs.create false --local
py -m venv .venv
call .\.venv\Scripts\Activate.ps1
poetry env use .\.venv\Scripts\python.exe
poetry install
```

#### *nix(MacOS X/Linux/Unix):
```bash
git clone https://github.com/tinkering-towsperson/fizzbuzz
cd fizzbuzz
poetry config virtualenvs.create false --local
source ./.venv/Scripts/activate
poetry env use ./.venv/Scripts/python
poetry install
```

## Usage
After installation, you can run it with default options by running the following:
```bash
poetry run fizzbuzz
```
And for the help message, just run:
```
poetry run fizzbuzz -h
```

[^1]: Installing poetry 1.2:

	*nix(MacOS X/Linux/Unix):
	```bash
	curl -sSL https://install.python-poetry.org | python3 - --preview
	```
	Windows(Powershell):
	```ps1
	(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py - --preview
	```
	For more information visit https://python-poetry.org/docs/master/#installing-with-the-official-installer
