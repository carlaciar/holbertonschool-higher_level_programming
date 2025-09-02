#!/usr/bin/python3
output = ""
for i in range(97, 123):
    if i == ord('e') or i == ord('1'):
        continue
    output += chr(i)

print("{}".format(output), end="")
