import re
def correct(file):
    with open(file) as f:
        with open("output.txt","w") as nf:
            # Buffer holds a sentence that has not finished yet and needs an ending
            buffer = ""

            # Replace soft hyphens with normal hyphens
            for line in f.readlines():
                line = line.replace('\xc2\xad', '-')

                # Write titles seperate from the rest of the text
                title = re.search('', line)
                if title:
                    nf.write("\n" + buffer + "\n")
                    nf.write("\n" + line)
                    buffer = ""

                else:
                    # If the last character in the line is a hyphen, remove it together with the end line token
                    if len(line) > 3 and line[-2] == "-":
                        line = line[:-2]

                    # Find words that indicate the end of a sentence *. and write them together with the built up buffer.
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