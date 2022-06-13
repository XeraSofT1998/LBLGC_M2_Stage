
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

def get_gene_from_gff(methylome_file, gff_file, header = True):
    #create dictionnary that will contain information of position & methylation
    content_in_gene = []
    content_not_in_gene = []

    #value just to create a compteu
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
                if chromo == info.split("\t")[0]:
                    inf = int(info.split("\t")[3].replace(" ", ""))
                    sup = int(info.split("\t")[4].replace(" ", ""))
                    strand = info.split("\t")[6].replace(" ", "")

                    if pos_meth_s >= inf and pos_meth_s <= sup:
                        ID = ((info.split("\t")[-1].split(";")[0]).replace("ID=", "")).replace(".v4.1", "") + "\n"
                        content_in_gene.append(line.replace("\n","") + "\t" + ID)
                        print(compt, "/",max)
                        break

                    elif pos_meth_e >= inf and pos_meth_e <= sup:
                        ID = ((info.split("\t")[-1].split(";")[0]).replace("ID=", "")).replace(".v4.1", "") + "\n"
                        content_in_gene.append(line.replace("\n","") + "\t" + ID)
                        print(compt, "/",max)
                        break

                    #if the position is not contained between two position in the gff
                    # that mean : the methylation is in intergenic part
                if pun == len(gff_file):
                    ID = "INTERGENIC" + "\n"
                    content_not_in_gene.append(line.replace("\n","") + "\t" + ID)
                    print("none")
        else:
            header = False
            content_in_gene.append(line)
            content_not_in_gene.append(line)
        compt += 1
    return content_in_gene, content_not_in_gene



if __name__ == '__main__':

    input_path = "All_data/Pnigra_Memoire/DMC_CG_PG31_MEMOIRE.bed"
    gff_path = "GFF_specific/Ptrichocarpa_533_v4.1.gene_exons_intron.gff3"

    methylome_file = read(input_path)
    gff_file = read(gff_path)

    new_methylome_file_genic, new_methylome_file_intergenic  = get_gene_from_gff(methylome_file, gff_file)
    genic_path = "/".join(input_path.split("/")[0:2]) + "/genic_" + input_path.split("/")[-1]
    intergenic_path = "/".join(input_path.split("/")[0:2]) + "/intergenic_" + input_path.split("/")[-1]

    write(genic_path, new_methylome_file_genic)
    write(intergenic_path, new_methylome_file_intergenic)

   # print(new_methylome_file)
