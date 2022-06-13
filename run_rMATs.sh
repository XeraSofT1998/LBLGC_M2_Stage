#!/bin/bash
#
#SBATCH --partition=workq             # partition
#SBATCH --ntasks=1                   # nb de tâches à lancer en // (en général 1)
#SBATCH --nodes=1                    # nombre de nœuds à réserver pour chaque tâche (en général 1)
#SBATCH --cpus-per-task=16          # nombre de cœurs réservés pour chaque tâche (ne pas dépasser dans les calculs !
#SBATCH --mem=80GB                   # mémoire vive réservée pour chaque tâche (ne pas dépasser dans les calculs !)
#SBATCH --time=3-00:00              # durée maximum de la tâche (J-HH:MM, surtout ne pas dépasser !)
#SBATCH -o slurm.%N.%j.out    # fichier de sortie standard (STDOUT) avec le N° du noeud et le job ID
#SBATCH -e slurm.%N.%j.err    # fichier de sortie standard (STDERR) avec le N° du noeud et le job ID
#SBATCH --job-name=rMATs_data1   # nom de la tâche, pour l'affichage dans squeue et sacc
#SBATCH --mail-type END
#SBATCH --mail-user alexandre.duplan@etu.univ-amu.fr

# Loading tools
module purge
#module load system/Python-3.7.4
module load system/Miniconda3
#module load bioinfo/rmats-turbo-v4.1.2
module load bioinfo/bamtools-2.5.0 
module load bioinfo/samtools-1.10
 
#Exécuter le calcul
##Run rMATs
#run_rmats --b1 b1.txt --b2 b2.txt --gtf Ptrichocarpa_533_v4.1.gene_exons.gtf -t paired --readLength 101 --variable-read-length --cstat 0.0001 --nthread ${SLURM_CPUS_PER_TASK} --od output --tmp tmp_output --task both --allow-clipping --paired-stats

#Need Python-2.7.2
module load system/Python-2.7.2
module load bioinfo/rMATS.4.0.2
cd /home/aduplan/work/aduplan/rMATs
rmats.py --b1 b1.txt --b2 b2.txt --gtf Ptrichocarpa_533_v4.1.gene_exons.gtf --od output -t paired --nthread ${SLURM_CPUS_PER_TASK} --readLength 101 --anchorLength 1 --tstat 4
