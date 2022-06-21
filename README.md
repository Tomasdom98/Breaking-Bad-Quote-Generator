# Description
- Description: Breaking Bad Quote Generator
- Data Source: API Endpoint https://wagon-breaking-bad-quotes.herokuapp.com/v1/quotes

# Web
To Access the Breaking Bad Quote Generator Web, Please access
https://bbquote-generator.herokuapp.com/

# Install The Packages 
```
pip install git+https://github.com/liviaellen/Breaking-Bad-Quote-Generator.git
```

# Run ```bbquote-run``` on terminal to generate Breaking Bad Quote
```bbquote-run```


--------------------

# Startup the project

The initial setup.

Create virtualenv and install the project:
```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
    pip install pip -U; pip install -r requirements.txt
```

Unittest test:
```bash
make clean install test
```

```

# Install

Go to `https://github.com/liviaellen/Breaking-Bad-Quote-Generator` to see the project.

Create a python3 virtualenv and activate it:

```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:

```bash
git clone git@github.com:liviaellen/Breaking-Bad-Quote-Generator.git
cd Breaking-Bad-Quote-Generator
pip install -r requirements.txt
make clean install test                # install and test
```
Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
bbquote-run
```
