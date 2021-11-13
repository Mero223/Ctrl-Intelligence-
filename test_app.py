""" Unit tests for the functions imported into app.py

to run enter "pytest test_app.py" in terminal"""

from select_story import select_story
from select_story import story_list


def test_select_story_result():
    result = select_story()
    assert result in set(story_list)