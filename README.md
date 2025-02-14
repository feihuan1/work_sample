# Multi-Value Dictionary

## Overview

This is a command-line application that allows users to work with a multi-value dictionary.

It follows the Model-View-Controller (MVC) design pattern, separating concerns for better maintainability.

## Features

* Add keys and members to a dictionary
* Retrieve keys, members, and all dictionary items
* Check if a key or member exists
* Remove specific members or entire keys
* Clear all dictionary data
* Save and load data from `data.txt`

## Technologies Used

* Python (Core Logic)
* `unittest` (Testing Framework)
* MVC Architecture


### Prerequisites

Python 3.x installed on your system

## How to Run the Application

```bash
python app.py
```

### Run Tests
```bash
python -m unittest tests/test_controller.py
python -m unittest tests/test_model.py
python -m unittest tests/test_view.py
```

## How to Use

Once the app is running, you can use the following commands:

| Command               | Description                                                     |
|-----------------------|-----------------------------------------------------------------|
| `ADD key value`       | Adds a value to a key. Creates the key if it doesn't exist.     |
| `MEMBERS key`         | Lists all members of a key.                                     |
| `REMOVE key value`    | Removes a specific value from a key.                            |
| `REMOVEALL key`       | Removes a key and all its members.                              |
| `KEYS`                | Displays all keys in the dictionary.                            |
| `ALLMEMBERS`          | Lists all members across all keys.                              |
| `ITEMS`               | Lists all key-value pairs.                                      |
| `KEYEXISTS key`       | Checks if a key exists.                                         |
| `MEMBEREXISTS key value` | Checks if a value exists for a key.                          |
| `CLEAR`               | Removes all keys and members.                                   |
| `EXIT`                | Closes the application.                                         | 


## Example Usage

```bash
$ ADD fruits apple
Added

$ ADD fruits banana
Added

$ MEMBERS fruits
1) apple
2) banana

$ REMOVE fruits apple
Removed

$ ITEMS
1) fruits: banana
```

## Additional Notes

* The application saves data in `data.txt` for persistence.
* If `data.txt` is missing, it will be automatically created.
* Error handling is implemented to prevent errors when using incorrect commands.