# Rainwater Retention Project

This project calculates the amount of rainwater retained after rainfall, given the heights of walls.

## Table of Contents

- [Description](#description)
- [Usage](#usage)
- [Installation](#installation)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Description

The project includes a Python script (`0-rain.py`) that defines a `rain` function. The function takes a list of non-negative integers representing wall heights and calculates the total amount of rainwater retained between the walls.

## Usage

To use the rainwater retention function, you can import it in your Python script or run the provided example script.

```python
from rain import rain

walls = [0, 1, 0, 2, 0, 3, 0, 4]
result = rain(walls)
print(result)

