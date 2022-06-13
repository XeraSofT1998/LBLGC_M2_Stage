
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

def sort_data_from_specific_gff(methylome_file, gff_file, gff_annotation, header = True):
    #create dictionnary that will contain information of position & methylation
    content_in_gff = []
    content_not_in_gff = []

    #init compt
    compt = 0
    max  = len(methylome_file) -1
    #for each methylation data
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
                if chromo == info.split("\t")[0]:
                    inf = int(info.split("\t")[3].replace(" ", ""))
                    sup = int(info.split("\t")[4].replace(" ", ""))

                    if pos_meth_s >= inf and pos_meth_s <= sup:
                        ID = gff_annotation + "\n"
                        content_in_gff.append(line.replace("\n","") + "\t" + ID)
                        print(compt, "/",max)
                        break

                    elif pos_meth_e >= inf and pos_meth_e <= sup:
                        ID = gff_annotation + "\n"
                        content_in_gff.append(line.replace("\n","") + "\t" + ID)
                        print(compt, "/",max)
                        break
                    #if the position is not contained between two position in the gff
                    # that mean : the methylation is in intergenic part
                if pun == len(gff_file):
                    content_not_in_gff.append(line)
                    print("not in gff file")
        else:
            header = False
            content_in_gff.append(line)
            content_not_in_gff.append(line)

        compt +=1

    return content_in_gff, content_not_in_gff



if __name__ == '__main__':

    #Check if data are intron
    input_path = "Not_UTR_three_Galaxy1-[methylKit_CG_All___Differential_methylation_-_subset_RNAi_DDM1_15-7_C_].bedgraph"
    gff_path = "GFF_genomic_specific/Ptrichocarpa_533_v4.1.junction_intron_exon.gff3"

    methylome_file = read(input_path)
    gff_file = read(gff_path)

    content_in_gff, content_not_in_gff = sort_data_from_specific_gff(methylome_file, gff_file, "jonction_intron_exon")

    output_path = "junction_" + input_path
    write(output_path, content_in_gff)

    output_path = "not_junction_" + input_path
    write(output_path, content_not_in_gff)



    #Check if data is in junctions
    #Check if data are exon


