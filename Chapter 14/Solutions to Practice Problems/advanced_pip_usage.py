import subprocess
import os

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if process.returncode == 0:
        print(out.decode('utf-8'))
    else:
        print(f"Error: {err.decode('utf-8')}")

if __name__ == "__main__":
    # Create a PIP configuration file with specified settings
    config_dir = os.path.join(os.path.expanduser("~"), ".pip")
    os.makedirs(config_dir, exist_ok=True)
    config_file = os.path.join(config_dir, "pip.conf")
    
    with open(config_file, 'w') as file:
        file.write("[global]\n")
        file.write("timeout = 60\n")
        file.write("index-url = https://pypi.org/simple/\n")
        file.write("trusted-host = pypi.org\n")
    
    # Print the configuration file content
    with open(config_file, 'r') as file:
        print(file.read())
    
    # Suppose you have access to a private repository, install a package from this repository using authentication
    run_command('pip install package-name --extra-index-url https://<username>:<password>@private-repo.com/simple')
    
    # Update the PIP configuration file to set the private repository as the default index URL
    with open(config_file, 'a') as file:
        file.write("index-url = https://<username>:<password>@private-repo.com/simple\n")
    
    # Print the updated configuration file content
    with open(config_file, 'r') as file:
        print(file.read())
