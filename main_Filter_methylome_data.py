from Sort_genic_intergenic_from_data_methylome import *
from Sort_annotation_for_genic_data_methylome import *
from Sort_intergenic_in_TE_or_promoter import *
import time
import os

if __name__ == '__main__':
    samples = ["DMC_CG_DRA38_MEMOIRE.bed","DMC_CG_DRA38_P.NIGRA.bed", "DMC_CG_PG31_MEMOIRE.bed",
               "DMC_CG_PG31_P.NIGRA.bed", "DMC_CHG_DRA38_MEMOIRE.bed", "DMC_CHG_DRA38_P.NIGRA.bed",
               "DMC_CHG_PG31_MEMOIRE.bed", "DMC_CHG_PG31_P.NIGRA.bed", "DMC_CHH_DRA38_MEMOIRE.bed",
               "DMC_CHH_PG31_MEMOIRE.bed", "DMC_CHH_PG31_P.NIGRA.bed", "DMR_CG_DRA38_P.nigra.bed",
               "DMR_CG_PG31_P.nigra.bed", "DMR_CHG_DRA38_P.nigra.bed", "DMR_CHG_PG31_P.nigra.bed",
               "DMR_CHH_DRA38_P.nigra.bed", "DMR_CHH_PG31_P.nigra.bed", "DRA38_MEMOIRE_DMR_CG.bed",
               "DRA38_MEMOIRE_DMR_CHG.bed", "DRA38_MEMOIRE_DMR_CHH.bed", "PG31_MEMOIRE_DMR_CG.bed",
               "PG31_MEMOIRE_DMR_CHG.bed", "PG31_MEMOIRE_DMR_CHH.bed"
               ]

    for sample in samples:

        start = time.time()

        working_dir = sample.split(".")[0]

        #DATA to sort methylome by genic and intergenic
        input_path = "All_data/Pnigra_Memoire/"
        gff_path = "GFF_specific/Ptrichocarpa_533_v4.1.gene_exons_intron.gff3"

        methylome_file = read(input_path+sample)

        output_path = "All_analyse/Pnigra_Memoire/" + working_dir + "/"
        os.system("mkdir " + output_path)

        gff_file = read(gff_path)

        #Sort it !
        new_methylome_file_genic, new_methylome_file_intergenic = get_gene_from_gff(methylome_file, gff_file)

        #Save them
        genic_path = output_path + "genic_" + sample
        write(genic_path, new_methylome_file_genic)

        intergenic_path = output_path + "intergenic_" + sample
        write(intergenic_path, new_methylome_file_intergenic)
    #========================================
        #let's go sort DATA genic by presence in UTR five or not
        gff_path = "GFF_specific/Ptrichocarpa_533_v4.1.five_prime_UTR_only.gff3"

        #get the methylome in the "genic" part
        methylome_file = new_methylome_file_genic
        gff_file = read(gff_path)

        #Sort them by 5'UTR or not
        content_in_gff_five_prime, content_not_in_five_prime_gff = sort_data_from_specific_gff(methylome_file, gff_file, "UTR_five_prime")

        # Save them
        output_path_five_prime = output_path + "UTR_five_" + sample
        write(output_path_five_prime, content_in_gff_five_prime)

        output_path_not_five_prime = output_path + "Not_UTR_five_" + sample
        write(output_path_not_five_prime, content_not_in_five_prime_gff)
        # ========================================
        # let's go sort DATA genic & not in five prime UTR by presence in UTR three or not
        gff_path = "GFF_specific/Ptrichocarpa_533_v4.1.three_prime_UTR.gff3"

        #get methylome data i genic part and not in five prime UTR
        methylome_file = content_not_in_five_prime_gff
        gff_file = read(gff_path)

        #Sort by 3'UTR or not
        content_in_gff_three_prime, content_not_in_three_prime_gff = sort_data_from_specific_gff(methylome_file, gff_file, "UTR_three_prime")

        #Save it !
        output_path_three_prime = output_path + "UTR_three_" + sample
        write(output_path_three_prime, content_in_gff_three_prime)

        output_path_not_three_prime = output_path + "Not_UTR_three_" + sample
        write(output_path_not_three_prime, content_not_in_three_prime_gff)

        # ========================================
        # let's go sort Data genic not 5' UTR or 3' UTR by presence or not in Junction exon/intron
        gff_path = "GFF_specific/Ptrichocarpa_533_v4.1.junction_intron_exon.gff3"
        gff_file = read(gff_path)
        methylome_file = content_not_in_three_prime_gff

        content_in_gff_junction, content_not_in_gff_junction = sort_data_from_specific_gff(methylome_file, gff_file, "jonction_intron_exon")

        # Sort it !
        output_path_junction = output_path + "junction_" + sample
        write(output_path_junction, content_in_gff_junction)

        # Save it !
        output_path_not_junction = output_path + "not_junction_" + sample
        write(output_path_not_junction, content_not_in_gff_junction)

        # ========================================
        # let's go sort Data genic not 5' UTR or 3' UTR by presence or not in exon
        gff_path = "GFF_specific/Ptrichocarpa_533_v4.1.exon_only.gff3"
        gff_file = read(gff_path)

        content_in_gff, content_not_in_gff = sort_data_from_specific_gff(methylome_file, gff_file, "exon")

        # Sort it !
        output_path_exon = output_path + "exon_" + sample
        write(output_path_exon, content_in_gff)

        # Save it !
        output_path_not_exon = output_path + "not_exon_" + sample
        write(output_path_not_exon, content_not_in_gff)


        # ========================================
        # let's go sort Data genic not 5' UTR or 3' UTR NOT EXON by presence or not in intron ->> if it's a CDS but not UTR/INTRON/EXON = Big Problem
        gff_path = "GFF_specific/Ptrichocarpa_533_v4.1.intron_only.gff3"
        gff_file = read(gff_path)
        methylome_file = content_not_in_gff

        content_in_gff, content_not_in_gff = sort_data_from_specific_gff(methylome_file, gff_file, "intron")

        # Sort it !
        output_path_intron = output_path + "intron_" + sample
        write(output_path_intron, content_in_gff)

        # Save it !
        output_path_problem = output_path + "PROBLEMS_" + sample
        write(output_path_problem, content_not_in_gff)


        #========================================
        #let's check if intergenic data is TE

        gff_file = read("GFF_specific/Ptrichocarpa_533_v4.1.all_te.gff3")
        content_in_Te, content_not_in_Te = intersect_dmc_to_gff(new_methylome_file_intergenic, gff_file, 2, 0, 1)

        output_path_te = output_path + "Te_" + sample
        write(output_path_te, content_in_Te)

        output_path_not_te = output_path + "not_in_Te_" + sample
        write(output_path_not_te, content_not_in_Te)
        # ==============================================================================================

        gff_file = read("GFF_specific/Ptrichocarpa_533_v4.1.PROMOTER_prox.gff3")
        content_in_promoter, content_not_in_promoter = intersect_dmc_to_gff(content_not_in_Te, gff_file, 3, 8, 0)

        output_path_prox = output_path + "promo_prox_" + sample
        write(output_path_prox, content_in_promoter)

        # ==============================================================================================
        gff_file = read("GFF_specific/Ptrichocarpa_533_v4.1.PROMOTER_dist.gff3")
        content_in_promoter, content_not_in_promoter = intersect_dmc_to_gff(content_not_in_Te, gff_file, 3, 8, 0)

        output_path_dist = output_path + "promo_dist_" + sample
        write(output_path_dist, content_in_promoter)

        output_path_inter = output_path + "intergenomic_" + sample
        write(output_path_inter, content_not_in_promoter)

        end = time.time()
        print("le script à durée : ",format(end-start))
