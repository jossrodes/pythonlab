# -*- coding: utf-8 -*-
from hypothesis import given, example
from hypothesis.strategies import text


@given(text())
@example(5,10)
def test_lowerup(lower,upper):
    assert lower_up_while(lower,upper) == lower_up_while(lower, upper)


@given(text())
@example(['computer', 'software', 'python'],5)
def test_word_filter(lower,upper):
    assert word_filter(lower,upper) == word_filter_2(lower, upper)


@given(text())
@example('test')
def test_word_filter(l):
    assert string_length(l) == string_length2(l)


@given(text())
@example('murcielago')
def test_is_vocal(l):
    assert is_vocal2(l) == is_vocal(l)
