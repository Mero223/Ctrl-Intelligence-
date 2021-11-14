""" Selects a random walk activity prompt. """

from random import seed, choice

random_list = [
"On your walk, see how many different types of trees you can spot.  Can you name any of them?",
"Go for a stroll and see if you can spot any insects!",
"Keep an ear out on your walk today and see if  you hear any birds?",
"Give back to random today, and go litter picking",
"Collect your favourite leaves you spot on your walk today!",
"Can you draw a self portrait without taking your pencil off the page?",
"Draw your favourite animal",
"Embrace your inner child and give finger painting a go",
"Draw the view from your window",
"Go to a local park and draw what you can see",
"Create a collage",
"Draw your workspace",
"Go to the cook page and check out Turkey Pot Pie",
"Go to the cook page and check out Maple-glazed ham steak",
"Go to the cook page and check out Mandarin orange salad",
"Go to the cook page and check out Garlic butter turkey meatballs",
"Go to the cook page and check out Slow cooker chili",
"Go to the cook page and check out Shrimp scampi"
]

def select_random():
    seed()
    random_suggestion = choice(random_list)

    return random_suggestion
