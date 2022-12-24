import sys


def calc(expr, register, inv_register):
    try:
        r = register.get(expr[0])
        for i in range(1, len(expr) - 1, 2):
            x = expr[i]
            b = register.get(expr[i + 1])
            r = str(eval(r + x + b))
        return inv_register.get(r)
    except:
        return "unknown"


def update_register(register, inv_register, name, value):
    old_value = register.get(name)
    register.update({name: value})
    try:
        if inv_register.get(old_value):
            inv_register.pop(old_value)
        inv_register.update({value: name})
    except:
        inv_register.update({value: name})


def main():
    register = {}
    inv_register = {}

    for line in sys.stdin:
        tokens = line.split()

        if tokens[0] == "def":
            name = tokens[1]
            value = tokens[2]
            update_register(register, inv_register, name, value)

        elif tokens[0] == "calc":
            res = calc(tokens[1:-1], register, inv_register)
            print(" ".join(tokens[1:]) + " " + ("".join(res) if res else "unknown"))

        elif tokens[0] == "clear":
            register = {}
            inv_register = {}


if __name__ == '__main__':
    main()
