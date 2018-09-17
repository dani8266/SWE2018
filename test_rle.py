from rle import rle_encoder
from rle import rle_decoder
import sys
from hypothesis import given, settings
from hypothesis.strategies import text

def test_simple():
    assert rle_encoder("bbbkkk") == "b3k3"
def test_advanced():
    assert rle_encoder("ffffiiiii") == "f4i5"

def test_decoder():
    assert rle_decoder("b3k3") == "bbbkkk"
def test_advanced_decoder():
    assert rle_decoder("b3k3o9i5") == "bbbkkkoooooooooiiiii"

def test_advanced_failure():
    assert rle_encoder("0000000000:") == "010:1"
def test_advanced2():
    assert rle_decoder("010:1") == "0000000000:"

@given(text())
@settings(max_examples=5000)
def test_hypo(x):
    #print x
    assert rle_decoder(rle_encoder(x)) == x
