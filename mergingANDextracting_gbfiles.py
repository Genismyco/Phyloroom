# juntos os arquivos em um só, altere antes a extensão para .txt OK https://stackoverflow.com/questions/13613336/python-concatenate-text-files
import os
All_GBfiles = 'E:/Python/room/All_GBfiles.gb'

def concatFiles():
    path = 'E:/Python/room/gb/' #define o diretório para pegar todos os arquivos que haja nele
    files = os.listdir(path)
    for idx, infile in enumerate(files):
        print ("File #" + str(idx) + "  " + infile)
    concat = ''.join([open(path + f).read() for f in files])
    with open(All_GBfiles, "w") as fo:
        fo.write(concat)

if __name__ == "__main__":
    concatFiles()
	
#extrair todas as infos OK
from Bio import SeqIO
import os
input = All_GBfiles
output = "E:/Python/room/Alldata.txt"

handle = open(input)

if not os.path.exists(output): #checks for a pre-existing file with the same name as the output
    for seq_record in SeqIO.parse(handle, "genbank"): # parse = pesquisar/analisar
        for seq_feature in seq_record.features:
            if seq_feature.type=="source":
                try: #If you would like your script to run to completion even when that information is not present, you can wrap each access to seq_feature.qualifiers in a try-except block catching KeyError and IndexError
                    strain = seq_feature.qualifiers.get('strain')
                except (KeyError, IndexError):
                    strain = None
                try:
                    country = seq_feature.qualifiers.get('country')
                except (KeyError, IndexError):
                    country = None
                try:
                    isolation_source = seq_feature.qualifiers.get('isolation_source')
                except (KeyError, IndexError):
                    isolation_source = None
                try:
                    host = seq_feature.qualifiers.get('host')
                except (KeyError, IndexError):
                    host = None
                with open(output, "a") as ofile:
                    ofile.write(">{0}xxx{1}xxx{2}xxx{3}xxx{4}xxx{5}xxx{6}xxx{7}xxx{8}xxx{9}xxx{10}zzz\n".format(seq_record.annotations["organism"], 
                    seq_record.name, strain, country, isolation_source, host, 
                    len(seq_record), seq_record.annotations['references'][0].authors, 
                    seq_record.annotations['references'][0].title, seq_record.annotations['references'][0].journal, 
                    seq_record.seq))
                    
else:
    print ("The output file already seem to exist in the current working directory {0}. Please change the name of the output file".format(os.getcwd())) #error msg
#
# Python code to remove duplicate elements OK

none_duplicate = "E:/Python/room/none_duplicate.txt"
 
def Remove(duplicate): # https://www.geeksforgeeks.org/python-remove-duplicates-list/
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list

# Driver Code 
duplicate = open(output) #https://qiita.com/visualskyrim/items/1922429a07ca5f974467

import sys
sys.stdout=open(none_duplicate,"w") #https://stackoverflow.com/questions/7152762/how-to-redirect-print-output-to-a-file-using-python/38186276
print(Remove(duplicate))
sys.stdout.close()