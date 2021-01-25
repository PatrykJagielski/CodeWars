def same_structure_as(original, other):
    my_table = str(original).maketrans('123456789', '000000000')
    return str(original).translate(my_table) == str(other).translate(my_table)
