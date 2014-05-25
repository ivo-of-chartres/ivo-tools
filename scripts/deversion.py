#!/usr/bin/env python
""" Remove file-name versioning now we're in git """
from __future__ import print_function

from os.path import join as pjoin, split as psplit, abspath, dirname
import os
import re
import shutil

path_re = re.compile(r'(\w+)_\dp\d.pdf')
href_re = re.compile(r'<a href="(\w+)/(\w+)_\dp\d.pdf">')

EXAMPLE = '<a href="decretum/idecforw_1p4.pdf">'
EXAMPLE2 = '<a href="decretum/leiden_1p4.pdf">'

print(href_re.sub(r'<a href="\1/\2.pdf">', EXAMPLE))
print(href_re.match(EXAMPLE2).groups())

for dirpath, dirnames, filenames in os.walk('.'):
    fname_matches = {}
    for fname in filenames:
        fpath = pjoin(dirpath, fname)
        if fname.endswith('.html'):
            with open(fpath, 'rt') as fobj:
                lines = fobj.readlines()
            with open(fpath, 'wt') as fobj:
                for line in lines:
                    line = href_re.sub(r'<a href="\1/\2.pdf">', line)
                    fobj.write(line)
            continue
        if path_re.match(fname):
            new_fname = path_re.sub(r'\1.pdf', fname)
            if new_fname in fname_matches:
                fname_matches[new_fname].append(fname)
            else:
                fname_matches[new_fname] = [fname]
    for new_fname, matches in fname_matches.items():
        matches.sort()
        print("Checking", new_fname)
        print("Matches are:")
        print('\n'.join(matches))
        old_fpath = pjoin(dirpath, matches[-1])
        new_fpath = pjoin(dirpath, new_fname)
        print("Copying {0} as {1}".format(old_fpath, new_fpath))
        shutil.copyfile(old_fpath, new_fpath)
