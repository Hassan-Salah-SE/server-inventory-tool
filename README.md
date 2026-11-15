# Server Inventory Tool

A command-line program written in Python to keep track of servers and check if they respond to ping. The servers are saved in a JSON file and a report can be exported as a CSV file.

The program can be used in two ways: 
An interactive menu or command-line arguments.

## Features

- Show all servers in a table
- Show servers in a specific environment (dev, test or prod)
- Add a new server
- Remove a server
- Check if one server responds to ping
- Check if all servers respond to ping
- Export all servers to a CSV report

## Requirements

- Linux (tested on Ubuntu in WSL)
- Python 3 (tested with Python 3.14)
- The `ping` command
- No extra Python packages are needed, the program only uses Python's standard library.

## Installation

1. Clone the repository
   ```bash
   git clone git clone https://github.com/Hassan-Salah-SE/server-inventory-tool.git
   ```
2. Go into the project folder
   ```bash
   cd server-inventory-tool
   ```

**Note:** The program must always be run from inside the project folder.

## Usage

### Menu mode

Start the program to open menu:

```bash
python3 main.py
```

```
====== Server Inventory Tool ======
1.Show all servers
2.Show servers in environment
3.Add a server
4.Remove a server
5.Check a server
6.Check all servers
7.Export a report as CSV
8.Quit
Enter choice:
```

| Option | What it does |
|---|---|
| 1 | Shows all servers in a table |
| 2 | Asks for an environment (dev, test or prod) and shows only those servers |
| 3 | Asks for name, address, environment and role, and adds the server |
| 4 | Removes a server by name. Asks "yes/no" first if it is a prod server |
| 5 | Pings one server and saves its status and the time |
| 6 | Pings all servers, saves the results and shows the table |
| 7 | Saves all servers to a CSV file in `reports/` |
| 8 | Quits the program |

If you type an invalid choice, the program shows a message and the menu again.
If you type the name of a server that does not exist, the program tells you.

### Command-line mode

Give the program an argument to do one tasks and then exit without the menu.

| Command | What it does |
|---|---|
| `python3 main.py --help` | Shows all available options |
| `python3 main.py --list` | Shows all servers |
| `python3 main.py --list --environment prod` | Shows only servers in one environment (dev, test or prod) |
| `python3 main.py --check dev01` | Checks one server by name |
| `python3 main.py --check-all` | Checks all servers and shows the table |
| `python3 main.py --export` | Exports all servers to a CSV file in `reports/` |

### Exit codes

When the program finishes, it returns a number called an **exit code**.
It tells if everything went well. It does not print on the screen,
but you can show it by typing `echo $?` right after the program has finished.

- `0` means everything is OK
- `1` means something is wrong
- `2` means the command was typed wrong

**For `--check`:**

- `0` if the server is up
- `1` if the server is down, or if no server with that name exists

**For `--check-all`:**

- `0` if all servers are up
- `1` if at least one server is down

## Choosing the data file (environment variable)

The servers are saved in the file `servers.json`.
If you want the program to use a different file, you can tell it with
the environment variable `INVENTORY_DATAFILE`.

**Example:** use the file `test.json` instead of `servers.json`:

```bash
INVENTORY_DATAFILE=test.json python3 main.py
```

The program reads it when it starts. You do not need to change any code. However, this only works for that one command. The next time you run
`python3 main.py`, the program uses `servers.json` again.

If you do not set `INVENTORY_DATAFILE`, the program uses `servers.json`.

If the file does not exist, the program does not crash, it just starts with an empty list of servers.

## Project structure

```
server-inventory-tool/
├── main.py          starting point, reads command-line arguments
├── menu.py          the text menu and its functions
├── storage.py       loads and saves JSON, exports CSV
├── checks.py        checks if servers respond to ping
├── servers.json     the saved servers
├── .gitignore
├── README.md
├── EXPLANATION.md   answers to the written questions (REDOGORELSE)
└── reports/         CSV reports (created automatically)
```

Both the menu and the command-line mode use the same functions from
`storage.py` and `checks.py`, so the logic is only written once.

## Notes

- Wrote the whole program in English so changed the file names accordingly:
`meny.py` → `menu.py`, `lagring.py` → `storage.py`,
  `kontroller.py` → `checks.py`, `servrar.json` → `servers.json`,
  `REDOGORELSE.md` → `EXPLANATION.md`
  and `INVENTORY_DATAFIL` → `INVENTORY_DATAFILE`.