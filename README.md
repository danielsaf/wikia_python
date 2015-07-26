# Holmium Demo

Refer to the [article here](http://lifeinvistaprint.com/techblog/unit-testing-holmium-page-objects/).

## Setup

* Install Firefox
* Install `Python3` and `pip`
    * **On OSX**

            sudo easy_install pip

    * **On Windows**
      * Download and install [python 3.0](https://www.python.org/download/)
      * Install `pip`
          * Download and save [get-pip.py](https://raw.github.com/pypa/pip/master/contrib/get-pip.py) as `get-pip.py`
          * `python get-pip.py`
          * Add `C:\Python34\Scripts` to PATH

* Using `pip` install Selenium, nostests, Holmium, Jinja2:

        pip install selenium nose holmium.core
* Clone this repo and navigate to that folder

## Execution

    nosetests login_test.py --with-holmium --holmium-browser=firefox --holmium-environment=http://qm-homework.wikia.com


