class BalanceException(Exception):
    pass

# 1. way
# def checkbalance():
#     money = 10000
#     withdraw = 9000
#     try:
#         balance = money - withdraw
#         if balance <= 2000:
#             raise BalanceException("Insufficient Balance")
#         print(balance)
#     except BalanceException as e:
#         print(e)
# checkbalance()

# 2. way
def checkbalance():
    money = 10000
    withdraw = 9000
    balance = money - withdraw
    if balance <= 2000:
        raise BalanceException("Insufficient Balance")
    print(balance)

try:
    checkbalance()
except BalanceException as e:
        print(e)