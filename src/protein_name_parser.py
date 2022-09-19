"""
Author: Gijsbert Keja
This file parses the gennames given in a .txt file and writes
the gennames to a new file
"""

def main(chr_file, chr_output):
    list_without_duplicates = file_reader_splitter(chr_bestand)
    file_writer(chr_output, list_without_duplicates)

def file_reader_splitter(chr_file):
    """
    This file parses the file with the gene names and also removes the
    duplicates
    :param chr_bestand: This is the name of the file which needs to be read
    :type chr_bestand: str
    :return: lijst_without_duplicates
    :rtype: list
    """
    chr_read = open(chr_file, 'r')
    list_with_duplicates = []
    list_without_duplicates = []
    for x in chr_read:
        if x.startswith('>'): # 
            line = x.split("|") 
            line2 = line[2].split()
            position_genename = len(line2) - 3 # The recurring position of the name of the gene is 3 to the left from the back
            genename = line2[position_genename]
            gene = genename.split("=") # the gene name contains a "=" so this needs to be removed 
            list_with_duplicates.append(gene[1])
    list_without_duplicates = list(set(list_with_duplicates)) # the duplicates will be removed by using a set
    return list_without_duplicates

def file_writer(chr_output, list_without_duplicates):
    """
    :param chr_output: This is the name of the file which needs to be created
    :type chr_output: str
    :param lijst_zonder_duplicates: this is a list with all gene names
    :type lijst_zonder_duplicates: list
    :return: N/A
    :rtype: N/A
    """
    new_file = open(chr_output, "w")
    for x in list_without_duplicates:
        new_file.write(x)
        new_file.write("\n") # the \n will make sure that there are enters after the strings

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])




