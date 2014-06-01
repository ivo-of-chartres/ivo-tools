#!/usr/bin/env python
""" Rename ivo files in a directory """
from __future__ import print_function

import os
from os.path import join as pjoin, isdir
import shutil
import argparse

from ivoing import rename

DIR2FUNC = dict(
    decretum=rename.dec_transformer,
    panormia=rename.pan_transformer,
    tripartita=rename.trip_transformer)

def main():
    parser = argparse.ArgumentParser(description='Rename Ivo files.')
    parser.add_argument('in_dir',
                    help='directory to process')
    parser.add_argument('--out-dir',
                        default=os.getcwd(),
                        help='output directory (default is current directory)')
    args = parser.parse_args()
    in_dir = args.in_dir
    out_dir = args.out_dir
    for dirpath, dirnames, filenames in os.walk(in_dir):
        for fbase in filenames:
            full_path = pjoin(dirpath, fbase)
            out_sdir = rename.sdir_for(fbase)
            if out_sdir is None:
                print('Skipping', full_path)
                continue
            new_dir = pjoin(out_dir, out_sdir)
            if not isdir(new_dir):
                os.mkdir(new_dir)
            new_base = DIR2FUNC[out_sdir](fbase)
            new_path = pjoin(new_dir, new_base)
            print('Copying', full_path, 'to', new_path)
            shutil.copyfile(full_path, new_path)


if __name__ == '__main__':
    main()
