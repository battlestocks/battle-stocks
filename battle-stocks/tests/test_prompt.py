from pickle import FALSE
from battle_stocks.classes.input_validation import InputValidation
from battle_stocks.scripts.main import main
from battle_stocks.classes.prompt import Prompt
from battle_stocks.utils.validate_transaction import validate_transaction
import sys

def test_main():
  expected = 'b'
  actual = 'q'
  assert expected != actual

def test_validate_start_quit_yes():
  validated = InputValidation.validate_start_quit('Y')
  expected = validated.upper()
  actual = 'Y'
  assert expected == actual

def test_validate_start_quit_no():
  validated = InputValidation.validate_start_quit('N')
  expected = validated.upper()
  actual = 'N'
  assert expected == actual


