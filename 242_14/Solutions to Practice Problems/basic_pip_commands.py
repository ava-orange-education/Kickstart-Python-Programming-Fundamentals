
import subprocess

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if process.returncode == 0:
        print(out.decode('utf-8'))
    else:
        print(f"Error: {err.decode('utf-8')}")

if __name__ == "__main__":
    # Install the requests library
    run_command('pip install requests')
    
    # List all installed packages
    run_command('pip list')
    
    # Show details for the requests library
    run_command('pip show requests')
    
    # Upgrade the requests library to the latest version
    run_command('pip install --upgrade requests')
    
    # Uninstall the requests library
    run_command('pip uninstall -y requests')

