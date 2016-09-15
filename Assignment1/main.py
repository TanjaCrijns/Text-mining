import re
def correct(file):
    with open(file) as f:
        with open("output.txt","w") as nf:
            buffer = ""
            for line in f.readlines():
                line = line.replace('\xc2\xad', '-')
                title = re.search('', line)
                if title:
                    nf.write("\n" + buffer + "\n")
                    nf.write("\n" + line)
                    buffer = ""
                else:
                    if len(line) > 3 and line[-2] == "-":
                        line = line[:-2]
                    end = re.search('\w+\.' , line)
                    if end and len(end.group(0)) > 2:
                        words = line.split()
                        try:
                            linetw = words[:words.index(end.group(0))+1]
                            nf.write(buffer + " " + " ".join(linetw)+ "\n")
                            buffer = " ".join(words[words.index(end.group(0))+1:])
                        except:
                            buffer+= " " + line[:-1] if len(buffer) > 0 else line[:-1]


                    else:
                        buffer+= " " + line[:-1] if len(buffer) > 0 else line[:-1]

if __name__ == "__main__":
    correct("input.txt")