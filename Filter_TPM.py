


def read(path):
    f = open(path, 'r')
    lines = f.readlines()
    f.close()
    return lines

def get_TPM_values(path, file_in_list, TPM_value):
    f = open(path, 'w')
    header_line = 1
    index = 0
    for line in file_in_list:
        index +=1
        if index > header_line:
            line = line.split("\t")
            if line[3] == "tpm":
                for i in line:
                    index2 += 1
                    f.write(i)
                    if index2 != 25:
                        f.write("\t")
                break
            if float(line[3])>float(TPM_value) or float(line[7])>float(TPM_value) or float(line[11])>float(TPM_value) or float(line[15])>float(TPM_value) or float(line[19])>float(TPM_value) or float(line[23])>float(TPM_value):
                index2 = 0
                print(line[0], float(line[3]), float(line[7]), float(line[11]), float(line[15]), float(line[19]), float(line[23]))
                for i in line:
                    index2 += 1
                    f.write(i)
                    if index2 != 25:
                        f.write("\t")
        else:
            line_n = line.split("\t")
            print(line_n[0],line_n[3], line_n[7], line_n[11], line_n[15], line_n[19],
                  (line_n[23]))
            f.write(line)

    f.close()

if __name__ == '__main__':

    input_file = "Galaxy14-[Multi-Join_on_data_13_and_data_12].tabular"

    output_file = "Galaxy14-[Multi-Join_on_data_13_and_data_12]_TPM>0_1.tabular"
    TPM_value = 0.1
    file = read(input_file)
    get_TPM_values(output_file, file, TPM_value)

    #Run_Program(input_file, output_file)


