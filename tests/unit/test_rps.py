from rock_paper_scissors.rps import rock_paper_scissors


def test_rps():
    """
    Basic test for Rock Paper Scissors
    """

    assert rock_paper_scissors(1) is not None
    result, pc_choice = rock_paper_scissors(1)
    for i in range(0, 3):
        result, pc_choice = rock_paper_scissors(i)
        if pc_choice == i:
            assert result == 0
        elif (i + 1) % 3 == pc_choice % 3:
            assert result == -1
        else:
            assert result == 1