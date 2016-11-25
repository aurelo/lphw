from nose.tools import *
from source.ex48 import lexicon


def setup():
    print "SETUP!"


def teardown():
    print "TEAR DOWN!"


def test_basic():
    print "I RAN!"


def test_directions():
    assert_equal(lexicon.scan("north"), [("direction", "north")])
    result = lexicon.scan("north south east")
    assert_equal(result, [('direction', 'north'),
                          ('direction', 'south'),
                          ('direction', 'east')])


def test_verbs():
    assert_equal(lexicon.scan('go'), [('verb', 'go')])
    result = lexicon.scan("go kill EAT")
    assert_equals(result, [('verb', 'go'),
                           ('verb', "kill"),
                           ('verb', "EAT")])


def test_stops():
    assert_equals(lexicon.scan('the'), [('stop', 'the')])
    result = lexicon.scan("the in of")
    assert_equals(result, [('stop', 'the'),
                           ('stop', 'in'),
                           ('stop', 'of')])


def test_nouns():
    assert_equals(lexicon.scan("bear"), [('noun', 'bear')])
    result = lexicon.scan("bear princess")
    assert_equals(result, [('noun', 'bear'),
                           ('noun', 'princess')])


def test_number():
    assert_equals(lexicon.scan('1234'), [('number', '1234')])
    result = lexicon.scan('3 91234')
    assert_equals(result, [('number', '3'),
                           ('number', '91234')])


def test_errors():
    assert_equals(lexicon.scan('ASDFADFASDF'), [('error', 'ASDFADFASDF')])


def test_sentence():
    result = lexicon.scan('go north and kill the bear 9 times')
    assert_equals(result, [('verb', 'go'),
                           ('direction', 'north'),
                           ('stop', 'and'),
                           ('verb', 'kill'),
                           ('stop', 'the'),
                           ('noun', 'bear'),
                           ('number', '9'),
                           ('error', 'times')])
