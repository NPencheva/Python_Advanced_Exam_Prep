def flights(*args):
    result = {}
    arguments = [el for el in args]
    for i in range(len(arguments)):
        if i % 2 == 0:
            if arguments[i] == "Finish":
                break
            if arguments[i] in result.keys():
                result[arguments[i]] += arguments[i + 1]
            else:
                result[arguments[i]] = arguments[i + 1]

    return result


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
