#This is a simple compound interest calculator for an investment account with a monthly contribution.
import random

def get_initial_amount():
    while True:
        amount = input("Enter your initial amount. Please round to nearest integer: $")
        if amount.isdigit() and int(amount) >= 0:
            break
        else:
            print("Please enter a positive integer.")
    print(f"Your initial amount is: ${amount}")
    return amount

def get_monthly_amount():
    while True:
        amount = input("Enter your monthly contribution. Please round to nearest integer: $")
        if amount.isdigit() and int(amount) >= 0:
            break
        else:
            print("Please enter a positive integer.")
    print(f"Your monthly contribution is: ${amount}")
    return amount

def calculate_compound_interest(principal, monthly_contribution, rate, years):
    total_amount = principal
    for month in range(years * 12):
        total_amount *= (1 + rate / 12)
        total_amount += monthly_contribution
    return total_amount

def get_rate_from_range():
    while True:
        min_rate = input("Enter the minimum annual interest rate as a whole integer: ")
        max_rate = input("Enter the maximum annual interest rate as a whole integer: ")
        if min_rate.isdigit() and max_rate.isdigit() and float(min_rate) >= 0 and float(max_rate) > float(min_rate):
            min_rate = float(min_rate) / 100
            max_rate = float(max_rate) / 100
            break
        else:
            print("Please enter valid rates.")
    return min_rate, max_rate

def run_calculations(num):
    initial_amount = int(get_initial_amount())
    monthly_contribution = int(get_monthly_amount())
    years = int(input("Enter the number of years for the investment: "))
    min_rate, max_rate = get_rate_from_range()

    results = []
    for i in range(num):
        random_rate = random.uniform(min_rate, max_rate)
        total_amount = calculate_compound_interest(initial_amount, monthly_contribution, random_rate, years)
        results.append(total_amount)

    return results
   
 
def print_results(results):
    print("Investment results:")
    for i, result in enumerate(results):
        print(f"Simulation {i + 1}: ${result:.2f}")
    min_total = min(results)
    max_total = max(results)
    print("The higher end of this investment: ${:.2f}".format(max_total))
    print("The lower end of this investment: ${:.2f}".format(min_total))

num_simulations = input("Enter the number of simulations to run: ")
print_results(run_calculations(num_simulations))