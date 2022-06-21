# Description
- Description: Breaking Bad Quote Generator
- Data Source: API Endpoint https://wagon-breaking-bad-quotes.herokuapp.com/v1/quotes

# Web
To Access the Breaking Bad Quote Generator Web, Please access
https://bbquote-generator.herokuapp.com/

# Install The Packages 
```
pip install git+ssh://git@github.com/liviaellen/Breaking-Bad-Quote-Generator/
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

Check for bbquote883 in gitlab.com/{group}.
If your project is not set please add it:

- Create a new project on `gitlab.com/{group}/bbquote883`
- Then populate it:

```bash
##   e.g. if group is "{group}" and project_name is "bbquote883"
git remote add origin git@github.com:{group}/bbquote883.git
git push -u origin master
git push -u origin --tags
```

Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
bbquote-run
```

# Install

Go to `https://github.com/liviaellen/Breaking-Bad-Quote-Generator` to see the project, manage issues,
setup you ssh public key, ...

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
