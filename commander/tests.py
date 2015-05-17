import itertools
from Commands import commands
from commandtools import isCommand


if __name__ == "__main__":
    # List all commands and functions linked to

    print("{amt} commands available.".format(amt=len(commands)))
    for command, func in commands.items():
            line = "{command} >> ".format(command=command)
            func, args = func
            line += "{func}(".format(func=repr(func).split()[1])
            if args:
                    line += ", ".join(repr(arg) for arg in args)
            line += ')'
            print(line)
    print

    # Test isCommand on all variations of defined commands in commands.py
    passed = list()
    fails = list()
    for command in commands:
            for test in itertools.product(*command):
                test = " ".join(test)
                if isCommand(test, command):
                    passed.append(test)
                else:
                    fails.append(test)

    print("Ran {testnum} tests.".format(testnum=(len(passed) + len(fails))))
    print("Passed {passed} tests.".format(passed=len(passed)))
    for pas in passed:
        print("\t{pas}".format(pas=pas))
    print("Failed {fails} tests.".format(fails=len(fails)))
    for fail in fails:
        print("\t{fail}".format(fail=fail))
