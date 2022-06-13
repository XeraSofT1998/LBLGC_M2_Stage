#!/bin/bash
#
#SBATCH --partition=workq             # partition
#SBATCH --ntasks=1                   # nb de tâches à lancer en // (en général 1)
#SBATCH --nodes=1                    # nombre de nœuds à réserver pour chaque tâche (en général 1)
#SBATCH --cpus-per-task=45          # nombre de cœurs réservés pour chaque tâche (ne pas dépasser dans les calculs !
#SBATCH --mem=100GB                   # mémoire vive réservée pour chaque tâche (ne pas dépasser dans les calculs !)
#SBATCH --time=4-00:00              # durée maximum de la tâche (J-HH:MM, surtout ne pas dépasser !)
#SBATCH -o slurm.%N.%j.out    # fichier de sortie standard (STDOUT) avec le N° du noeud et le job ID
#SBATCH -e slurm.%N.%j.err    # fichier de sortie standard (STDERR) avec le N° du noeud et le job ID
#SBATCH --job-name=WGBS_Teflon   # nom de la tâche, pour l'affichage dans squeue et sacc
#SBATCH --mail-type END
#SBATCH --mail-user alexandre.duplan@etu.univ-amu.fr

# Loading tools
module purge
module load system/Python-2.7.15
module load bioinfo/RepeatMasker-4.1.2-p1
module load bioinfo/samtools-1.3.1
module load bioinfo/bwa-0.7.17

# Variable incrementation
WD="./sample_output_WGBS_test/"
PREFIX="LBLGC_data"

GENOME="./Ptrichocarpa_533_v4.0.fa"
READS1="./WGBS_data/B00FLQW_1.IND320.fastq"
READS2="./WGBS_data/B00FLQW_2.IND320.fastq"
SAMPLES="./sample_names.txt"
TELIBRARY="./TE_databases/new_TE_more_than_1000pb.fasta"

#Tools path
REPEATMASKER="/usr/local/bioinfo/src/RepeatMasker/RepeatMasker-4.1.2-p1/RepeatMasker"
BWA="/usr/local/bioinfo/src/bwa/bwa-0.7.17/bwa"
SAMTOOLS="/usr/local/bioinfo/src/samtools/samtools-1.3.1/samtools"

#coverage value
COV=20

# Exécuter le calcul

##For each samples

#srun python ./../teflon_prep_custom.py -wd ${WD}reference -e ${REPEATMASKER} -g ${GENOME} -l ${TELIBRARY} -p ${PREFIX} -c 250 -m 200 -s 100 -d 20 -t ${SLURM_CPUS_PER_TASK}

#srun python ./../bwa-meth-master/bwameth.py index ${WD}reference/${PREFIX}.prep_MP/${PREFIX}.mappingRef.fa

#srun python ./../bwa-meth-master/bwameth.py --threads ${SLURM_CPUS_PER_TASK} --reference ${WD}reference/${PREFIX}.prep_MP/${PREFIX}.mappingRef.fa ${READS1} ${READS2} > ${WD}reference/${PREFIX}.sam

#srun samtools view -Sb ${WD}reference/${PREFIX}.sam | samtools sort -@ ${SLURM_CPUS_PER_TASK} -o ${WD}reference/${PREFIX}.sorted.bam

#srun samtools index ${WD}reference/${PREFIX}.sorted.bam

#srun rm ${WD}reference/${PREFIX}.sam

#Run Teflon
##For each samples
srun python ./../teflon.v0.4.py -wd ${WD} -d ${WD}reference/${PREFIX}.prep_TF/ -s ${SAMPLES} -i sample1 -eb ${BWA} -es ${SAMTOOLS} -l1 family -l2 class -q 20 -cov ${COV} -t ${SLURM_CPUS_PER_TASK} -sd 20

#Teflon collapse
##Only once
srun python ./../teflon_collapse.py -wd ${WD} -d ${WD}reference/${PREFIX}.prep_TF/ -s ${SAMPLES} -es ${SAMTOOLS} -n1 3 -n2 3 -q 20 -t ${SLURM_CPUS_PER_TASK}

#Teflon Count
##For each samples
srun python ./../teflon_count.py -wd ${WD} -d ${WD}reference/${PREFIX}.prep_TF/ -s ${SAMPLES} -i sample1 -eb ${BWA} -es ${SAMTOOLS} -l2 class -q 20 -t ${SLURM_CPUS_PER_TASK}

#Teflon genotype
##Only once
srun python ./../teflon_genotype.py -wd ${WD} -d ${WD}reference/${PREFIX}.prep_TF/ -s ${SAMPLES} -lt 1 -ht 100 -dt pooled
