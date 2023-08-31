import math


def nominal_interest(interest):
    return (interest / 100) / 12


def number_of_months(interest, month_pay, principal):
    nom_interest = nominal_interest(interest)
    return math.ceil(math.log(month_pay / (month_pay - nom_interest * principal), 1 + nom_interest))


def annuity_over_principal(interest, prd):
    nom_interest = nominal_interest(interest)
    return (math.pow(1 + nom_interest, prd) * nom_interest) / (math.pow(1 + nom_interest, prd) - 1)


def calculated_annuity(interest, prd, principal):
    a_over_p = annuity_over_principal(interest, prd)
    return principal * a_over_p


def calculated_principal(interest, prd, anty):
    a_over_p = annuity_over_principal(interest, prd)
    return anty / a_over_p


print("What do you want to calculate?")
print("type \"n\" for number of monthly payments,")
print("type \"a\" for annuity monthly payment amount,")
print("type \"p\" for the loan principal:")
option = input()

if option == 'n' or option == 'a':
    print("Enter the loan principal:")
    principal = int(input())
    if option == 'a':
        print("Enter the number of periods:")
        period = int(input())
        print("Enter the loan interest:")
        interest = float(input())
        print("Your monthly payment = " +
              str(math.ceil(calculated_annuity(interest, period, principal))) + "!")
    else:
        print("Enter the monthly payment:")
        monthly_payment = int(input())
        print("Enter the loan interest:")
        interest = float(input())
        num_of_mnths = number_of_months(interest, monthly_payment, principal)
        years = math.floor(num_of_mnths / 12)
        months = num_of_mnths % 12
        if months == 0:
            print("It will take", years, "years to repay this loan!")
        elif months > 0:
            print("It will take", years, "years and",
                  months, "months to repay this loan!")
elif option == 'p':
    print("Enter the annuity payment:")
    annuity = float(input())
    print("Enter the number of periods:")
    period = int(input())
    print("Enter the loan interest:")
    interest = float(input())
    print("Your loan principal = " +
          str(int(round(calculated_principal(interest, period, annuity), 0))) + "!")
