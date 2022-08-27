flag = 0
inputnum = int(input("Enter Number: "))
inputdigit = int((input("Enter Digit: ")))
checker = int(inputnum)
falser = int(inputnum)  # mirroring number
while falser != 0:
    checker = falser % 10
    if checker == inputdigit:
        flag = 1
    falser = int(falser / 10)

if flag == 1:
    print("Approved")
if flag == 0:
    changer = inputnum % 10
    inputnum = (inputnum - changer) + inputdigit
    print("New Num Is: ", inputnum)
