from typing import List
from typing import Any
from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Address:
    name: str
    street_name: str
    city: str
    state: str
    zipcode: int

    def __init__(self, name, street_name, city, state, zipcode):
        self.name = name
        self.street_name = street_name
        self.city = city
        self.state = state
        self.zipcode = zipcode

    @staticmethod
    def from_dict(obj: Any) -> 'Address':
        _name = str(obj.get("name"))
        _street_name = str(obj.get("street_name"))
        _city = str(obj.get("city"))
        _state = str(obj.get("state"))
        _zipcode = int(obj.get("zipcode"))
        return Address(_name, _street_name, _city, _state, _zipcode)

@dataclass_json
@dataclass
class Amount:
    value: float
    currency: str
    convertedToValue: float
    convertedToCurrency: str

    def __init__(self, value, currency, convertedToValue, convertedToCurrency):
        self.value = value
        self.currency = currency
        self.convertedToValue = convertedToValue
        self.convertedToCurrency = convertedToCurrency

    @staticmethod
    def from_dict(obj: Any) -> 'Amount':
        _value = float(obj.get("value"))
        _currency = str(obj.get("currency"))
        _convertedToValue = float(obj.get("convertedToValue"))
        _convertedToCurrency = str(obj.get("convertedToCurrency"))
        return Amount(_value, _currency, _convertedToValue, _convertedToCurrency)

@dataclass_json    
@dataclass
class Split:
    type: str
    amount: Amount

    def __init__(self, type, amount):
        self.type = type
        self.amount = amount

    @staticmethod
    def from_dict(obj: Any) -> 'Split':
        _type = str(obj.get("type"))
        _amount = Amount.from_dict(obj.get("amount"))
        return Split(_type, _amount)


@dataclass_json
@dataclass
class Paycheck:
    type: str
    amount: Amount
    split: List[Split]

    def __init__(self, type, amount, split):
        self.type = type
        self.amount = amount
        self.split = split

    @staticmethod
    def from_dict(obj: Any) -> 'Paycheck':
        _type = str(obj.get("type"))
        _amount = Amount.from_dict(obj.get("amount"))
        _split = [Split.from_dict(y) for y in obj.get("split")]
        return Paycheck(_type, _amount, _split)

@dataclass_json
@dataclass
class Project:
    name: str
    description: str

    def __init__(self, name, description):
        self.name = name
        self.description = description

    @staticmethod
    def from_dict(obj: Any) -> 'Project':
        _name = str(obj.get("name"))
        _description = str(obj.get("description"))
        return Project(_name, _description)

@dataclass_json
@dataclass
class Summary:
    count: int
    completed: int
    pending: int
    cancelled: int

    def __init__(self, count, completed, pending, cancelled):
        self.count = count
        self.completed = completed
        self.pending = pending
        self.cancelled = cancelled


    @staticmethod
    def from_dict(obj: Any) -> 'Summary':
        _count = int(obj.get("count"))
        _completed = int(obj.get("completed"))
        _pending = int(obj.get("pending"))
        _cancelled = int(obj.get("cancelled"))
        return Summary(_count, _completed, _pending, _cancelled)

@dataclass_json
@dataclass
class Projects:
    summary: Summary
    project: List[Project]

    def __init__(self, summary, project):
        self.summary = summary
        self.project = project

    @staticmethod
    def from_dict(obj: Any) -> 'Projects':
        _summary = Summary.from_dict(obj.get("summary"))
        _project = [Project.from_dict(y) for y in obj.get("project")]
        return Projects(_summary, _project)


@dataclass_json
@dataclass
class TimeOff:
    workHours: int
    floatingHours: int
    pendingHours: int

    def __init__(self, workHours, floatingHours, pendingHours):
        self.workHours = workHours
        self.floatingHours = floatingHours
        self.pendingHours = pendingHours

    @staticmethod
    def from_dict(obj: Any) -> 'TimeOff':
        _availableHours = int(obj.get("availableHours"))
        _floatingHours = int(obj.get("floatingHours"))
        _pendingHours = int(obj.get("pendingHours"))
        return TimeOff(_availableHours, _floatingHours, _pendingHours)

@dataclass_json   
@dataclass
class Employee:
    designation: str
    address: Address
    paycheck: List[Paycheck]
    timeOff: TimeOff
    projects: Projects

    def __init__(self, designation, address, paycheck, timeOff, projects):
        self.designation = designation
        self.address = address
        self.paycheck = paycheck
        self.timeOff = timeOff
        self.projects = projects

    @staticmethod
    def from_dict(obj: Any) -> 'Employee':
        _designation = str(obj.get("designation"))
        _address = Address.from_dict(obj.get("address"))
        _paycheck = [Paycheck.from_dict(y) for y in obj.get("paycheck")]
        _timeOff = TimeOff.from_dict(obj.get("timeOff"))
        _projects = Projects.from_dict(obj.get("projects"))
        return Employee(_designation, _address, _paycheck, _timeOff, _projects)


@dataclass_json
@dataclass
class Root:
    employee: Employee

    def __init__(self, employee):
        self.employee = employee

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        _employee = Employee.from_dict(obj.get("employee"))
        return Root(_employee)


# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)
