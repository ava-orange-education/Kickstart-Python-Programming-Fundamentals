import subprocess

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if process.returncode == 0:
        print(out.decode('utf-8'))
    else:
        print(f"Error: {err.decode('utf-8')}")

if __name__ == "__main__":
    # Simulate a network issue by attempting to install a package without internet access, then retries with a different mirror
    print("Simulating network issue...")
    run_command('pip install requests --index-url=https://pypi.org/simple/ --timeout=60')
    
    # Install pipdeptree and list the dependency tree
    run_command('pip install pipdeptree')
    run_command('pipdeptree')
    
    # Handle a broken installation by uninstalling and reinstalling the requests package
    run_command('pip uninstall -y requests')
    run_command('pip install requests')
    
    # Clear the PIP cache
    run_command('pip cache purge')
