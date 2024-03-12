import subprocess

# Path to the directory containing the scripts (adjust this path accordingly)
scripts_directory = '/root/Twitch-Channel-Points-Miner-v2'

# Run scripts from run.py to run30.py
for i in range(11, 31):
    script_filename = f'run{i}.py'
    script_path = f'{scripts_directory}/{script_filename}'

    try:
        subprocess.run(['python', script_path], check=True)
        print(f'Successfully ran {script_filename}')
    except subprocess.CalledProcessError as e:
        print(f'Error running {script_filename}: {e}')
