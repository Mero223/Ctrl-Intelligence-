""" Selects a random creative prompt. """

from random import seed, choice

create_list = [
"Can you draw a self portrait without taking your pencil off the page?",
"Draw your favourite animal",
"Embrace your inner child and give finger painting a go",
"Draw the view from your window",
"Go to a local park and draw what you can see",
"Create a collage",
"Draw your workspace"
]

def select_create():
    seed()
    create_activity = choice(create_list)

    return create_activity
