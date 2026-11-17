import argparse
import sys

from storage import load_servers, get_data_file, save_servers, export_csv
from menu import run_menu, show_servers, match_environment, find_server
from checks import check_server, check_all_servers


def main():
    # describing which command-line options the program accepts
    parser = argparse.ArgumentParser(
        description="Server Inventory Tool: keep track of servers and check if they respond.")
    parser.add_argument("--list", action="store_true", help="show all servers and exit")
    parser.add_argument("--environment", help="with --list: only show servers in this environment (dev, test or prod)")
    parser.add_argument("--check", metavar="NAME", help="check one server by name if it is responding")
    parser.add_argument("--check-all", action="store_true", help="check all servers and exit")
    parser.add_argument("--export", action="store_true", help="export all servers to a csv report in reports/")
    args = parser.parse_args()
    data_file = get_data_file()
    servers = load_servers(data_file)

    if args.list:
        if args.environment:
            show_servers(match_environment(servers, args.environment))
        else:
            show_servers(servers)
    elif args.check:
        server = find_server(servers, args.check)
        if server is None:
            print(f"No server with name '{args.check}' was found")
            sys.exit(1)
        check_server(server)
        save_servers(servers, data_file)
        print(f"{server['name']} is {server['status']}, checked: "
              f"{server['last_checked']}")
        if server['status'] == 'down':
            sys.exit(1)
        sys.exit(0)
    elif args.check_all:
        check_all_servers(servers)
        save_servers(servers, data_file)
        show_servers(servers)
        # exit code 1 if at least one server is down otherwise 0
        for server in servers:
            if server['status'] == 'down':
                sys.exit(1)
        sys.exit(0)
    elif args.export:
        report_file = export_csv(servers)
        print(f"report saved to {report_file}")
    else:
        run_menu(servers, data_file)


if __name__ == "__main__":
    main()
