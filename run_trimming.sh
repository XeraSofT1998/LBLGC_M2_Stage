#!/bin/bash
#
#SBATCH --partition=workq             # partition
#SBATCH --ntasks=1                   # nb de tâches à lancer en // (en général 1)
#SBATCH --nodes=1                    # nombre de nœuds à réserver pour chaque tâche (en gé$
#SBATCH --cpus-per-task=20           # nombre de cœurs réservés pour chaque tâche (ne pas $
#SBATCH --mem=15GB                   # mémoire vive réservée pour chaque tâche (ne pas dép$
#SBATCH --time=1-00:00              # durée maximum de la tâche (J-HH:MM, surtout ne pas d$
#SBATCH -o slurm.%N.%j.out    # fichier de sortie standard (STDOUT) avec le N° du noeud et$
#SBATCH -e slurm.%N.%j.err    # fichier de sortie standard (STDERR) avec le N° du noeud et$
#SBATCH --job-name=trimming   # nom de la tâche, pour l'affichage dans squeue et sacc
#SBATCH --mail-type END
#SBATCH --mail-user alexandre.duplan@etu.univ-amu.fr

# Préparatif
module purge

module load system/Python-3.4.3
module load bioinfo/TrimGalore-0.6.5
module load bioinfo/cutadapt-1.14-python-3.4.3
module load bioinfo/FastQC_v0.11.5

# Variable
FASTA1=""
FASTA2=""

# Exécuter le calcul (en général avec srun)
trim_galore -q 30 --paired -o ./trimmed_data/ ${FASTA1} ${FASTA2}

