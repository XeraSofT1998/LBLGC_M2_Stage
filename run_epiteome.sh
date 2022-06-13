#!/bin/bash
#
#SBATCH --partition=workq             # partition
#SBATCH --ntasks=1                   # nb de tâches à lancer en // (en général 1)
#SBATCH --nodes=1                    # nombre de nœuds à réserver pour chaque tâche (en général 1)
#SBATCH --cpus-per-task=45           # nombre de cœurs réservés pour chaque tâche (ne pas dépasser dans les calculs !
#SBATCH --mem=80GB                   # mémoire vive réservée pour chaque tâche (ne pas dépasser dans les calculs !)
#SBATCH --time=4-00:00              # durée maximum de la tâche (J-HH:MM, surtout ne pas dépasser !)
#SBATCH -o slurm.%N.%j.out    # fichier de sortie standard (STDOUT) avec le N° du noeud et le job ID
#SBATCH -e slurm.%N.%j.err    # fichier de sortie standard (STDERR) avec le N° du noeud et le job ID
#SBATCH --job-name=epiteome_copia_ltr   # nom de la tâche, pour l'affichage dans squeue et sacc
#SBATCH --mail-type END
#SBATCH --mail-user alexandre.duplan@etu.univ-amu.fr

# Préparatif
module purge

module load bioinfo/bedtools-2.26.0
module load bioinfo/samtools-1.3.1

GFF="Phytozome_Ptrichocarpa_533_v4.gff3"
TELIBRARY="teid.lst"

# Exécuter le calcul (en général avec srun)
srun ./../idxEpiTEome.pl -l 100 -gff ${GFF} -t ${TELIBRARY} -fasta Ptrichocarpa_533_v4.0.fa

srun ./../epiTEome.pl -gff ${GFF} -ref Ptrichocarpa_533_v4.0.epiTEome.masked.fasta -un B00FLQW_1.IND320__unmapped_reads.fastq -t ${TELIBRARY}
