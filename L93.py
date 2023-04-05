#Katherine O'Roark
def replace_substring(string, sub, replacement):
    output = []
    index = 0
    while index<len(string):
        if string[index:index+len(sub)] == sub:
            index += len(sub)
            output.append(replacement)
        else:
            output.append(string[index])
            index += 1
    print("".join(output))

replace_substring("I think cars are cool", "cars","planes")
