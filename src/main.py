#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------- #
# Created By: Uribe
# Created Date: 28/4/23
# --------------------------------------------------------------------------- #
# ** Description **
""""""

# Standard Library Imports
# --------------------------------------------------------------------------- #
# ** Required libraries **
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("word")
    args = parser.parse_args()
    word = args.word
    print(word)
