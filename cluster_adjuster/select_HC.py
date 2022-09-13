# -*- coding: utf-8 -*-
"""

"""


import os
import argparse

import pandas as pd


input_file = '/home/rmamede/Desktop/Hackathon/spyogenes/HierCC_wgMLST/wgMLST_hcceval.tsv'
output_directory = '/home/rmamede/Desktop/Hackathon/test_select'
silhouette_threshold = 0.9
def main(input_file, output_directory, silhouette_threshold):

    # create output_directory
    if os.path.isdir(output_directory) is False:
        os.mkdir(output_directory)

    with open(input_file, 'r') as infile:
        lines = infile.readlines()
    
    silhouette_lines = [line.strip() for line in lines if '#Silhouette' in line]
    silhouette_lists = [line.split('\t') for line in silhouette_lines]
    silhouette_values = {line[1]:float(line[2]) for line in silhouette_lists}

    # select the HC at the start of each block
    block_starts_hcs = []
    in_block = False
    for k, v in silhouette_values.items():
        if v >= silhouette_threshold and in_block is False:
            block_starts_hcs.append(k)
            in_block = True
        elif v <= silhouette_threshold and in_block is True:
            in_block = False

    print('HC at start of each block for silhouette >= {0}: {1}'.format(silhouette_threshold, ','.join(block_starts_hcs)))

    # select the NMI
    # nmi_index = lines.index([line for line in lines if '#NMI' in line][0])
    # nmi_lines = lines[nmi_index:]
    # nmi_lines = [line.strip()]
    # nmi_df = pd.DataFrame(nmi_lines, separator='\t')



def parse_arguments():

    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('-i', '--input-file', type=str,
                        required=True, dest='input_file',
                        help='')

    parser.add_argument('-o', '--output-directory', type=str,
                        required=True, dest='output_directory',
                        help='')

    args = parser.parse_args()

    return args


if __name__ == "__main__":

    args = parse_arguments()
    main(**vars(args))
