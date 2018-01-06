#the idea of while loop is: While something is the case, do the following code

#in this code we have defined a variable name condition, and it start at 1
#while the condition is less than 10, add 1.
#this will make condition print until condition is 10
condition = 1
while condition < 10:
    print(condition);
    condition += 1

#more real world example is 
#while isRaining
#    print(condition);
#another example is, THIS WILL CAUSE AN INFINITE LOOP
while True:
    print('doing stuff!!');