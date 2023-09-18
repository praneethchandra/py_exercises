import random
import json
from employee import Root, Employee, Amount, Address, Paycheck, Split, Summary, TimeOff, Projects, Project

names = ["Alice ", "Bob", "Cyrus", "David", "Eme", "Faze", "Gag", "Harry", 
         "Ion", "Jose", "Kate", "Lac", "Maze", "Nick", "Oscar", "Peds", "Quak", "Rick", 
         "Sam", "Toss", "Umb", "Ven", "Xur", "Yon", "Zack"]
cities = ["San Jose", "San Francisco", "San Diego", "Santa Monica", "San Libispo", "Santa Ann", "Maui", "Big Island", "Kauai"]
states = ["Alabama", "Alaska", "Arizona","Arkansas","California", "Colorado", "Connecticut","Delaware","Florida","Georgia"
          "Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts",
          "Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey",
          "New Mexico","New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island",
          "South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia",
        "Wisconsin","Wyoming"]
zipcodes = []
streetname = "10 John Doe"
designations = ["Jr. Software Engineer", "Sr. Software Engineer", "Software Engineer", "Software Manager"]

def generate_address():
    address = Address(random.choice(names), streetname, random.choice(cities), random.choice(states), random.randint(501, 99950))
    return address

def generate_designation():
    return random.choice(designations)

def generate_timeoff():
    timeoff = TimeOff(random.randint(0,100), random.randint(0,50), random.randint(0,25))
    return timeoff

def generate_summary():
    count = random.randint(0,10)
    completed = random.randint(0,count)
    pending = random.randint(0, count - completed)
    cancelled = count - completed - pending
    summary = Summary(count, completed, pending, cancelled)
    return summary

def generate_project():
    name = "PROJECT" + str(random.randint(0,100))
    description = name
    project = Project(name, description)
    return project

def generate_projects():
    projects = []
    for i in range(0,10):
        projects.append(generate_project())
    projects = Projects(generate_summary(), projects)
    return projects

def generate_amount(amount=100.00):
    value = round(random.uniform(0.00, amount), 2)
    currency = "USD"
    convertedToValue = 1.15 * value
    convertedToCurrency = "EUR"

    amt = Amount(value, currency, convertedToValue, convertedToCurrency)
    return amt


def generate_paycheck(type, amount=100.00, add_split=False):
    splits = []
    if add_split:
        for i in range(0,3):
            local_type = None
            if i==0:
                local_type='MONTHLY'
            elif i==1:
                local_type='GRANT_BONUS'
            elif i==2:
                local_type='GRANT_STOCK'
            else:
                local_type='MONTHLY'
            amt = generate_amount(amount)
            split = Split(local_type, amt)
            splits.append(split)    
    paycheck = Paycheck(type, generate_amount(amount), splits)
    return paycheck
   
def generate_paychecks(amt=100.00):
    paychecks = []
    # generate GRANT_BONUS
    grant_bonus_amt = generate_paycheck("GRANT_BONUS", amount=amt) 
    paychecks.append(grant_bonus_amt)
    # generate GRANT_STOCK
    grant_stock_amt = generate_paycheck("GRANT_STOCK", amount=amt) 
    paychecks.append(grant_stock_amt)
    # generate MONTHLY
    paychecks.append(generate_paycheck("MONTHLY", amount=amt+grant_bonus_amt.amount.value+grant_stock_amt.amount.value))

    # generate NEGATE_CHECK
    paychecks.append(generate_paycheck("NEGATE_CHECK", amount=20, add_split=True))

    # generate DISPUTE_CHECK
    paychecks.append(generate_paycheck("DISPUTE", amount=10))
    return paychecks

def generate_ceo():
    employee = Employee("CEO", generate_address(), generate_paychecks(1000.00), generate_timeoff(), generate_projects())
    root = Root(employee)
    return root.to_json()

def generate_cto():
    employee = Employee("CTO", generate_address(), generate_paychecks(750.00), generate_timeoff(), generate_projects())
    root = Root(employee)
    return root.to_json()

def generate_employee():
    employee = Employee(generate_designation(), generate_address(), generate_paychecks(), generate_timeoff(), generate_projects())
    root = Root(employee)
    return root.to_json()

