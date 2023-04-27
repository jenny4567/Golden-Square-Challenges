from lib.music_list import *
import pytest

my_music_list = TrackList()
def test_list_all_exists():
    assert my_music_list.list_all() == {}

def test_add_adds():
    my_music_list.add("Goodbye Yellow Brick Road", "Elton John")
    assert my_music_list.list_all() == {"Goodbye Yellow Brick Road" : "Elton John"}

def test_add_excludes_deplicates():
    with pytest.raises(Exception) as e:
        my_music_list.add("Goodbye Yellow Brick Road", "Elton John")
    error_message = str(e.value)
    assert error_message == "Song already added." 

def test_add_incorrect_input():
    with pytest.raises(Exception) as e:
        my_music_list.add(13, 50)
    error_message = str(e.value)
    assert error_message == "Input must be strings."

def test_list_all():
    my_music_list.add("Under Pressure", "Queen")
    assert my_music_list.list_all() == {"Goodbye Yellow Brick Road" : "Elton John", "Under Pressure" : "Queen"}

def test_track_count():
    assert my_music_list.track_count() == 2

def test_one_string_one_int():
    with pytest.raises(Exception) as e:
        my_music_list.add(13, "The Offspring")
    error_message = str(e.value)
    assert error_message == "Input must be strings."