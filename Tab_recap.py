



def read(path):
    f = open(path, 'r')
    lines = f.readlines()
    f.close()
    lines = list(map(lambda x: x.replace('\n', ''), lines))
    return lines

def get_ID_LOG2FC_PvalAdj(DESeq):
    dico_info = {}
    for line in DESeq:
        geneID = line.split("\t")[0].replace("\n", "")
        Log2FC = line.split("\t")[2].replace("\n", "")
        PValueAdj = line.split("\t")[-1].replace("\n", "")
        dico_info[geneID] = [Log2FC, PValueAdj]
    return dico_info

def get_TPM(dico_information, Sample_Salmon, Transcript = True):

    for ID, data in dico_information.items():
        for line in Sample_Salmon:
            if str(ID) in line:
                if Transcript is True:
                    if ID.split(".")[2] == (line.split('\t')[0]).split('.')[2]:
                        TPM = line.split("\t")[3].replace("\n", "")
                        data.append(TPM)
                else:
                    TPM = line.split("\t")[3].replace("\n", "")
                    data.append(TPM)

    return dico_information

def get_IDarabidopsis_GoTerm_function(dico, Annotation, Transcript = True):
    for ID, data in dico.items():
        listID_arabi = []
        listGOterm = []
        list_function = []
        for line in Annotation:
            if str(ID) in line:
                if Transcript is True:
                    if ID.split(".")[2] == (line.split('\t')[2]).split('.')[2]:
                        print(ID.split(".")[2], (line.split('\t')[2]).split('.')[2])
                        GO = line.split("\t")[9]
                        IDarabi = line.split("\t")[10]
                        fonction = line.split("\t")[11]

                        listID_arabi.append(IDarabi.replace("\n", ""))
                        listGOterm.append(GO.replace("\n", ""))
                        list_function.append(fonction.replace("\n", ""))
                else:
                    if ID.split(".")[1] == (line.split('\t')[1]).split('.')[1]:
                        GO = line.split("\t")[9]
                        IDarabi = line.split("\t")[10]
                        fonction = line.split("\t")[11]

                        listID_arabi.append(IDarabi.replace("\n", ""))
                        listGOterm.append(GO.replace("\n", ""))
                        list_function.append(fonction.replace("\n", ""))

        data.append(' '.join(list(set(listID_arabi))))
        data.append(' '.join(list(set(listGOterm))))
        data.append(' '.join(list(set(list_function))))


    return dico


def RunProgram(DESeq, salmon_list, Ptri_Annotation_Phytozome, path, Transcript):
    dico_information = get_ID_LOG2FC_PvalAdj(DESeq)

    for salmon in salmon_list:
        dico_information = get_TPM(dico_information, salmon, Transcript)

    # get ID arabidospsis + term GO  + function in pythozome annotation txt
    dico_information = get_IDarabidopsis_GoTerm_function(dico_information, Ptri_Annotation_Phytozome, Transcript)

    f = open(path, "w")
    header = "ID_Populus" + "\t" + "LOG2FC" + "\t" + "PValueAdj" + "\t" + "TPM_data1" + "\t" + "TPM_data2" + "\t" + "TPM_data3" + "\t" + "TPM_data4" + "\t" + "TPM_data5" + "\t" + "TPM_data6" + "\t" + "ID_arabidopsis T." + "\t" + "GO_term" + "\t" + "Fonction" + "\n"
    f.write(header)
    for IDgene, data in dico_information.items():
        f.write(IDgene + "\t")
        size = len(data)
        index = 0
        for el in data:
            index += 1
            if index == size:
                f.write(el + "\n")
            else:
                f.write(el + "\t")

    f.close()


if __name__ == '__main__':

    #give a name to the output
    output_path = "TemoinvsKD_S_gene_tab_recap.tabular"
    Transcript = False
    #Phytozome file
    Ptri_Annotation_Phytozome = read("Ptrichocarpa_533_v4.1.annotation_info.txt")

    #DEG's from deseq2
    DESeq = read("Galaxy16-[DESeq2_result_file_on_data_2,_data_15,_and_others].tabular")

    #Salmon used for this DEG's discovered
    Sample1_Salmon = read("Galaxy22-[Salmon_quant_on_data_14,_data_8,_and_others_(Gene_Quantification)].tabular")
    Sample2_Salmon = read("Galaxy24-[Salmon_quant_on_data_14,_data_10,_and_others_(Gene_Quantification)].tabular")
    Sample3_Salmon = read("Galaxy26-[Salmon_quant_on_data_14,_data_12,_and_others_(Gene_Quantification)].tabular")
    Sample4_Salmon = read("Galaxy211-[Salmon_quant_on_data_2,_data_189,_and_others_(Gene_Quantification)].tabular")
    Sample5_Salmon = read("Galaxy213-[Salmon_quant_on_data_2,_data_195,_and_others_(Gene_Quantification)].tabular")
    Sample6_Salmon = read("Galaxy215-[Salmon_quant_on_data_2,_data_201,_and_others_(Gene_Quantification)].tabular")

    salmon_list = [Sample1_Salmon, Sample2_Salmon, Sample3_Salmon, Sample4_Salmon, Sample5_Salmon, Sample6_Salmon]
    RunProgram(DESeq, salmon_list, Ptri_Annotation_Phytozome, output_path, Transcript)