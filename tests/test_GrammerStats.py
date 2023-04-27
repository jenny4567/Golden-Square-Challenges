from lib.GrammerStats import *

Stat_1 = GrammarStats()

def test_GrammerStats_check():
    bool_list = []
    bool_list.append(Stat_1.check("Happy!"))
    bool_list.append(Stat_1.check("happy!"))
    bool_list.append(Stat_1.check("Happy"))
    bool_list.append(Stat_1.check("happy"))
    assert bool_list == [True, False, False, False]

def test_GrammerStats_percent_good():
    assert Stat_1.percentage_good() == 25