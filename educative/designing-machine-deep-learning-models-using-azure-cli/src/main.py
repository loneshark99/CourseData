import os
import argparse
import pandas as pd

def main(args):
    df = pd.read_csv(args.titanic_csv)
    os.makedirs("output", exist_ok=True)
    df.to_csv("output/titanic.csv", index=False)

def parse_args():
    # setup arg parser
    parser = argparse.ArgumentParser()

    # add arguments
    parser.add_argument("--titanic-csv", type=str)

    # parse args
    args = parser.parse_args()

    # return args
    return args


# run script
if __name__ == "__main__":
    # parse args
    args = parse_args()

    # run main function
    main(args)
