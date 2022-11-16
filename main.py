number = int(input('Enter a number: '))
base1 = int(input('Enter the first base no. you would like to trigger the phrase Fizz: '))
base2 = int(input('Enter the second base no. you would like to trigger the phrase Fizz: '))

if number % base1 == 0:
    print('fizz')
if number % base2 == 0:
    print('buzz')
if number % base1 == 0 and number % base2 == 0:
    print('fizzbuzz')
if number > 1:
   for i in range(2,number):
       if (number % i) != 0:
        phrase = True
if phrase == 'True':
  print('oops')
