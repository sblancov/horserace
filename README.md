# HorseRace

## Motivation

Horserace is a for-fun-project inspired by a computing class exercise of school made in Basic.

This does not pretend to be something great, just practice what I have learnt and I am learning about programming, always in a fun way.

### The original HorseRace

I do not remember what was the requirements, but I remember multiple lines growing until one touching the finish line. I will start doing that.

## Contributing

* Take a look at makefile, there are useful commands.
* Install all dev dependencies.
* Configure .githooks

    git config core.hooksPath .githooks

## Installation

For now, [pipenv](https://docs.pipenv.org/) is preferred over [pip](https://pip.pypa.io/en/stable/) plus [virtualenv](https://virtualenv.pypa.io/en/stable/), so install pipenv and then, manage virtual environment and install dependencies with it.

### Dependencies

Currently, this application needs python 3.5 (executed over Linux).

All python dependencies are listed in the Pipfile.

### From Source Code

First of all, download the code from this repository. Then:

    python3 -m pip install .
