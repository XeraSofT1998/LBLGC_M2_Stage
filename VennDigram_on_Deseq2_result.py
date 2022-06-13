"""
This script get DESeq2 output as input and give the VennDiagram of them.
the DESeq2 output have to be filtered on p_adj <0.05

"""


# library
import matplotlib.pyplot as plt
from venn import *
from Verbosity import *
from datetime import datetime


def read(path):
    f = open(path, 'r')
    lines = f.readlines()
    f.close()
    return lines

def get_gene_names(file):
    list_gene = []
    for line in file:
        line = line.replace("\n", "").replace(".v4.1", "").replace('"ID_Populus"', "").replace('"', "")
        line = line.split("\t")
        line = ".".join(line[0].split(".")[0:2])
        print(line)
        if line != "":
            list_gene.append(line)
    return list_gene

def Run_Program(list_input_file, list_name, Verbosity):

    # run program
    #create the dictionnary of the venn diagram (organism : {gene1, gene2})
    list_gene = []
    for file in list_input_file:
        list_gene.append(set(get_gene_names(read(file))))
    VennDictionnary = dict(zip(list_name, list_gene))

    #draw the venn diagram (with spécific size and font size)
    venn(VennDictionnary, figsize=(8, 8), fontsize=15)

    #create a name (with date) for the picture of the venn diagram
    img_title = 'figure_'
    for name in list_name:
        img_title += str(name) + "_"
    now = datetime.now()
    img_title += "figure_" + now.strftime("%m_%d_%Y_%H_%M_%S")

    #save and show the picture (with a specific dpi (dot per inch)
    plt.savefig(img_title, dpi=500)
    plt.show()

    #create the output file containing the core or the unique genome.
    run_verbosity(list_gene, list_name, Verbosity)

if __name__ == '__main__':

    #input data
    input1_DESeq2 = "/home/alexandre/Documents/LBLGC/Script/DEG_Anouar_TOUMI/DRA38_CSvSS_transcript_tab_recap.csv"
    name_grpA = "DET's DRA38 CSvSS"

    #input2_DESeq2 = "/home/alexandre/Documents/LBLGC/Script/Methylome/All_analyse/Pnigra_Memoire/DMC_CHG_PG31_MEMOIRE/genic_DMC_CHG_PG31_MEMOIRE (copie).bed"
    #name_grpB = "Methylation CHG"

    #input3_DESeq2 = "/home/alexandre/Documents/LBLGC/Script/Methylome/All_analyse/Pnigra_Memoire/DMC_CHH_PG31_MEMOIRE/genic_DMC_CHH_PG31_MEMOIRE (copie).bed"
    #name_grpC = "Methylation CHH"

    #input data
    input4_DESeq2 = "/home/alexandre/Documents/LBLGC/Script/AS_data_anouar/DRA_CS_vs_SS.txt"
    name_grpD = "AS DRA38 CSvSS"

    #input2_DESeq2 = "DEG's/DDM1/salmon/mean/Galaxy145-[DESeq2_result_file_on_data_1,_data_141,_and_others].tabular"
    #name_grpB = "DDM1"

    #input2_DESeq2 = "DEG's/DDM1/salmon/parametric/Galaxy142-[DESeq2_result_file_on_data_1,_data_141,_and_others].tabular"
    #name_grpB = "DDM1"

    #Adapt to your data
    list_name = [name_grpA, name_grpD]
    list_input = [input1_DESeq2, input4_DESeq2]

    #Run Program
    Verbosity = True #or False
    Run_Program(list_input, list_name,Verbosity)

    #ctrl_C_ctrl_S, Ctrl_C_KD_C_transcript, ctrl_C_OX_C_gene, ctrl_C_OX_C_transcript, Ctrl_ddm1_S_transcript, ctrl_KD_C_gene, Ctrl_S_KD_S_transcript, ctrl_S_OX_S_gene, ctrl_S_OX_S_transcript, KD_C_KD_S_gene, KD_C_KD_S_transcript, OX_C_OX_S_gene, OX_C_OX_S_transcript

    # import matplotlib.pyplot as plt
    #
    # dictionary = {"ControleC vs ControleS (gene)": 0,
    #               "ControleC vs ControleS (transcript)":7,
    #               "DDM1C vs DDM1S (gene)": 0,
    #               "DDM1C vs DDM1S (transcript)" : 0,
    #               "KDC vs KDS (gene)" : 1,
    #               "KDC vs KDS (transcript) " : 3,
    #               "OXC vs OXS (gene)" : 0,
    #               "OXC vs OXS (transcript)": 2,
    #               "ControleC vs DDM1C (gene)":0,
    #               "ControleC vs DDM1C (transcript)" : 0,
    #               "ControleS vs DDM1S (gene)" : 0,
    #               "ControleS vs DDM1S (transcript)" : 8,
    #               "ControleC vs KDC (gene)" : 4,
    #               "ControleC vs KDC (transcript)" : 6,
    #               "ControleS vs KDS (gene) " : 0,
    #               "ControleS vs KDS (transcript)" : 6,
    #               "ControleC vs OXC (gene)" : 3,
    #               "ControleC vs OXC (transcript" : 5,
    #               "ControleS vs OXS (gene)" : 2,
    #               "ControleS vs OXS (transcript)" : 5,
    #               }
    # plt.bar(list(dictionary.keys()), dictionary.values(), color='g')
    # plt.xticks(rotation='vertical')
    # plt.savefig("image.png", bbox_inches='tight', dpi=100)
    #
    # plt.show()

