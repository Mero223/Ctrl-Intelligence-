""" Selects a random walk activity prompt. """

from random import seed, choice

nature_list = [
"On your walk, see how many different types of trees you can spot.  Can you name any of them?",
"Go for a stroll and see if you can spot any insects!",
"Keep an ear out on your walk today and see if  you hear any birds?",
"Give back to nature today, and go litter picking",
"Collect your favourite leaves you spot on your walk today!"
]

def select_nature():
    seed()
    selected_suggestion = choice(nature_list)

    return selected_suggestion
