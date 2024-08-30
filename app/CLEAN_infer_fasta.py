import argparse
import os
import time
from CLEAN.utils import *
from CLEAN.infer import infer_maxsep

def eval_parse():
    # only argument passed is the fasta file name to infer
    # located in ./data/[args.fasta_data].fasta
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--fasta_data', type=str)
    args = parser.parse_args()
    return args


def main():
    args = eval_parse()
    train_data = 'split100'
    test_data = 'inputs/' + args.fasta_data 
    # converting fasta to dummy csv file, will delete after inference
    # esm embedding are taken care of
    prepare_infer_fasta(test_data) 
    # inferred results is in
    # results/[args.fasta_data].csv
    start_time = time.time()
    infer_maxsep(train_data, test_data, report_metrics=False, pretrained=True, gmm = './data/pretrained/gmm_ensumble.pkl')
    print("--- %s seconds ---" % (time.time() - start_time)) #debug
    
    # removing dummy csv file
    os.remove("data/"+ test_data +'.csv')
    

if __name__ == '__main__':
    main()
