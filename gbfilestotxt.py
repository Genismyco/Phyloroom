### THIS is working
	
from sys import argv

input = argv[1]
output = argv[2]

import pip
import os

try:
    import Bio
except ImportError:
    os.system('pip install biopython')
	
try:
    import Scipy
except ImportError:
    os.system('pip install scipy')
	
try:
    import numpy
except ImportError:
    os.system('pip install numpy')
	
from Bio import SeqIO
import os

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
                    ofile.write(">{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\n".format(seq_record.annotations["organism"], 
                    seq_record.name, strain, country, isolation_source, host, 
                    len(seq_record), seq_record.annotations['references'][0].authors, 
                    seq_record.annotations['references'][0].title, seq_record.annotations['references'][0].journal, 
                    seq_record.seq))
                    
else:
    print ("The output file already seem to exist in the current working directory {0}. Please change the name of the output file".format(os.getcwd())) #error msg