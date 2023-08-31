import math


def nominal_interest(interest):
    return (interest / 100) / 12


def test_number_of_months(interest=0.2, month_pay=200, principal=1000):
    nom_interest = nominal_interest(interest)
    result = math.ceil(
        math.log(month_pay / (month_pay - nom_interest * principal), 1 + nom_interest))
    assert result


def annuity_over_principal(interest=0.2, prd=200):
    nom_interest = nominal_interest(interest)
    return (math.pow(1 + nom_interest, prd) * nom_interest) / \
        (math.pow(1 + nom_interest, prd) - 1)


def test_calculated_annuity(interest=0.2, prd=200, principal=1000):
    a_over_p = annuity_over_principal(interest, prd)
    assert principal * a_over_p


def test_calculated_principal(interest=0.2, prd=200, anty=200):
    a_over_p = annuity_over_principal(interest, prd)
    assert anty / a_over_p


def runtests():
    test_number_of_months()
    test_calculated_annuity()
    test_calculated_principal()


runtests()
