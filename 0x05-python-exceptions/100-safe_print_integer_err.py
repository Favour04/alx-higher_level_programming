#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    results = None
    try:
        print("{:d}".format(value))
        results = True
    except Exception as err:
        print(f"Exception: {err}", file=sys.stderr)
        results = False
    finally:
        return results
