def validate_transaction(user, transaction):
  balance = user.bank.get_balance()
  cost = transaction.current_total_value()
  if balance >= cost:
    return True
  else:
    return False
