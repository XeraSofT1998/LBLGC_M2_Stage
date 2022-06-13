

def read_fasta(path):
    f = open(path, 'r')
    lines = f.readlines()
    f.close()
    return lines

def get_transcript_id(fasta):
    """
    This function get the transcript ID from the fasta (containing transcript ID and Sequences)
    """
    list_id = []
    for line in fasta:
        if line.startswith(">"):
            line = line.split(' ')
            line = line[0]
            list_id.append(line[1:].replace("\n", ""))
    return list_id

def get_dico_transcript(list_transcript_id) :
    """
    This function get the gene id and transcript id for each alternative splicing (gifted in the transcript.fa)
    """
    dico_transcript_gene = {}  #key = transcript id, value = gene id

    for id in list_transcript_id:
        id = id.replace(" ", "")
        new_id = id.split(".")
        new_id = new_id[0] + "." + new_id[1]
        dico_transcript_gene[id] = new_id
    return dico_transcript_gene

def write_dico_in_file(dico, name_file):
    """
    Write tabular file containing Transcript - Gene 
    """
    f = open(name_file, 'w')
    for key, value in dico.items():
        f.write(key)
        f.write("\t")
        f.write(value)
        f.write("\n")

    f.close()

def Run_Program(input_file, output_file):

    fasta_transcript = read_fasta(input_file)
    list_transcript_id = get_transcript_id(fasta_transcript)
    dico_transcript_gene_mapped = get_dico_transcript(list_transcript_id)
    write_dico_in_file(dico_transcript_gene_mapped, output_file)




if __name__ == '__main__':

    input_file = "data/Ptrichocarpa_533_v4.1.transcript.fa"
    output_file = "data/Ptrichocarpa_transcript_gene_tab.txt"
    Run_Program(input_file, output_file)







