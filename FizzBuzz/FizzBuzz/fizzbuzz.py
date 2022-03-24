def FizzBuzz(n):
    numbers= list(range(n))
    boslist= []
    
    for i in numbers:
        if i % 3 == 0 and i % 5 == 0:
             boslist.append("FizzBuzz")
        elif i % 3 == 0 :
             boslist.append("Fizz")
        elif i % 5 == 0 :
              boslist.append("Buzz")
        elif i % 3 != 0 and i % 5 != 0:
              boslist.append(i)
    for i in boslist:
        print(i)



