from random import choice, seed

def select_story():
    seed()
    story_list = ["story 1","story 2","story 3","story 4","story 5"]
    selected_story = choice(story_list)
    return selected_story