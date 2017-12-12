# 🤖 Toy Robot Simulator

### Version 1.0.0

![Python 3.5](https://img.shields.io/badge/Python%20-3.5-3776ab.svg)
![PEP 8](https://img.shields.io/badge/Style-PEP8-yellow.svg)

### Built and Requires

- [Python 3.5](https://www.python.org)
- [Nose](http://nose.readthedocs.io/en/latest/)

## Setup

- _IF using virtualenv be sure to activate it before starting the application e.g: `source env/bin/activate`_
- Install the required Python Dependencies via PIP `pip3 install -r requirements.txt`

## Instructions and Usage

To start the application run `python3 robot.py`

The robot will response to the commands as outlined in `problem.md`

## Tests

Test can be run using [Nose](http://nose.readthedocs.io/en/latest/)

E.g: `nosetests tests/test-move.py`

## Structure

The entry point to the application is `robot.py`.
This loads the modules `validateplace.py` and `inputcontroller.py`.

We use `validateplace.py` to ensure that the first command is only **PLACE X,Y,F**.

After the first loop is successfully passed we let `inputcontroller.py` validate
all commands. If a command is valid it then passes the request on to the appropriate module
otherwise it returns a *Invalid command* message.

The robots position is stored as a [dict](https://docs.python.org/3.5/tutorial/datastructures.html#dictionaries)
in order to ensure we can read, write and update via a immutable key.

- `robot.py` Main application
    - `modules` Application dependencies
        - `inputcontroller.py` Handle and validates input from user
        - `move.py` Controls Robots movement around the board
        - `orientate.py` Orientate Robot along a compass
        - `validateplace.py` Validate and process the place command
    - `tests` Unit tests
        - `test-inputcontroller.py`
        - `test-move.py`
        - `test-orientate.py`
        - `test-validateplace.py`


