import re, datetime
def sentences(file):
    with open(file) as f:
        with open("sentences" + file ,"w") as nf:
            for line in f.readlines():
                line = re.sub(r'(\S{3,}\.)' , r'\1\n', line)
                remwhitesp = re.sub('\n\s', '\n', line)
                nf.write(remwhitesp)

def gettimeline(file):
    table = []
    sortedtable = []
    with open("sentences" + file) as f:
        months = "(January|February|March|April|May|June|July|August|September|October|November|December)"
        # Example: January, 1994, 1
        pattern1 = months + "\W{1,2}\d{4}\W{1,2}\d{1,2}"
        # Example:  January, 1, 1994
        pattern2 = months + "\W{1,2}\d{1,2}\W{1,2}\d{4}"
        # Example:  January, 1994
        pattern3 = months + "\W{1,2}\d{4}"
        # Example:  1994
        pattern4 = "\d{4}"

        for line in f.readlines():
            expression = pattern1 + "|" + pattern2+ "|" +pattern3 + "|"+pattern4
            matches = re.finditer(expression, line)
            if matches:
                for match in matches:
                    table.append([rewritedate(match.group(0), False), line])
                    sortedtable.append([rewritedate(match.group(0), True), line])

        with open("timeline" + file, "w") as f:
            for tuple in sorttable(table, sortedtable):
                f.write(tuple[0] + ":\t" + tuple[1])

        with open("unsortedtimeline" + file, "w") as f:
            for tuple in sorttable(table, table):
                f.write(tuple[0] + ":\t" + tuple[1])

def rewritedate(string, sort):
    months = "(January|February|March|April|May|June|July|August|September|October|November|December)"
    monthnumbers = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    year = re.search('\d{4}', string)
    month = re.search(months, string)
    day = re.search('\d{1,2}\W+', string)

    if month:
        if  month.group(0) != "October" and month.group(0) != "November" and month.group(0) != "December":
            monthnumber = "0" + str(monthnumbers.index(month.group(0))+1)
        else:
            monthnumber = str(monthnumbers.index(month.group(0))+1)

    if day:
        # extra iteration so that 2013 isn't found as a day 20
        day = re.search('\d{1,2}', day.group(0))
        if len(day.group(0)) < 2:
            daynumber = "0" + day.group(0)
        else:
            daynumber = day.group(0)

    if year and month and day:
        return year.group(0) + "-" + monthnumber  + "-" + daynumber
    elif year and month:
        return year.group(0) + "-" + monthnumber if not sort else year.group(0) + "-" + month.group(0)
    else:
        return year.group(0) if not sort else year.group(0)

def sorttable(table,sortedtable):
    temp = zip(table,sortedtable)
    finaltable = sorted(temp, key=lambda x: x[1][0])
    table, sortedtable = zip(*finaltable)
    return table

if __name__ == "__main__":
    name = "tatiana"
    # get all sentences from text
    sentences(name + ".txt")
    # get the timeline from the sentences
    gettimeline(name + ".txt")