import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Port scanner")

    parser.add_argument("host", type=str)
    parser.add_argument("--ports", type=str, default="1-1000")
    parser.add_argument("--filter", type=str, default="none", choices=["none","open", "closed","filtered"])
    parser.add_argument("--timeout", type=int, default=1)
    args = parser.parse_args()
    return args