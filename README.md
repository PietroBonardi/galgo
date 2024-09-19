# GALGO

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) 
![Python 3.12](https://img.shields.io/badge/python-3.12-blue)

### Overview

GALGO is an implementation of the genetic algorithm, designed for flexibility and ease of use.

### Experiments

To demonstrate the functionality of Galgo, an `experiments` folder has been included. This folder contains a vanilla example that uses random strings as individuals. The example provides a clear guide on how to wrap the `Population` and `Fitness` classes, which are the core components you need to configure before running the genetic algorithm.

### Key Components

To use the genetic algorithm, you need to define the following components by wrapping these classes:

- **Population Class**: Manages the collection of individuals in the genetic algorithm.
- **Fitness Class**: Evaluates the fitness of individuals based on a specific criterion.


### WIP

- Upgrade early stopping
- Enhance offspring evolution
- Add visualization tool

### Project Structure

    .
    ├──── examples/
    │       ├── main.ipynb
    │       └── string_vanilla.py
    ├── src/
    │   ├── genealgo/
    │   │   └── genetic_algorithm.py
    │   └── components/
    │   │   ├── crossover.py
    │   │   ├── fitness.py
    │   │   ├── mutator.py
    │   │   ├── parents.py
    │   │   └── population.py
    │   └── setup.py
    ├── Makefile
    └── README.md