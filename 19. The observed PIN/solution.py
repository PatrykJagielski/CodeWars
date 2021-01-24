def get_pins(observed):
    pin_map = {
        '1': ['1', '2', '4'],
        '2': ['1', '2', '3', '5'],
        '3': ['2', '3', '6'],
        '4': ['1', '4', '5', '7'],
        '5': ['2', '4', '5', '6', '8'],
        '6': ['3', '5', '6', '9'],
        '7': ['4', '7', '8'],
        '8': ['5', '7', '8', '9', '0'],
        '9': ['6', '8', '9'],
        '0': ['8', '0']
    }

    m = [pin_map.get(x) for x in observed]
    results = []

    for i_1 in m[0]:
        res = i_1
        if len(m) >= 2:
            for i_2 in m[1]:
                res = i_1 + i_2
                if len(m) >= 3:
                    for i_3 in m[2]:
                        res = i_1 + i_2 + i_3
                        if len(m) >= 4:
                            for i_4 in m[3]:
                                res = i_1 + i_2 + i_3 + i_4
                                if len(m) >= 5:
                                    for i_5 in m[4]:
                                        res = i_1 + i_2 + i_3 + i_4 + i_5
                                        if len(m) >= 6:
                                            for i_6 in m[5]:
                                                res = i_1 + i_2 + i_3 + i_4 + i_5 + i_6
                                                if len(m) >= 7:
                                                    for i_7 in m[6]:
                                                        res = i_1 + i_2 + i_3 + i_4 + i_5 + i_6 + i_7
                                                        if len(m) >= 7:
                                                            for i_8 in m[7]:
                                                                results.append(
                                                                    i_1 + i_2 + i_3 + i_4 + i_5 + i_6 + i_7 + i_8)
                                                        else:
                                                            results.append(res)
                                                else:
                                                    results.append(res)
                                        else:
                                            results.append(res)
                                else:
                                    results.append(res)
                        else:
                            results.append(res)
                else:
                    results.append(res)
        else:
            results.append(res)

    return results
