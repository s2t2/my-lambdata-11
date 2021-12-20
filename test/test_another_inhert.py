
# test/test_another_inherit.py

from my_lambdata.assignment_w_inherit import MyFrame

def test_add_state_names():
    my_frame = MyFrame({"abbrevs": ["CA", "CO", "CT", "DC", "TX"]})

    # test there is no state_name col
    cols = my_frame.columns.tolist()
    #self.assertIn("abbrevs", cols)
    #self.assertNotIn("state_name", cols)
    assert "abbrevs" in cols
    assert "state_name" not in cols

    ## test that our function added the proper column
    my_frame.add_state_names()
    cols = my_frame.columns.tolist()
    assert "state_name" in cols


# doesn't get run b/c not named right
def do_stuff():
    assert False
