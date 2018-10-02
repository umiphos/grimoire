### About this page:
The idea is to collect notes that will help us in the future in vauxoo about the tools we use everyday.
We should avoid ideas or tutorials about something that it's outside vauxoo.

## Running flake8, pep8, pylint with a config file
Why? because sometimes you need it, and it's faster than waiting for travis.

Let us remember that vauxoo has **amintainer-quality-tools** that(as it's name stablishes) is a collection of tools that help us to certify a certain degree of cohesion among all the code.
Inside this folder we find **travis** and inside there **cfg** wich has all the configurations standard for cheking lints and bad syntaxis.

**flake8**
flake8 . --config=/cfg/travis_run_flake8.cfg
pylint . --rcfile=/cfg/travis_run_flake8.cfg **not shure about this one**
pep8 . --config=/cfg/travis_run_flake8.cfg


**Running a new server without t2d**
Run first the addons
/home/odoo/odoo-11.0/odoo-bin -d bundle --addons-path=/home/odoo/build/Vauxoo/odoo-peru,/home/odoo,/home/odoo/odoo-11.0/addons,/home/odoo/odoo-11.0/odoo/addons,/home/odoo/enterprise/

Then init the modules that you need:q

**Errors while installing travis2docker**
https://github.com/pypa/pip/issues/5221#issuecomment-382069604
The error after upgrading pip, after searching in the web I found this solution to work in the environment at the time.
hash -r pip # or hash -d pip
python -m pip uninstall pip  # this might need sudo
sudo apt install --reinstall python-pip
pip install --upgrade pip
