import subprocess
import os
import shutil

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if process.returncode == 0:
        print(out.decode('utf-8'))
    else:
        print(f"Error: {err.decode('utf-8')}")

if __name__ == "__main__":
    # Create a virtual environment named myenv
    run_command('python -m venv myenv')
    
    # Activate the virtual environment
    activate_command = '.\\myenv\\Scripts\\activate' if os.name == 'nt' else 'source myenv/bin/activate'
    run_command(activate_command)
    
    # Install the requests package within the virtual environment
    run_command('pip install requests')
    
    # Deactivate the virtual environment
    deactivate_command = 'deactivate' if os.name != 'nt' else '.\\myenv\\Scripts\\deactivate'
    run_command(deactivate_command)
    
    # Delete the myenv virtual environment
    shutil.rmtree('myenv')
