import os
import subprocess
from icecream import ic

# Path to the file containing the folder names
folders_file = 'all_apps'

# Remote server details
remote_user = 'zeqiri0000'
remote_host = 'transfer.scicore.unibas.ch'
remote_base_path = '/scicore/soft/apps/'

# Local directory where you want to download the folders
local_target_directory = '$HOME/Downloads/scicore'.replace('/', os.sep)
folders = ""
# Read the folder names from the file
with open(folders_file, 'r') as file:
    folders = [line.strip() for line in file]

# Loop through each folder and execute SCP command
for folder in folders:
    remote_path = f'{remote_base_path}{folder}'
    local_path = f'{local_target_directory}/{folder}'
    scp_command = f'scp -r {remote_user}@{remote_host}:{remote_path} {local_path}'

    try:
        ic(scp_command)
        #subprocess.run(scp_command, shell=True, check=True)
        print(f'Successfully downloaded {folder}')
    except subprocess.CalledProcessError as e:
        print(f'Error downloading {folder}: {e}')

# End of script
