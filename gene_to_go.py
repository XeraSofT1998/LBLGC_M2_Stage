

def read(path):
    content = []
    f = open(path, 'r')
    for line in f.readlines():
        content.append(line)
    f.close()
    return content

def write(path, content):
    f = open(path, "w")
    for line in content:
        f.write(line)
    f.close()

def reform(content):
    new_content = []
    for line in content :
        line = (".".join(line.split("\t")[2].split(".")[0:2]) + "\t" + line.split("\t")[-3]).replace(" ", ", ") + "\n"
        new_content.append(line)
    print(new_content)
    return new_content


path = "Ptrichocarpa_533_v4.1.annotation_info.txt"
output = "Gene2GO.txt"
write(output, reform(read(path)))