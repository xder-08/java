MONTHLY_FEE = 120.62
EFIR_RATE1 = 8.36
EFIR_RATE2 = 9.41
EFLR_RATE = 9.11
GFIR_RATE1 = 4.56
GFIR_RATE2 = 5.89
GFLR_RATE = 3.93
MONTHLY_GAS_FEE = 1.32
ELEC_THRESHOLD = 1000
GAS_THRESHOLD = 950
CDN = 0.01

PROV_TAX = {
    'ab': 0.05, 'bc': 0.05, 'mb': 0.05, 
    'nt': 0.05, 'nu': 0.05, 'qc': 0.05, 
    'sk': 0.05, 'yt': 0.05, 'on': 0.13,
    'nb': 0.15, 'nl': 0.15, 'ns': 0.15, 'pe': 0.15
}

print("Welcome to the Global Energy bill calculator!")
account_number = input("Enter your account number.\n")
month = input("Enter the month number (e.g., for January, enter 1).\n")
electricity_plan = input("Enter your electricity plan (EFIR or EFLR).\n")
electricity_usage = float(input("Enter the amount of electricity you used in month " + month + " (in kWh).\n"))
gas_plan = input("Enter your gas plan (GFIR or GFLR).\n")
gas_usage = float(input("Enter the amount of gas you used in month " + month + " (in GJ).\n"))
province = input("Enter the abbreviation for your province of residence (two letters)\n").lower()

if electricity_plan == "EFIR":
    if electricity_usage <= ELEC_THRESHOLD:
        electricity_cost = electricity_usage * EFIR_RATE1 * CDN
    else:
        electricity_cost = (ELEC_THRESHOLD * EFIR_RATE1 + 
                          (electricity_usage - ELEC_THRESHOLD) * EFIR_RATE2) * CDN
elif electricity_plan == "EFLR":
    electricity_cost = electricity_usage * EFLR_RATE * CDN
else:
    electricity_cost = 0

if gas_plan == "GFIR":
    if gas_usage <= GAS_THRESHOLD:
        gas_cost = gas_usage * GFIR_RATE1 * CDN
    else:
        gas_cost = (GAS_THRESHOLD * GFIR_RATE1 + 
                   (gas_usage - GAS_THRESHOLD) * GFIR_RATE2) * CDN
elif gas_plan == "GFLR":
    gas_cost = gas_usage * GFLR_RATE * CDN
else:
    gas_cost = 0

subtotal = electricity_cost + gas_cost + MONTHLY_FEE + MONTHLY_GAS_FEE

if province in PROV_TAX:
    tax = subtotal * PROV_TAX[province]
    total = subtotal + tax
    print(f"Thank you! Your total amount due now is: ${total:.2f}")
else:
    print("Invalid province code")