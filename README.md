# Multithreaded Elevator System

## Table of Contents
- [Introduction](#introduction)
- [Overview](#overview)
- [Features](#features)
- [Files](#files)
- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
- [Authors](#authors)

## Introduction

A multithreaded elevator system implemented in Python that simulates real-world elevator operations.
This Multithreaded Elevator System simulator is a Python project designed to simulate the operations of an elevator system in a multi-story building. The simulation handles elevator movement, user requests, and direction of travel.

## Overview

This system allows you to simulate elevator operations using Python's threading and queue modules. It has a modular structure that allows for customizing the number of elevators, the speed of the elevators, and the range of floors they can serve. 

## Features

- Multithreading: The system utilizes Python's threading module to simulate the concurrent operation of multiple elevators.
- PriorityQueue: Each elevator maintains a priority queue of floor requests to optimize its operation.
- User Interaction: Users can input their current floor and desired direction, and the system will assign the best elevator to serve them.

## Files

The project contains the following files:

- `main.py`: The entry point of the system. Here we initialize the elevator system and start a thread for user input.
- `elevator_system.py`: Contains the `ElevatorSystem` class which manages all elevators and handles floor requests.
- `elevator.py`: Contains the `Elevator` class which simulates an individual elevator's operation. 

## Installation

1. Clone the repo
   ```sh
   git clone https://github.com/nkamali/elevator

## Usage

1. Run `main.py` to start the system.

```bash
python main.py
```

2. When prompted, input your current floor number and the direction you want to go in.

```bash
What floor are you on?
10
Going up or down?
up
```

3. To exit the system, input `quit` when asked for the floor number.

When rendered in a markdown viewer or editor, the code blocks will be displayed with syntax highlighting, and the commands and prompts will be formatted as monospaced text.

## Development

This project uses Python 3.8+.

To contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## Authors

- **Navid Kamali** - *Initial work* - [navidk](https://github.com/navidk)
