""" Selects a random cooking recommendation. """

from random import seed, choice

cook_list = [
"Turkey Pot Pie",
"Maple-glazed ham steak",
"Mandarin orange salad",
"Garlic butter turkey meatballs",
"Slow cooker chili",
"Shrimp scampi"
]

def select_cook():
    seed()
    cook_activity = choice(cook_list)

    return cook_activity
