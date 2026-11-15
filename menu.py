from storage import save_servers, export_csv
from checks import check_server, check_all_servers

valid_environments = ["dev", "test", "prod"]


def show_servers(servers):
    if len(servers) == 0:
        print("No servers found")
        return

    print(f"{'Name':<15} {'Address':<15} {'Environment':<15}"
          f"{'Role':<20} {'Status':<15} {'Last checked'}")
    print('-' * 100)

    for server in servers:
        print(f"{server['name']:<15} {server['address']:<15} {server['environment']:<15}"
              f"{server['role']:<20} {server['status']:<15} {server['last_checked']}")


def match_environment(servers, environment):
    matching = []
    for server in servers:
        if server["environment"] == environment:
            matching.append(server)
    return matching


# return the server with given name or None if it does not exist
def find_server(servers, name):
    for server in servers:
        if server["name"] == name:
            return server
    return None


def add_server(servers, data_file):
    name = input("Name: ")
    if find_server(servers, name) is not None:
        print("Server already exists")
        return
    address = input("Address: ")

    environment = input("Environment: ")
    # keep asking until user enters valid environment
    while environment not in valid_environments:
        print("Invalid environment. Please choose dev, test or prod")
        environment = input("Environment: ")

    role = input("Role: ")

    new_server = {
        "name": name,
        "address": address,
        "environment": environment,
        "role": role,
        "status": "unknown",
        "last_checked": ""
    }
    servers.append(new_server)
    save_servers(servers, data_file)
    print(f"Server {name} was added")


def remove_server(servers, data_file):
    name = input("Name of the server to remove: ")
    server = find_server(servers, name)
    if server is None:
        print("This server was not found")
        return
    if server["environment"] == "prod":
        answer = input(f" {name} is a prod server. "
                       f"Are you sure you want to remove it? yes/no")
        if answer != "yes":
            print("Removal cancelled")
            return
    servers.remove(server)
    save_servers(servers, data_file)
    print(f"Server {name} was removed")


def check_one_server(servers, data_file):
    name = input("Name of the server to check: ")
    server = find_server(servers, name)
    if server is None:
        print("This server was not found")
        return
    check_server(server)
    save_servers(servers, data_file)
    print(f"Server {server['name']}"
          f" is {server['status']} "
          f"checked {server['last_checked']}")


def show_menu():
    print()
    print("====== Server Inventory Tool ======")
    print("1.Show all servers")
    print("2.Show servers in environment")
    print("3.Add a server")
    print("4.Remove a server")
    print("5.Check a server")
    print("6.Check all servers")
    print("7.Export a report as CSV")
    print("8.Quit")


def run_menu(servers, data_file):
    while True:
        show_menu()
        choice = input("Enter choice: ")
        if choice == "1":
            show_servers(servers)
        elif choice == "2":
            environment = input("Which environment?")
            matching = match_environment(servers, environment)
            show_servers(matching)
        elif choice == "3":
            add_server(servers, data_file)
        elif choice == "4":
            remove_server(servers, data_file)
        elif choice == "5":
            check_one_server(servers, data_file)
        elif choice == "6":
            print("Checking all servers, please wait...")
            check_all_servers(servers)
            save_servers(servers, data_file)
            show_servers(servers)
        elif choice == "7":
            report_file = export_csv(servers)
            print(f"Report saved to {report_file}")
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8")
