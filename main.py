def error_detect(parity_type, data):
    "Returns the location of error in a 2d array of bits"
    error_location_string = ""
    has_error = False

    for index, row in enumerate(data):
        parity_bit_row = row[-1:][0]
        row_bits = [x for x in row[:-1] if x == 1]
        row_bits_length = len(row_bits) % 2 if row_bits != None else 1

        func = parity_bit_row != row_bits_length if parity_type == "even" else parity_bit_row == row_bits_length

        if (func):
            error_location_string += str(index) + ":"
            has_error = True
            break

    if(has_error == True):
        for index in range(len(data[0])):
            column = [x[index] for x in data]
            parity_bit_column = column[-1:][0]
            column_bits = [x for x in column[:-1] if x == 1]
            column_bits_length = len(
                column_bits) % 2 if column_bits != None else 1
            func = parity_bit_column != column_bits_length if parity_type == "even" else parity_bit_column == column_bits_length
            if(func):
                error_location_string += str(index)
                break
        return error_location_string
    return ""


def error_correct(data, location):
    "Return the corrected 2d array of bits"
    location = location.split(":")
    location = [int(x) for x in location]
    data[location[0]][location[1]] ^= 1
    return data
