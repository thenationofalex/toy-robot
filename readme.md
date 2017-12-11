# 🤖 Toy Robot Simulator

### Version 1.0.0

![Python 3.5](https://img.shields.io/badge/Python%20-3.5-3776ab.svg)
![PEP 8](https://img.shields.io/badge/Style-PEP8-yellow.svg)

### Built and Requires

- [Python 3.5](https://www.python.org)
- [Nose](http://nose.readthedocs.io/en/latest/)

## Setup

- _IF using virtualenv be sure to activate it before starting the application e.g: `source env/bin/activate`_
- Install Python Dependencies via PIP `pip3 install -r requirements.txt`

## Instructions and Usage

To start the application run `python3 robot.py`

The robot will response to the commands as outlined in `problem.md`

## Tests

Test can be run using [Nose](http://nose.readthedocs.io/en/latest/)

E.g: `nosetests tests/test-move.py`

## Structure

- `robot.py` Main application
    - `modules` Application dependencies
        - `inputcontroller.py` Handle input from user
        - `move.py` Control Robots movement
        - `orientate.py` Orientate Robot
        - `validateplace.py` Validate Robots position on the board
    - `tests` Unit tests
        - `test-move.py`
        - `test-orientate.py`
        - `test-validateplace.py`


