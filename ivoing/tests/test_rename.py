""" Tests for rename module """

from ..rename import (all_transformer, sdir_for,
                      dec_transformer, is_dec,
                      pan_transformer, is_pan,
                      trip_transformer, is_trip)

from nose.tools import assert_equal, assert_true, assert_false

def test_dec_transformer():
    assert_equal(dec_transformer('ivodec1.pdf'), 'ivodec_1.pdf')
    assert_equal(dec_transformer('Ivodec1.pdf'), 'ivodec_1.pdf')
    assert_equal(dec_transformer('ivodec12.pdf'), 'ivodec_12.pdf')
    assert_equal(dec_transformer('ivodec12.doc'), 'ivodec_12.doc')
    assert_equal(dec_transformer('id concordance.doc'),
                 'id_concordance.doc')
    assert_equal(dec_transformer('id concordance.pdf'),
                 'id_concordance.pdf')


def test_all_transformers():
    for transformer in (all_transformer,
                        dec_transformer,
                        pan_transformer,
                        trip_transformer):
        assert_equal(transformer('Not matched'), 'not_matched')
        assert_equal(transformer('SOME THING.ext'), 'some_thing.ext')


def test_is_dec():
    assert_true(is_dec('ivodec1.pdf'))
    assert_true(is_dec('Ivodec1.pdf'))
    assert_true(is_dec('ivodec_1.pdf'))
    assert_true(is_dec('ivodec_1.doc'))
    assert_true(is_dec('id_concordance.doc'))
    assert_true(is_dec('Leiden.doc'))
    assert_false(is_dec('Leiden2.doc'))
    assert_true(is_dec('idsource_1.something'))
    assert_true(is_dec('idecforw.something'))
    assert_false(is_dec('ipsource.pdf'))
    assert_false(is_dec('pan1.pdf'))
    assert_false(is_dec('pan_1.pdf'))
    assert_false(is_dec('method.pdf'))


def test_pan_transformer():
    assert_equal(pan_transformer('pan1.pdf'), 'pan_1.pdf')
    assert_equal(pan_transformer('pan1.pdf'), 'pan_1.pdf')
    assert_equal(pan_transformer('pan12.pdf'), 'pan_12.pdf')
    assert_equal(pan_transformer('pan12.doc'), 'pan_12.doc')
    assert_equal(pan_transformer('panend.doc'), 'panend.doc')
    assert_equal(pan_transformer('method.pdf'), 'method.pdf')
    assert_equal(pan_transformer('mslist.pdf'), 'mslist.pdf')
    assert_equal(pan_transformer('MSLIST.pdf'), 'mslist.pdf')
    assert_equal(pan_transformer('Conspectus.pdf'), 'conspectus.pdf')
    assert_equal(pan_transformer('Pan concordance.pdf'), 'pan_concordance.pdf') 


def test_is_pan():
    assert_true(is_pan('pan1.pdf'))
    assert_true(is_pan('pan1.pdf'))
    assert_true(is_pan('pan_1.pdf'))
    assert_true(is_pan('pan_1.doc'))
    assert_true(is_pan('METHOD.ext'))
    assert_true(is_pan('method.pdf'))
    assert_true(is_pan('MSLIST.ext'))
    assert_true(is_pan('mslist.pdf'))
    assert_true(is_pan('Conspectus.pdf'))
    assert_true(is_pan('Panend.pdf'))
    assert_true(is_pan('Pan concordance.ext'))
    assert_false(is_pan('id_concordance.doc'))
    assert_false(is_pan('Leiden.doc'))
    assert_false(is_pan('idsource_1.something'))
    assert_false(is_pan('idecforw.something'))


def test_trip_transformer():
    assert_equal(trip_transformer('tripa1.pdf'), 'trip_a_1.pdf')
    assert_equal(trip_transformer('tripab.pdf'), 'tripab.pdf') # not recognized
    assert_equal(trip_transformer('tripa1a.pdf'), 'tripa1a.pdf') # ditto
    assert_equal(trip_transformer('tripba.pdf'), 'trip_b_a.pdf')
    assert_equal(trip_transformer('tripb1.pdf'), 'tripb1.pdf') # not recognized
    assert_equal(trip_transformer('tripba1.pdf'), 'tripba1.pdf') # ditto
    assert_equal(trip_transformer('tripbb.pdf'), 'trip_b_b.pdf')
    assert_equal(trip_transformer('tripbc.pdf'), 'trip_b_c.pdf')
    assert_equal(trip_transformer('tripapref.pdf'), 'trip_a_pref.pdf')
    assert_equal(trip_transformer('tripa1cont.pdf'), 'trip_a_1_cont.pdf')
    assert_equal(trip_transformer('tripa2cont.pdf'), 'trip_a_2_cont.pdf')
    assert_equal(trip_transformer('tripbcont.pdf'), 'trip_b_cont.pdf')
    assert_equal(trip_transformer('dkmnapp.pdf'), 'dkmn_app.pdf')


def test_is_trip():
    assert_true(is_trip('tripa1.pdf'))
    assert_true(is_trip('tripab.pdf'))
    assert_true(is_trip('tripba.pdf'))
    assert_true(is_trip('tripbb.pdf'))
    assert_true(is_trip('tripbc.pdf'))
    assert_true(is_trip('trip_a_1.pdf'))
    assert_true(is_trip('trip_b_a.pdf'))
    assert_true(is_trip('trip_b_b.pdf'))
    assert_true(is_trip('trip_b_c.pdf'))
    assert_true(is_trip('tripapref.pdf'))
    assert_true(is_trip('tripa1cont.pdf'))
    assert_true(is_trip('tripa2cont.pdf'))
    assert_true(is_trip('tripbcont.pdf'))
    assert_true(is_trip('dkmnapp.pdf'))
    assert_true(is_trip('trip_a_pref.pdf'))
    assert_true(is_trip('trip_a_1_cont.pdf'))
    assert_true(is_trip('trip_a_2_cont.pdf'))
    assert_true(is_trip('trip_b_cont.pdf'))
    assert_true(is_trip('dkmn_app.pdf'))
    assert_true(is_trip('tripind.pdf'))
    assert_false(is_trip('id_concordance.doc'))
    assert_false(is_trip('Leiden.doc'))
    assert_false(is_trip('idsource_1.something'))
    assert_false(is_trip('idecforw.something'))
    assert_false(is_trip('METHOD.ext'))
    assert_false(is_trip('method.pdf'))
    assert_false(is_trip('MSLIST.ext'))
    assert_false(is_trip('mslist.pdf'))


def test_sdir_for():
    assert_equal(sdir_for('trip_a_1.pdf'), 'tripartita')
    assert_equal(sdir_for('pan1.pdf'), 'panormia')
    assert_equal(sdir_for('method.pdf'), 'panormia')
    assert_equal(sdir_for('leiden.pdf'), 'decretum')
    assert_equal(sdir_for('ivodec1.pdf'), 'decretum')
    assert_equal(sdir_for('funny_thing_way_to_forum.pdf'), None)
