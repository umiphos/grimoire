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

