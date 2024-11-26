import subprocess

def run_bash_command(command):
    """Runs a Bash command and prints its output line by line.

    Args:
        command: The Bash command to execute.
    """

    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    while True:
        output = process.stdout.readline().decode('utf-8').strip()
        if output == '':
            break
        print(output)

    # Check for errors
    stderr = process.stderr.read().decode('utf-8').strip()
    if stderr:
        print(f"Error: {stderr}")

    process.wait()

if __name__ == '__main__':
    bash_command = "ra -S localhost:561"  # Replace with your desired command
    run_bash_command(bash_command)