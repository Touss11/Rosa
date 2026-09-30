import numpy as np

ZONES = ['Central', 'North', 'Far West']
TIME_BLOCKS = ['Lunch', 'Weekday eve', 'Fri/Sat eve', 'Other']
COSTS = {'refund': 15.0, 'churn_orders': 1.8, 'margin': 20.0}

_BASE_ORDERS = {  # orders at the 45-minute promise
    ("Central", "Lunch"): 260, ("Central", "Weekday eve"): 330,
    ("Central", "Fri/Sat eve"): 190, ("Central", "Other"): 190,
    ("North", "Lunch"): 190, ("North", "Weekday eve"): 250,
    ("North", "Fri/Sat eve"): 150, ("North", "Other"): 160,
    ("Far West", "Lunch"): 120, ("Far West", "Weekday eve"): 170,
    ("Far West", "Fri/Sat eve"): 210, ("Far West", "Other"): 192,
}
_BASE_MEDIAN = {  # median delivery minutes at the 45-minute promise
    ("Central", "Lunch"): 26.6, ("Central", "Weekday eve"): 28.9,
    ("Central", "Fri/Sat eve"): 31.6, ("Central", "Other"): 25.6,
    ("North", "Lunch"): 28.2, ("North", "Weekday eve"): 31.1,
    ("North", "Fri/Sat eve"): 36.4, ("North", "Other"): 27.5,
    ("Far West", "Lunch"): 30.1, ("Far West", "Weekday eve"): 34.6,
    ("Far West", "Fri/Sat eve"): 42.0, ("Far West", "Other"): 29.5,
}


def _share(promise):
    return 1 / (1 + np.exp((promise - 60) / 8))


def _expected_orders(zone, time_block, promise):
    return _BASE_ORDERS[(zone, time_block)] * _share(promise) / _share(promise)

