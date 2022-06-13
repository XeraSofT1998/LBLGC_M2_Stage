import matplotlib.pyplot as plt

def read(path):
    f = open(path, 'r')
    lines = f.readlines()
    f.close()
    return lines

def get_transcript_gene_in_dico(transcript_content):
    dico = {}
    for line in transcript_content:
        dico[(line.split('\t')[0]).split('.')[0] + '.' + (line.split('\t')[0]).split('.')[1]] = 0
    for key, value in dico.items():
        for line in transcript_content:
            if key in line:
                dico[key] += 1
    return dico

def create_dico_frequence(dico):
    dicoFreq = {}
    max = 0
    index = 0
    stop = False

    while stop is False:
        index += 1
        for key, value in dico.items():
            if value > max :
                max = value
            if value == index:
                try:
                    dicoFreq[value] +=1
                except:
                    dicoFreq[value] = 1
        if index == max:
            stop = True

    graduation = []
    for i in range(max+1):
        graduation.append(i)

    return [dicoFreq, graduation]

def save_dico(path, dico):
    f = open(path.split(".")[0] + "_dico." + path.split(".")[1], 'w')
    print(path.split(".")[0] + "_dico." + path.split(".")[1])
    for key, value in dico.items():
        f.write(str(key))
        f.write("\t")
        f.write(str(value))
        f.write("\n")
    f.close()

def RunProgram(DEG_file, img_name):

    file = read(DEG_file)
    dico_transcript_gene = get_transcript_gene_in_dico(file)
    save_dico(DEG_file, dico_transcript_gene)
    dico_freq = create_dico_frequence(dico_transcript_gene)
    print(dico_freq)
    plt.bar(list(dico_freq[0].keys()), dico_freq[0].values(), color='r')
    plt.xticks(dico_freq[1], color='black')

    plt.title(img_name)
    plt.xlabel("nbr de transcript")
    plt.ylabel("nbr de gene")
    plt.savefig(img_name + '.png')
    plt.show()

if __name__ == '__main__':

    output_name = "Temoin_CvS_transcript"

    DEG_file = "/home/alexandre/Documents/LBLGC/Script/histogramme/myDEG's/" + output_name + ".tabular"
    RunProgram(DEG_file, "histogram_" + output_name)

