def obrabotka(dic):
    operationsDict = {
        "+": lambda v1, v2: v1 + v2,
        "-": lambda v1, v2: v1 - v2,
        "*": lambda v1, v2: v1 * v2,
        "/": lambda v1, v2: v1 / v2,
        "%": lambda v1, v2: v1 % v2,
        "^": lambda v1, v2: v1 ** v2,
    }
    a = dic['num_1']
    b = dic['action']
    c = dic['num_2']
    if (b == "/" or b == "%") and c == '0':
        return 'error'
    else:
        try:
            aa = float(a.replace(',', '.'))
            cc = float(c.replace(',', '.'))
            operation_lambda = operationsDict[b]
            result = operation_lambda(aa, cc)
            return result
        except Exception:
            return None

    # if a.isfloat() and c.isfloat() and b in operationsDict:
    #     a = float(a)
    #     c = float(c)
    #     operation_lambda = operationsDict[b]
    #     result = operation_lambda(a, c)
    #     return result
    # else:
    #     return -1

# print(obrabotka({'num_1':'5.9','action': '/','num_2':'0'}))
