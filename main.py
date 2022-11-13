result = []


def divider(a, b):
    try:
        if a < b:
            result.append(res)
        if b > 100:
            result.append(res)
            if type(a) == "str":
                result.append(res)
    except IndexError:
        print('IndexError print')
    except ValueError:
        print('ValueError print')
    except TypeError:
        print('Value Error')
        return
    except ZeroDivisionError:
        print('ZeroDivisionError')
        return

    return a / b


data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}
for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)
