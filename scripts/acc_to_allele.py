"""
Convert ssr to enterobase alleles 

Convert ssr to enterobase alleles 

### CHANGE LOG ###
2022-09-12 Nabil-Fareed Alikhan <nabil@happykhan.com> 
    * Initial build
"""

__licence__ = "ECL-2.0"
__author__ = "Nabil-Fareed Alikhan"
__author_email__ = "nabil@happykhan.com"
__version__ = "0.1.0"


epi = "Licence: " + __licence__ + " by " + __author__ + " <" + __author_email__ + ">"

import argparse
import time 
import os 
import traceback
import sys 
import csv

def main(args):
    print(args)
    srr_file  = args.srr_file
    with open(args.srr_file) as f:
        srr_list = [x.strip() for x in f.readlines()]
        print('Check SRR list for cgST a')
        # Check SRR list for cgST a
        samples = []
        for ent in csv.DictReader(open('scripts/entero_all.tsv'), dialect=csv.excel_tab):
            acc = ent['Data Source(Accession No.;Sequencing Platform;Sequencing Library;Insert Size;Experiment;Status)'].split(';')[0]
            if acc in srr_list:
                samples.append(ent)
        print('open profiles and fetch allele based on cgST ')
        # open profiles and fetch allele based on cgST 
        headers = [] 
        with open('scripts/profiles.list') as z : 
            headers = z.readline().split('\t')
        print('alleles')
        with open('scripts/profiles.list') as z : 
            out = open(args.output + '.tsv', 'w')
            out.write('\t'.join(headers)) 
            for line in z.readlines():
                row =   line.split('\t')
                st = row[0]
                # Write allele table to file 
                for x in samples: 
                    if x["ST"]  == st: 
                        out.write(   '\t'.join([x['Name']] + line.split('\t')[1:]))
        print('done')

if __name__ == "__main__":
    try:
        start_time = time.time()
        desc = __doc__.split("\n\n")[1].strip()
        parser = argparse.ArgumentParser(description=desc, epilog=epi)
        parser.add_argument(
            "-v", "--verbose", action="store_true", default=False, help="verbose output"
        )
        parser.add_argument(
            "--version", action="version", version="%(prog)s " + __version__
        )
        parser.add_argument(
            "-o", "--output", action="store", help="output prefix", default="my_alleles"
        )
        parser.add_argument(
            "srr_file", action="store", help="Path to SRR list"
        )
        args = parser.parse_args()
        if args.verbose:
            print("Executing @ " + time.asctime())
        main(args)
        if args.verbose:
            print("Ended @ " + time.asctime())
        sys.exit(0)
    except KeyboardInterrupt:  # Ctrl-C
        raise
    except SystemExit:  # sys.exit()
        raise
    except Exception:
        print("ERROR, UNEXPECTED EXCEPTION")
        print(traceback.print_exc())
        os._exit(1)