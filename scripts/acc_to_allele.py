import time 
import os 



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
            "-o", "--output", action="store", help="output prefix", default="summary.tsv"
        )
        parser.add_argument(
            "app_dir", action="store", help="Path to directory of applications docx"
        )
        args = parser.parse_args()
        if args.verbose:
            print("Executing @ " + time.asctime())
        main()
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