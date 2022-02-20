from battle_stocks.classes.bank import Bank

def test_withdraw():
  bank = Bank()
  bank.withdraw(489.50)
  expected = 9510.50
  assert bank.get_balance() == expected

def test_withdraw_too_much():
  bank = Bank()
  bank.withdraw(20000)
  expected = 10000
  assert bank.get_balance() == expected

def test_deposit():
  bank = Bank()
  bank.deposit(455.68)
  expected = 10455.68
  assert bank.get_balance() == expected

def test_deposit():
  
