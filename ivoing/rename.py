""" Renaming files from original scheme to web-page scheme

General rule is to change all filenames to lower case, separate meaningful
suffixes with underscores, put all numbers after an underscore.
"""

from os.path import splitext
import re


def all_transformer(in_base):
    return in_base.replace(' ', '_').lower()


def dec_transformer(in_base):
    in_base = all_transformer(in_base)
    root, ext = splitext(in_base)
    match = re.match(r'(ivodec)(\d+)', root)
    if not match is None:
        return '{0}_{1}'.format(*match.groups()) + ext
    return in_base


def is_dec(in_base):
    out_dec = dec_transformer(in_base)
    if out_dec.startswith('id'):
        return True
    if out_dec.startswith('ivodec'):
        return True
    root, ext = splitext(out_dec)
    if root == 'leiden':
        return True
    return False


def pan_transformer(in_base):
    in_base = all_transformer(in_base)
    root, ext = splitext(in_base)
    match = re.match(r'(pan)(\d+)', root)
    if not match is None:
        return '{0}_{1}'.format(*match.groups()) + ext
    return in_base


def is_pan(in_base):
    out_pan = pan_transformer(in_base)
    if out_pan.startswith('pan'):
        return True
    root, ext = splitext(out_pan)
    if root in ('method', 'mslist', 'conspectus'):
        return True
    return False


def trip_transformer(in_base):
    in_base = all_transformer(in_base)
    root, ext = splitext(in_base)
    if root.startswith('tripa'):
        suffix = root[5:]
        if suffix == 'pref':
            return 'trip_a_pref' + ext
        elif suffix[0] in ('1234'):
            digit, suffix = suffix[0], suffix[1:]
            if suffix == '':
                return 'trip_a_{0}{1}'.format(digit, ext)
            elif suffix == 'cont':
                return 'trip_a_{0}_cont{1}'.format(digit, ext)
    elif root.startswith('tripb'):
        suffix = root[5:]
        if suffix == 'cont':
            return 'trip_b_cont' + ext
        elif suffix[0] in ('abcde'):
            letter = suffix[0]
            suffix = suffix[1:]
            if suffix == '':
                return 'trip_b_{0}{1}'.format(letter, ext)
    elif root == 'dkmnapp':
        return 'dkmn_app' + ext
    return in_base


def is_trip(in_base):
    out_trip = trip_transformer(in_base)
    if out_trip.startswith('trip'):
        return True
    root, ext = splitext(out_trip)
    if root == 'dkmn_app':
        return True
    return False


def sdir_for(in_base):
    if is_dec(in_base):
        return 'decretum'
    elif is_pan(in_base):
        return 'panormia'
    elif is_trip(in_base):
        return 'tripartita'
    return None
