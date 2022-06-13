#!/bin/bash
#
#SBATCH --partition=workq             # partition
#SBATCH --ntasks=1                   # nb de tâches à lancer en // (en général 1)
#SBATCH --nodes=1                    # nombre de nœuds à réserver pour chaque tâche (en général 1)
#SBATCH --cpus-per-task=15           # nombre de cœurs réservés pour chaque tâche (ne pas dépasser dans les calculs !
#SBATCH --mem=50GB                   # mémoire vive réservée pour chaque tâche (ne pas dépasser dans les calculs !)
#SBATCH --time=2-00:00              # durée maximum de la tâche (J-HH:MM, surtout ne pas dépasser !)
#SBATCH -o slurm.%N.%j.out    # fichier de sortie standard (STDOUT) avec le N° du noeud et le job ID
#SBATCH -e slurm.%N.%j.err    # fichier de sortie standard (STDERR) avec le N° du noeud et le job ID
#SBATCH --job-name=STAR_4   # nom de la tâche, pour l'affichage dans squeue et sacc
#SBATCH --mail-type END
#SBATCH --mail-user anouar.toumi@etu.univ-amu.fr

# Préparatif
module purge

# Variable 
FASTQ1="./../reads/trimmed_data/1_R1.fastq"
FASTQ2="./../reads/trimmed_data/1_R2.fastq"
GENOME="./Ptrichocarpa_533_v4.0.fa"
GTF="./Ptrichocarpa_533_v4.1.gene_exons.gtf"
INDEX="./star-genome"

#Load binaries
module load bioinfo/STAR-2.7.9a

# calculate indexes. You don't need to recalculte the indexes if they already exist.
mkdir star-genome
STAR --runMode genomeGenerate --genomeDir star-genome --genomeFastaFiles ${GENOME} --genomeSAindexNbases 13 --runThreadN ${SLURM_CPUS_PER_TASK}

# Run the mapping task
STAR --genomeDir ${INDEX} --readFilesIn ${FASTQ1} ${FASTQ2} --runThreadN ${SLURM_CPUS_PER_TASK} --sjdbGTFfile ${GTF} -outSAMtype BAM_Unsorted --quantMode TranscriptomeSAM GeneCounts --outReadsUnmapped Fastx --alignIntronMax 11000

