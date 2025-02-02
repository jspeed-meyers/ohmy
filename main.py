import argparse

import python

def parse_cli():
    parser = argparse.ArgumentParser(description='Assess the trust score of your Python packages.')
    parser.add_argument('-f', '--file', type=str, help='The name of the dependency file to be ingested.')
    parser.add_argument('-v', '--verbose', action='store_true', help='Option to print verbose output.')
    return parser.parse_args()

def print_output(package_status):
    cnt = 0
    for pkg in package_status.keys():
        if package_status[pkg]:
            cnt += 1
    
    print("")
    print("TRUSTED BUILD STATUS")
    print("--------------------")
    print(f"PyPI     | {round(cnt / len(package_status) * 100)}%")
    print("--------------------")
    print("chibbies | 100%")
    print("")

    if args.verbose:
        print("PyPI Details")
        print("============")
        for pkg in package_status.keys():
            if package_status[pkg]:
                print(f"{pkg}: Trusted")
            else:
                print(f"{pkg}: Untrusted")

if __name__ == "__main__":

    args = parse_cli()

    requirements_file = args.file

    pkgs = python.get_package_names(requirements_file)
    
    package_status = python.get_python_package_status(pkgs) 

    print_output(package_status)
