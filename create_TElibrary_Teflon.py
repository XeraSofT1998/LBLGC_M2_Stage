

def read(path):
    f = open(path, 'r')
    lines = f.readlines()
    f.close()
    return lines

def write(path, content):
    f = open(path, "w")
    for line in content:
        f.write(line)

    f.close()

def GetOrderTeFromGFF(GFF_file, TE_file):
    new_content = []
    for line in TE_file:
        if line.startswith(">"):
            for line2 in GFF_file:
                if "Target="+(line[1:]).replace("\n", "") in line2:
                    new_content.append(line.replace("\n", "") + "#" + line2.split("\t")[-1].split("Order=")[-1].split(";")[0] + "\n")
                    break
        else:
            new_content.append(line)
    return new_content

def RunProgram(path_TE, path_GFF, output_path):
    GFF_file = read(path_GFF)
    TE_file = read(path_TE)

    new_file = GetOrderTeFromGFF(GFF_file, TE_file)
    write(output_path, new_file)

if __name__ == '__main__':

    path_TE = "FsylCur4_denovoLibTEs.fa"
    path_GFF = "FsylCur4_refTEs_wclassif_wreliable.gff"

    output_path = "TeLibrary_Fagus.fa"

    RunProgram(path_TE, path_GFF, output_path)