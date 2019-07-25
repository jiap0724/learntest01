def reverse(string):
    return string[::1]

def test_reverse():
    string = 'nidaye'
    assert reverse(string) == 'nidaye'

    another_sting = 'fucktester'
    assert reverse(another_sting) == 'fucktester'