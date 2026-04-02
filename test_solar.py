import solar

def test_gravity():
    assert solar.gravity_force(10, 10, 2)/solar.gravity_constant == 25

def test_distance():
    pos1 = (1,1)
    pos2 = (10,1)
    assert solar.distance(pos1,pos2) == 9