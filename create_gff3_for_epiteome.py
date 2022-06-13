


def read(path):
    f = open(path, 'r')
    lines = f.readlines()
    f.close()
    return lines

def write_in_file(path, file_content_list):
    print("saving the modification in file : \n" + path)
    f = open(path, "w")
    for line in file_content_list:
        f.write(line)
    f.close()

def modif_gff3(file, path):
    f = open(path, "w")
    f2 = open("teid.lst", "w")
    header = True
    for line in file:
        if header is False:
            if (int(line.split("\t")[4]) - int(line.split("\t")[3]))>999:
                new_line = []
                line = line.split('\t')
                new_line.append(line[0])
                new_line.append(line[1])
                new_line.append("te")
                new_line.append(line[3])
                new_line.append(line[4])
                new_line.append(line[7])
                new_line.append(line[6])
                new_line.append(line[7])
                #identifiant
                id = line[-1].split(";")[0]
                f2.write(id.split("=")[1]+ "\n")
                #sF
                te_class = (line[-1].split(";")[-1].replace("\n", "")).replace("class=", "sF=")
                #Fam
                name = line[-1].split(";")[1].replace("Name=", "fam=")
                new_line.append(";".join([id, te_class, name]) + "\n")
                f.write("\t".join(new_line))
                if te_class == "sF=LTR/Copia" :
                    print(id.split("=")[1])
        else:
            header = False
            f.write(line)
    f.close()
    f2.close()


if __name__ == '__main__':

    input_file = "Ptrichocarpa_533_v4.1.repeatmasked_assembly_v4.0.gff3"
    output_file = "reformed_Ptrichocarpa_533_v4.1.repeatmasked_assembly_v4.0.gff3"

    file = read(input_file)

    new_file = modif_gff3(file, output_file)
