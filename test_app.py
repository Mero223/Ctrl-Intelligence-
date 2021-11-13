""" Unit tests for the functions imported into app.py

to run enter "pytest test_app.py" in termina;"""

from select_story import select_story

story = ["story 1","story 2","story 3","story 4","story 5"]

def test_select_story_result():
    result = select_story()
    assert result in set(story)