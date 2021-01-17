def find_missing_letter(chars):
    for i in range(len(chars)):
        if ord(chars[i]) == ord(chars[i+1]) - 2:
            return chr(ord(chars[i]) + 1)
