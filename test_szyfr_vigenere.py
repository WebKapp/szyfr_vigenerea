from szyfr_vigenere import generate_table, generate_password, encrypt_vigenere
from szyfr_vigenere import decrypt_vigenere, is_key_empty, is_letters_not_okay
import string
import pytest


def test_is_key_okay_False():
    assert is_key_empty('Kacper') is False


def test_is_key_okay_True():
    assert is_key_empty('') is True


def test_is_letters_not_okay_False():
    assert is_letters_not_okay('HALINA MALINA') is False


def test_is_letters_not_okay_True():
    assert is_letters_not_okay('Hacperek') is True


def test_generate_table():
    alphabet = list(string.ascii_uppercase)
    assert generate_table()[0] == alphabet


def test_generate_password_standard():
    output = 'TRUMPT RU MPTR'
    assert ''.join(generate_password('KACPER MA KOTA', 'TRUMP')) == output


def test_generate_password_empty_key():
    with pytest.raises(ValueError):
        ''.join(generate_password('POLITECHNIKA', ''))


def test_generate_password_wrong_key():
    with pytest.raises(ValueError):
        ''.join(generate_password('POLITECHNIKA', 'KlUcz44'))


def test_generate_password_wrong_text():
    with pytest.raises(ValueError):
        ''.join(generate_password('wARSZawA99', 'KLUCZ'))


def test_generate_password_both_values_wrong():
    with pytest.raises(ValueError):
        ''.join(generate_password('PolSKA89', 'PrAWda'))


def test_encrypt_vigenere_standard():
    assert encrypt_vigenere('TRUMP', 'KACPER MA KOTA') == 'DRWBTK DU WDMR'
    assert encrypt_vigenere('POLIBUDA', 'KOCHAM PIPR') == 'ZCNPBG SIEF'


def test_encrypt_vigenere_empty_key():
    with pytest.raises(ValueError):
        encrypt_vigenere('', 'POLITECHNIKA')


def test_encrypt_vigenere_wrong_value_of_key():
    with pytest.raises(ValueError):
        encrypt_vigenere('POliTechniKa', 'KACPERRO')


def test_encrypt_vigenere__wrong_value_of_text():
    with pytest.raises(ValueError):
        encrypt_vigenere('KLUCZYK', 'POLITECHnika')


def test_encrypt_vigenere__both_values_wrong():
    with pytest.raises(ValueError):
        encrypt_vigenere('klucZyk', 'POLITECHnika')


def test_encrypt_vigenere_empty_text():
    assert encrypt_vigenere('KLUCZ', '') == ''


def test_decrypt_vigenere_standard():
    assert decrypt_vigenere('TRUMP', 'DRWBTK DU WDMR') == 'KACPER MA KOTA'


def test_decrypt_vigenere_empty_key():
    with pytest.raises(ValueError):
        decrypt_vigenere('', 'POLITECHNIKA')


def test_decrypt_vigenere_wrong_value_of_key():
    with pytest.raises(ValueError):
        decrypt_vigenere('POliTechniKa', 'KACPERRO')


def test_decrypt_vigenere__wrong_value_of_text():
    with pytest.raises(ValueError):
        decrypt_vigenere('KLUCZYK', 'POLITECHnika')


def test_decrypt_vigenere__both_values_wrong():
    with pytest.raises(ValueError):
        decrypt_vigenere('klucZyk', 'POLITECHnika')
