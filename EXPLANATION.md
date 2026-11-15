# Code Explanation – Server Inventory Tool

## 1. Three constructs in the code

### Condition: if/elif/else in `run_menu` (menu.py)
The condition decides what happens for each menu choice that matches the number entered by the user, including printing a message when the user doesn't enter a valid number. It checks conditions until one matches with the user's input and stops when a match is found and runs the code that comes after `:` under that condition, the code after `:` is indented so it only runs when that condition is met otherwise it's skipped. Since choice comes from input() as a string it's compared with numbers in quotes instead of integers.

### While loop in `add_server` (menu.py)
As long as the user keeps typing an environment that is not dev, test or prod, the loop keeps asking until the input is valid. The loop checks the user's input against a list of strings, if the input matches none of them, the code inside it prints a message telling the user to enter one of the valid environments and asks for input again to take a new value. The loop prevents the program from going forward with wrong values so they are never saved.

### Function with parameters and return: `find_server(servers, name)` (menu.py)
It takes all servers and a name, returns the server with a matching name or None if none of the servers have a matching name. (servers, name) are parameters, the function takes the list of servers and a name the user types to look through the list of servers for a server with a matching name. As soon as a matching name is found, `return` gives back that server to where the function was called and the function stops. This function is important to avoid having to rewrite the same code in different places. It is used in `add_server`, `remove_server` and `check_one_server` in menu.py, and for `--check` in main.py.

## 2. List of dictionaries

### Why a list of dictionaries
In a dictionary each value has a name (a key), which makes the code easier to read. For example, `check_server` (checks.py) uses `server["address"]` and `server["status"]`. Since there are many servers, having them in a list makes it possible to loop through them with `for server in servers:`, which is done in for example `show_servers` and `find_server` (menu.py). A list also makes it easy to add or remove a server with `servers.append()` in `add_server` and `servers.remove()` in `remove_server` (menu.py). Also, a list of dictionaries has the same structure as a JSON file, so `json.load` and `json.dump` in `load_servers` and `save_servers` (storage.py) can read and save it directly.

### Data types
All values in a server are strings (`str`). For example, the address `"127.0.0.1"` is a string, because it is only used as text in the ping command. `last_checked` is also a string: in `check_server` (checks.py) the time is turned into text with `strftime`, and a new server added in `add_server` gets an empty string `""`.

## 3. JSON and CSV

JSON is for the program. It keeps the same structure as the Python data,
the program reads directly from it and can write to it (`load_servers` and
`save_servers` in storage.py). It is also readable in a text editor.

CSV is for people. It can be opened directly in Excel as a spreadsheet
(`export_csv` in storage.py). Each report is a new report and the old ones
are not overwritten.

## 4. Modules and functions

The program is divided into four modules (files), and each one has its own job.

- `main.py` is the starting point. In `main()` it reads the command-line
  arguments with argparse and decides if the program should run a single
  command or show the menu.
- `menu.py` has the text menu. `run_menu` shows the menu and calls a function
  for each choice, for example `add_server`, `remove_server` and
  `check_one_server`. It also has `show_servers` and `find_server`.
- `storage.py` handles the files. `load_servers` and `save_servers` read and
  write the JSON file, `get_data_file` reads the environment variable and
  `export_csv` creates the CSV report.
- `checks.py` checks the servers. `ping_server` runs the ping command,
  `check_server` sets the status and time for one server, and
  `check_all_servers` does it for all servers.

Since each file only has one job, it is easier to find and fix things.

## 5. Standard library modules

- `json` is used to read and save the servers in `load_servers` and `save_servers` (storage.py).
- `csv` is used to write the CSV report with `DictWriter` in `export_csv` (storage.py).
- `os` is used to read the environment variable `INVENTORY_DATAFILE` in `get_data_file` (storage.py).
- `pathlib` (`Path`) is used to check if the data file exists in `load_servers` and to create the `reports/` folder in `export_csv` (storage.py).
- `datetime` is used to get the current time for `last_checked` in `check_server` (checks.py) and for the CSV file name in `export_csv` (storage.py).
- `subprocess` is used to run the `ping` command in `ping_server` (checks.py).
- `argparse` is used to read command-line arguments like `--list` and `--check` in `main()` (main.py).
- `sys` is used to exit with an exit code, `sys.exit(0)` or `sys.exit(1)`, in `main()` (main.py).

## 6. Good practice

### 1. The program does not crash if the data file is missing

In `load_servers` (storage.py), the program checks `file_path.exists()` before
opening the file. If the file does not exist, it returns an empty list instead
of crashing, which makes it possible for the program to still start the first
time it is used or when `INVENTORY_DATAFILE` points to a new file.

### 2. Allowed environments are defined in one place

I created a list called `valid_environments` with the allowed environments in
menu.py. The while loop in `add_server` checks the user's input against this
list, so the list only has to be edited in one place.

### 3. Asking before removing a prod server

In `remove_server` (menu.py), the program asks the user to confirm with yes/no
if the server is in the prod environment, and only removes it if the answer is
`yes`. This is good because prod servers are important, and it stops the user
from removing one by mistake.

## 7. Sources and tools

I used the PowerPoint slides as the main guide and Claude to explain concepts I did not understand and help with the read me structure.
I tried to follow the slides in writing my code.
I practised with futurecoder.io and w3schools.com to have a further understanding of the code.

I wrote and tested the code myself.
I wrote it in PyCharm and ran and tested it in Ubuntu (WSL).

