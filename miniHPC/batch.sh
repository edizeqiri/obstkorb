#!/bin/bash
#The previous line is mandatory

#SBATCH --job-name=test_tlsh     #Name of your job
#SBATCH --cpus-per-task=8    #Number of cores to reserve
#SBATCH --mem-per-cpu=1G     #Amount of RAM/core to reserve
#SBATCH --time=06:00:00      #Maximum allocated time
#SBATCH --qos=6hours         #Selected queue to allocate your job
#SBATCH --output=myrun.o%j   #Path and name to the file for the STDOUT
#SBATCH --error=myrun.e%j    #Path and name to the file for the STDERR

module load Python/3.9.5-GCCcore-10.3.0                 #Load required modules
source $HOME/venv_numba/bin/activate
python tlsh_miner.py