import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Port scanner")

    parser.add_argument("host", type=str)
    parser.add_argument("--ports", type=str, default="1-1000")

    args = parser.parse_args()
    return args