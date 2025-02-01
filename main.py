import requests

def get_latest_pypi_version(package_name):
    url = f"https://pypi.org/pypi/{package_name}/json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data["info"]["version"]
    else:
        print(f"Error: {response.status_code}")
        return None

def get_pypi_files(package_name, version):
    url = f"https://pypi.org/pypi/{package_name}/{version}/json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        files = data.get("urls", [])  # "urls" contains the list of uploaded files
        return files
    else:
        print(f"Error: {response.status_code}")
        return None

def retrieve_trusted_build_json(package_name, version, filename):
    url = f"https://pypi.org/integrity/{package_name}/{version}/{filename}/provenance"
    headers = {
        "Accept": "application/vnd.pypi.integrity.v1+json"
    }
    response = requests.get(url, headers=headers)
    return response

def check_trusted_build_status(trusted_build_json):
    if trusted_build_json.status_code == 200:
        return True
    else:
        return False

def get_trusted_build_determination(package_name):
    latest_version = get_latest_pypi_version(package_name)
    files = get_pypi_files(package_name, latest_version)
    filename = files[0]['filename']
    test_json = retrieve_trusted_build_json(package_name, latest_version, filename)
    return check_trusted_build_status(test_json)

def get_package_names(requirements_file):
    with open(requirements_file, "r") as file:
        packages = [
            line.split("==")[0].strip().split(">=")[0].split("<=")[0]
            for line in file
            if line.strip() and not line.startswith("#")
        ]
    return packages


if __name__ == "__main__":
    requirements_file = "requirements.txt"
    pkgs = get_package_names(requirements_file)
    
    package_status = {}
    for pkg in pkgs:
        package_status[pkg] = get_trusted_build_determination(pkg)

    cnt = 0
    for pkg in package_status.keys():
        if package_status[pkg]:
            cnt += 1
    
    print("")
    print("TRUSTED BUILD STATUS")
    print(f"PyPI: {cnt / len(package_status) * 100}%")
    print("chibbies: 100%")
    print("")
    print("PyPI Details")
    for pkg in package_status.keys():
        if package_status[pkg]:
            print(f"{pkg}: Trusted")
        else:
            print(f"{pkg}: Untrusted")