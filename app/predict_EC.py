import os
import time
import subprocess

file_path = "/home/selina/ncbi_dataset/fetch.txt"
data_path = "/home/selina/Bacteria/ncbi_dataset/data/"

train_data = "split100"
test_data =  ["price", "protein", "protein_000154345"] # GCA_000144625.1

'''
parse the filename from fetch.txt, and append them to test_data.
data/GCA_000154505.1/protein.faa -> GCA_000154505.1 
'''

# test_data = []
# with open(file_path, "r") as f:
#     while (1):
#         line = f.readline()
#         # If the line is empty, break out of the loop (end of file reached)
#         if not line:
#             break
        
#         parsed_elements = line.split()
#         test_data.append( parsed_elements[2].split('/')[1] )  # data/GCA_000007745.1/protein.faa

'''
the targets [ data_path/GCA_000154505.1/protein.faa ] need to be placed at app/data/inputs/*.fasta as the usage of CLEAN
create symbolic link instead of copy raw data in consider of the data size
'''
# for data in test_data:
#     os.symlink(data_path + data + "/protein.faa", './data/inputs/'+ data + ".fasta")

for item in test_data:
    clean_script = "CLEAN_infer_fasta.py"
    command = ["python", clean_script, "--fasta_data", item]
    subprocess.run(command)
