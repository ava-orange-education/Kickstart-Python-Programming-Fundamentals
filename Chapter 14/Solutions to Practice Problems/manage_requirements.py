import subprocess

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if process.returncode == 0:
        print(out.decode('utf-8'))
    else:
        print(f"Error: {err.decode('utf-8')}")

if __name__ == "__main__":
    # Create a requirements.txt file with specified packages
    with open('requirements.txt', 'w') as file:
        file.write('requests==2.25.1\n')
        file.write('numpy==1.20.0\n')
        file.write('pandas==1.2.1\n')

    # Install the packages from requirements.txt
    run_command('pip install -r requirements.txt')
    
    # Freeze the currently installed packages to a new file
    run_command('pip freeze > new_requirements.txt')
