#DO NOT TAMPER WITH THIS FILE
#ANY EDITS YOU MAKE TO THIS FILE WILL BE SAVED TO YOUR PUBLIC GITHUB HISTORY
#TAMPERING WITH THIS FILE WILL BE OBVIOUS AND WILL RESULT IN A ZERO

import main;
import datetime;

year = 2021
month = 11
day = 12

def test_code():
    assert main.diff21(5) == 16, "diff21(5) failed"
    assert main.diff21(10) == 11, "diff21(10) failed"
    assert main.diff21(21) == 0, "diff21(21) failed"
    assert main.diff21(25) == 8, "diff21(25) failed"

def test_late():
    assert datetime.datetime.now() < datetime.datetime(year, month, day + 1, 4, 0), "Submitted Late"
