number = str(input('[INPUT] Input 6 numbers separated with comma: '));
numberInArray = [];
if (len(number) < 1):
    print ('[ERROR] No numbers provided!');
else:
    chunk = (number).split(",");
    total = 0;
    for num in chunk:
        if (num.strip().isdigit()):
            numberInArray.append(int(num));
            total += int(num);
    if (len(numberInArray) > 6):
        print ('[ERROR] Too many numbers inputted!');
    elif (len(numberInArray) < 6):
        print ('[ERROR] Only input 6 numbers!');
    else:
        print ('[RESULT] Total:', total, 'and the average is:', total/len(numberInArray));
