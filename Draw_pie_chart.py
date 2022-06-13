"""
This script is usefull to draw PieChart from methylome data sorted in differents files, for each annotation)
(cf. main_Filter_methylome_data.py)
"""

import matplotlib.pyplot as plt
import numpy as np
import os

def read(path):
    """
    function to read files
    """
    content = []
    f = open(path, "r")
    for line in f.readlines():
        content.append(line)
    f.close()
    return content

def write(path, content):
    """
    function to write files
    """
    f = open(path, "w")
    for line in content:
        f.write(line)
    f.close()

def add_percent_to_labels_names(label_list, size_list):
    """
    Function to create the labels for the PieChart legends
    """
    max = 0
    new_labels_list = []
    for num in size_list:
        max += num
    for i in range(0,len(label_list)):
            new_labels_list.append(label_list[i] + " | " + str(np.round(100 * (size_list[i]/max), 1)).replace('.', ',') + "%" + " | " + str(size_list[i]))

    label_list = tuple(new_labels_list)
    return label_list

def func(pct):
        return "{:.1f}%".format(pct)

def draw_PieChart(label_list, size_list, title, save_path):
    """
    Function to create PieChart
    """

    #modify the labels list with the % of presence of each elements
    label_list = add_percent_to_labels_names(label_list, size_list)

    #create the piechart plot
    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
    wedges, autotexts = ax.pie(size_list,textprops=dict(color="w"))
    ax.legend(wedges, label_list,
              title="Légende",
              loc="center left",
              fontsize=8,
              bbox_to_anchor=(1, 0, 0.5, 1))

    plt.setp(autotexts, size=10, weight="bold")

    #add the title
    Meth_total = 0
    for i in size_list[0:-1]:
        Meth_total += i
    n_title = " ".join(title.split("_")[0:]) + "     Total Diff. meth. : " + str(Meth_total)
    ax.set_title(n_title)

    #save & show the PieChart
    save_path += "/PieChart/"
    if not os.path.exists(save_path):
        os.makedirs(save_path, exist_ok=False)

    plt.savefig(save_path + title + '.png', bbox_inches='tight', dpi = 400)
   # plt.show()

def RunProgram(working_dir, path):
    """
    Main Function to run this algorythm
    """
    #Read and get informations of each annotation for methylome data sorted by annotation (cf. main_Filter_methylome_data.py)
    dist = len(read(path + working_dir + "/promo_dist_" + working_dir + ".bed")) - 1
    label_dist = "Promoteur distal"

    prox = len(read(path + working_dir + "/promo_prox_" + working_dir + ".bed")) - 1
    label_prox = "Promoteur proximal"

    five_prime_utr = len(read(path + working_dir + "/UTR_five_" + working_dir + ".bed")) - 1
    label_five_prime_utr = "5' UTR"

    exon = len(read(path + working_dir + "/exon_" + working_dir + ".bed")) - 1
    label_exon = "Exon"

    junction = len(read(path + working_dir + "/junction_" + working_dir + ".bed")) - 1
    label_junction = "Jonction E/I"

    intron = len(read(path + working_dir + "/intron_" + working_dir + ".bed")) - 1
    label_intron = "Intron"

    three_prime_utr = len(read(path + working_dir + "/UTR_three_" + working_dir + ".bed")) - 1
    label_three_prime_utr = "3' UTR"

    Te = len(read(path + working_dir + "/Te_" + working_dir + ".bed")) - 1
    label_TE = "Éléments transposable"

    intergenic = len(read(path + working_dir + "/intergenic_" + working_dir + ".bed")) - 1
    label_intergenic = "Intergénique"

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = label_dist, label_prox, label_five_prime_utr, label_exon, label_junction, label_intron, label_three_prime_utr, label_TE, label_intergenic
    sizes = [dist, prox, five_prime_utr, exon, junction, intron, three_prime_utr, Te, intergenic]

    #draw the piechart with given data
    draw_PieChart(labels, sizes, working_dir, path)

if __name__ == '__main__':

    #all RNAi samples
    samples_RNAi = ["0_DMC_DDM1_C_CG", "1_DMC_DDM1_C_CHG", "2_DMC_DDM1_C_CHH",
     "3_DMR_on_CG_DDM1_C", "4_DMR_on_CHG_DDM1_C", "5_DMR_on_CHH_DDM1_C",
     "6_DMC_CG_KD2_C", "7_DMC_CHG_KD2_C", "8_DMC_CHH_KD2_C",
     "9_DMR_CG_KD2_C", "10_DMR_CHG_KD2_C", "11_DMR_CHH_KD2_C",
     "12_DMC_CG_OX1_C", "13_DMC_CHG_OX1_C", "14_DMC_CHH_OX1_C",
     "15_DMR_CG_OX1_C", "16_DMR_CHG_OX1_C", "17_DMR_CHH_OX1_C",
     "18_DMC_CG_DDM1_15-7_S", "19_DMC_CHG_DDM1_15-7_S", "20_DMC_CHH_DDM1_15-7_S",
     "21_DMR_CG_DDM1_15-7_S", "22_DMR_CHG_DDM1_15-7_S", "23_DMR_CHH_DDM1_15-7_S",
     "24_DMC_CG_KD2_S", "25_DMC_CHG_KD2_S", "26_DMC_CHH_KD2_S",
     "27_DMR_CG_KD2_S", "28_DMR_CHG_KD2_S", "29_DMR_CHH_KD2_S",
     "30_DMC_CG_OX1_S", "31_DMC_CHG_OX1_S", "32_DMC_CHH_OX1_S",
     "33_DMR_CG_OX1_S", "34_DMR_CHG_OX1_S", "35_DMR_CHH_OX1_S"
     ]

    #and Pnigra data
    samples_Pnigra = ["DMC_CG_DRA38_MEMOIRE","DMC_CG_DRA38_P.NIGRA", "DMC_CG_PG31_MEMOIRE",
               "DMC_CG_PG31_P.NIGRA", "DMC_CHG_DRA38_MEMOIRE", "DMC_CHG_DRA38_P.NIGRA",
               "DMC_CHG_PG31_MEMOIRE", "DMC_CHG_PG31_P.NIGRA", "DMC_CHH_DRA38_MEMOIRE",
               "DMC_CHH_PG31_MEMOIRE", "DMC_CHH_PG31_P.NIGRA", "DMR_CG_DRA38_P.nigra",
               "DMR_CG_PG31_P.nigra", "DMR_CHG_DRA38_P.nigra", "DMR_CHG_PG31_P.nigra",
               "DMR_CHH_DRA38_P.nigra", "DMR_CHH_PG31_P.nigra", "DRA38_MEMOIRE_DMR_CG",
               "DRA38_MEMOIRE_DMR_CHG", "DRA38_MEMOIRE_DMR_CHH", "PG31_MEMOIRE_DMR_CG",
               "PG31_MEMOIRE_DMR_CHG", "PG31_MEMOIRE_DMR_CHH"
               ]

    #get the working directory of the Pnigra & Rnai data sorted by annotation
    working_dir = "/home/alexandre/Documents/LBLGC/Script/Methylome/All_analyse/"

    #for sample in samples_Pnigra:
    #    path = working_dir + "Pnigra_Memoire/"

    #    RunProgram(sample, path)

    #run this function for each RNAi data
    for sample in samples_RNAi:
        path = working_dir + "RNAi/"

        RunProgram(sample, path)

