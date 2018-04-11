from main import error_correct, error_detect


def test_error_correct():

    data_wrong_1 = [[0, 1, 1, 1], [1, 0, 1, 0], [0, 0, 1, 1], [0, 1, 1, 0]]
    correct_data_1 = [[1, 1, 1, 1], [1, 0, 1, 0], [0, 0, 1, 1], [0, 1, 1, 0]]

    data_wrong_2 = [[1, 1, 1], [0, 0, 0], [1, 0, 1]]
    correct_data_2 = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

    error_location_1 = error_detect('even', data_wrong_1)
    error_location_2 = error_detect('even', data_wrong_2)

    assert error_correct(data_wrong_1, error_location_1) == correct_data_1
    assert error_correct(data_wrong_2, error_location_2) == correct_data_2


def test_error_detect():
    data_correct_1 = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    data_wrong = [[1, 1, 1], [0, 0, 0], [1, 0, 1]]
    data_correct_2 = [[1, 1, 1, 1], [1, 0, 1, 0], [0, 0, 1, 1], [0, 1, 1, 0]]
    data_wrong_2 = [[0, 1, 1, 1], [1, 0, 1, 0], [0, 0, 1, 1], [0, 1, 1, 0]]

    assert error_detect('even', data_correct_1) == ""
    assert error_detect('even', data_wrong) == "0:1"
    assert error_detect('even', data_correct_2) == ""
    assert error_detect('even', data_wrong_2) == "0:0"
