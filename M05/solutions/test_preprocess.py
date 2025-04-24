# -*- coding: utf-8 -*-

from M05L08 import preprocess_review

def test_method_lower():
    review = "ABCDEF"
    got = preprocess_review(review)
    expected = ["abcdef"]
    assert got == expected

def test_method_replace():
    review = "abcde<br />fgh"
    got = preprocess_review(review)
    expected = ['abcde', 'fgh']
    assert got == expected


def test_method_split():
    review = "one\n two    three    four"
    got = preprocess_review(review)
    expected = ['one', 'two', 'three', 'four']
    assert got == expected
