#!/bin/bash
#
#SBATCH --partition=workq             # partition
#SBATCH --ntasks=1                   # nb de tâches à lancer en // (en général 1)
#SBATCH --nodes=1                    # nombre de nœuds à réserver pour chaque tâche (en général 1)
#SBATCH --cpus-per-task=15           # nombre de cœurs réservés pour chaque tâche (ne pas dépasser dans les calculs !
#SBATCH --mem=5GB                   # mémoire vive réservée pour chaque tâche (ne pas dépasser dans les calculs !)
#SBATCH --time=0-30:00              # durée maximum de la tâche (J-HH:MM, surtout ne pas dépasser !)
#SBATCH -o slurm.%N.%j.out    # fichier de sortie standard (STDOUT) avec le N° du noeud et le job ID
#SBATCH -e slurm.%N.%j.err    # fichier de sortie standard (STDERR) avec le N° du noeud et le job ID
#SBATCH --job-name=conv_gff2gtf   # nom de la tâche, pour l'affichage dans squeue et sacc
#SBATCH --mail-type END
#SBATCH --mail-user anouar.toumi@etu.univ-amu.fr

#Préparatif
module purge

#Need Miniconda3-4.7.10
module load system/Miniconda3-4.7.10
module load bioinfo/agat-v0.5.0

agat_convert_sp_gxf2gxf.pl --gff Ptrichocarpa_533_v4.1.gene_exons.gff3 -o result


