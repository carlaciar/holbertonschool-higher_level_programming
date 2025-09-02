#!/usr/bin/python3
output1 = ""
for i in range(97, 101):
    output1 += chr(i)

output2 = ""
for i in range(102, 113):
    output2 += chr(i)

output3 = ""
for i in range(114, 123):
    output3 += chr(i)

print("{}{}{}".format(output1, output2, output3), end="")
