#!/bin/bash
#
#SBATCH --partition=workq             # partition
#SBATCH --ntasks=1                   # nb de tâches à lancer en // (en général 1)
#SBATCH --nodes=1                    # nombre de nœuds à réserver pour chaque tâche (en général 1)
#SBATCH --cpus-per-task=55          # nombre de cœurs réservés pour chaque tâche (ne pas dépasser dans les calculs !
#SBATCH --mem=200GB                   # mémoire vive réservée pour chaque tâche (ne pas dépasser dans les calculs !)
#SBATCH --time=1-00:00              # durée maximum de la tâche (J-HH:MM, surtout ne pas dépasser !)
#SBATCH -o slurm.%N.%j.out    # fichier de sortie standard (STDOUT) avec le N° du noeud et le job ID
#SBATCH -e slurm.%N.%j.err    # fichier de sortie standard (STDERR) avec le N° du noeud et le job ID
#SBATCH --job-name=BWA_FagM   # nom de la tâche, pour l'affichage dans squeue et sacc
#SBATCH --mail-type END
#SBATCH --mail-user alexandre.duplan@etu.univ-amu.fr

# Loading tools
module purge

module load bioinfo/samtools-1.3.1
module load bioinfo/bwa-0.7.17
module load bioinfo/bamtofastq-v1.3.5


GENOME="./Genome/Scafold_1_Fagus_sylvatica_v3.fa"
READS1="./DATA/Mutant/CYR_AAAAOSDE_1_1_HLC2VDSX2.UDI315_clean.fastq"
READS2="./DATA/Mutant/CYR_AAAAOSDE_1_2_HLC2VDSX2.UDI315_clean.fastq"


# Exécuter le calcul
#Index Genome
srun bwa index ${GENOME}

#Align
srun bwa mem -t ${SLURM_CPUS_PER_TASK} -Y ${GENOME} ${READS1} ${READS2} > whole.sam

#from SAM2BAM
srun samtools view -S -b whole.sam -o whole.bam

###Extract Unmapped reads
#An unmapped read whose mate is mapped.
srun samtools view -u  -f 4 -F264 whole.bam  > tmps1.bam

#A mapped read who’s mate is unmapped
srun samtools view -u -f 8 -F 260 whole.bam  > tmps2.bam

#Both reads of the pair are unmapped
srun samtools view -u -f 12 -F 256 whole.bam > tmps3.bam

#merge
srun samtools merge -u - tmps[123].bam | samtools sort -n - unmapped

#Extract the reads in FASTQ format (paired)
srun bamToFastq -bam unmapped.bam -fq1 unmapped_reads1.fastq -fq2 unmapped_reads2.fastq

