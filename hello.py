# This simple program says hello to you and asks for your name.

print('Hello!')
print('What is your name?') #asks for name
name = input()
print('Nice to meet you ' + name)
print ('Your name has that length:')
print(len(name)) #gets name lenght
print('What is your age?') #asks for age
age = input()
print('That is a nice age, so next year you will be '+ str(int(age)+1) + '.')
