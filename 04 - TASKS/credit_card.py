def f(card_number):
    coded = card_number[:2] + '*' * 10 + card_number[-4:]
    print(coded)

