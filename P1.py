### Problema 1 Calcular el credit card penalty for paying late.
def credit_card_penalty(ccb, ndl): ###ccb = credit_card_balance, ndl = numbers_days_late
    if ndl < 15:
        penalty = ccb * 0.05
    elif ndl >= 15 and ndl <= 30:
        penalty = ccb * 0.10
    elif ndl >=30 and ndl <= 60:
        penalty = ccb * 0.15
    else:
        penalty = ccb * 0.20
    return penalty

print "Penalty 1:  $", credit_card_penalty(15000, 18)

print "Penalty 2:  $", credit_card_penalty(7000, 31)

print "Penalty 3:  $", credit_card_penalty(300, 70)

print "Penalty 4:  $", credit_card_penalty(1000, 3)