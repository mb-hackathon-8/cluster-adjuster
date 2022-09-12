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

def main(args):
    print(args)

    with open(args.srr_file):
        srr_list = [x.strip() for x in srr_file.readline()]
        


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