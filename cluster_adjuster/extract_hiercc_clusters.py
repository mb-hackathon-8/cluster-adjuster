# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import os
import argparse

import pandas as pd


def main(input_file, output_directory, metadata_table, columns):

    # create output_directory
    if os.path.isdir(output_directory) is False:
        os.mkdir(output_directory)

    hiercc_matrix = pd.read_csv(input_file, delimiter='\t', index_col=0)
    sample_ids = hiercc_matrix.index.tolist()
    hc_cuts = hiercc_matrix.columns.tolist()

    if metadata_table is not None:
        metadata = pd.read_csv(metadata_table, delimiter='\t', index_col=0, dtype=str)

    if metadata_table is not None:
        headers = '\t'.join(['Cluster', 'Samples'] + columns)
    else:
        headers = '\t'.join(['Cluster', 'Samples'])
    for c in hc_cuts:
        current_hc = hiercc_matrix[c]
        hc_clusters = list(current_hc.groupby(current_hc))
        hc_clusters = {c[0]: list(c[1].index) for c in hc_clusters}

        # get metadata counts/percentage
        if metadata_table is not None:
            clusters_metadata = {}
            for cid, csamples in hc_clusters.items():
                for category in columns:
                    metadata_counts = metadata[category][csamples].value_counts()
                    metadata_line = ','.join(['{0}({1})'.format(i, metadata_counts[i]) for i in metadata_counts.index])
                    clusters_metadata.setdefault(cid, []).append(metadata_line)

        # save file with clusters
        hc_output_file = os.path.join(output_directory, '{0}_clusters.tsv'.format(c))
        hc_lines = [headers]
        if metadata_table is not None:
            hc_lines += ['{0}\t{1}\t{2}'.format(k, ','.join(v), '\t'.join(clusters_metadata[k])) for k, v in hc_clusters.items()]
        else:
            hc_lines += ['{0}\t{1}'.format(k, ','.join(list(map(str, v)))) for k, v in hc_clusters.items()]
        with open(hc_output_file, 'w') as outfile:
            outfile.write('\n'.join(hc_lines)+'\n')


def parse_arguments():

    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('-i', '--input-file', type=str,
                        required=True, dest='input_file',
                        help='')

    parser.add_argument('-o', '--output-directory', type=str,
                        required=True, dest='output_directory',
                        help='')

    parser.add_argument('-m', '--metadata_table', type=str,
                        required=False, dest='metadata_table',
                        help='')

    parser.add_argument('-c', '--columns', type=str, nargs='+',
                        required=False, dest='columns',
                        help='')

    args = parser.parse_args()

    return args


if __name__ == "__main__":

    args = parse_arguments()
    main(**vars(args))
