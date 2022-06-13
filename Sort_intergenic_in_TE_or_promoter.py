
def read(path):
    content = []
    f = open(path, 'r')
    for line in f:
        content.append(line)
    f.close()
    return content

def write(path, content):
    f = open(path, "w")
    for line in content:
        f.write(line)
    f.close()

def intersect_dmc_to_gff(methylome_file, gff_file, start_pos, pos_id_in_gff, pos_chromo_in_gff, header= True):

    #create dictionnary that will contain information of position & methylation
    content = []
    not_in_content = []

    #value just to create a timer
    compt = 0
    max = len(methylome_file)-1

    #for each methylation
    for line in methylome_file:

        if header is False:
            #get the first position of methylation
            chromo = line.replace("\n","").split("\t")[0]
            pos_meth_s = int(line.replace("\n","").split("\t")[1])
            pos_meth_e = int(line.replace("\n","").split("\t")[2])
            pun = 0

            #and let's get the information in the gff file thanks to the positions
            for info in gff_file:
                pun += 1
                if chromo == info.split("\t")[pos_chromo_in_gff]:
                    inf = int(info.split("\t")[start_pos].replace(" ", ""))
                    sup = int(info.split("\t")[start_pos+1].replace(" ", ""))

                    #if the position is contained between two start & stop in the gff
                    # that mean : the methylation is in a TE
                    if pos_meth_s >= inf and pos_meth_s <= sup:
                        ID = info.split("\t")[pos_id_in_gff] + "\n"
                        content.append(line.replace("\n","") + "\t" + ID)
                        print(compt, "/",max)
                        break
                    elif pos_meth_e >= inf and pos_meth_e <= sup:
                        ID = info.split("\t")[pos_id_in_gff] + "\n"
                        content.append(line.replace("\n","") + "\t" + ID)
                        print(compt, "/",max)
                        break
                    #if the position is not contained between two position in the gff
                    # that mean : the methylation is in intergenic part
                if pun == len(gff_file):
                    not_in_content.append(line)
                    print(compt, "/",max)

        #just save the header (a the begging)
        else:
            header = False
            content.append(line)
            not_in_content.append(line)
        compt += 1

    return content, not_in_content

if __name__ == '__main__':

    samples = ["DMC_CG_DDM1_15-7_S", "DMC_CG_KD2_C", "DMC_CG_KD2_S",
               "DMC_CG_OX1_C", "DMC_CG_OX1_S", "DMC_CHG_DDM1_15-7_S",
               "DMC_CHG_KD2_C", "DMC_CHG_KD2_S", "DMC_CHG_OX1_C",
               "DMC_CHG_OX1_S", "DMC_CHH_DDM1_15-7_S", "DMC_CHH_KD2_C",
               "DMC_CHH_KD2_S", "DMC_CHH_OX1_C", "DMC_CHH_OX1_S",
               "DMC_DDM1_C_CG", "DMC_DDM1_C_CHG", "DMC_DDM1_C_CHH"
               ]

    for sample in samples:
        path = "All_analyse/DMC/" + sample + "/not_genomic_" + sample + ".bed"
        methylome_file = read(path)

        gff_file = read("GFF_specific/Ptrichocarpa_533_v4.1.all_te.gff3")
        content_in_Te, content_not_in_Te = intersect_dmc_to_gff(methylome_file, gff_file, 2, 0, 1)

        output_path = "/".join(path.split("/")[:-1]) + "/Te_" + path.split("/")[-1]
        write(output_path, content_in_Te)
        #==============================================================================================

        gff_file = read("GFF_specific/Ptrichocarpa_533_v4.1.PROMOTER_prox.gff3")
        content_in_promoter, content_not_in_promoter = intersect_dmc_to_gff(content_not_in_Te, gff_file, 3, 8, 0)

        output_path = "/".join(path.split("/")[:-1]) + "/promo_prox_" + path.split("/")[-1]
        write(output_path, content_in_promoter)


        # ==============================================================================================
        gff_file = read("GFF_specific/Ptrichocarpa_533_v4.1.PROMOTER_dist.gff3")
        content_in_promoter, content_not_in_promoter = intersect_dmc_to_gff(content_not_in_Te, gff_file, 3, 8, 0)

        output_path = "/".join(path.split("/")[:-1]) + "/promo_dist_" + path.split("/")[-1]
        write(output_path, content_in_promoter)

        output_path = "/".join(path.split("/")[:-1]) + "/intergenomic_" + path.split("/")[-1]
        write(output_path, content_not_in_promoter)


