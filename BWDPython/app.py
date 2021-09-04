from math import *
'''
    name = 'michael'

    print('hi. \nhow are you')
    print(name)
    print(name.index('i'))
    print(name.replace('i', 'z'))

    print(len(name))
    print(name.upper())
    print(name.lower())
    print(name[0])

    print(sqrt(10))


    name = input('Enter your name: ')
    age = int(input('Enter your age: '))
    print('Your name is ',name,' and your are',age,'years old')


    sentence = input('Enter your sentence: ')
    print('Your sentece is: ',sentence)
    w1 = input('Enter the word to replace: ')
    w2 = input('Enter the word to replace it with: ')

    print(sentence.replace(w1, w2))

    countries = ['USA', 'UK', 'China', 'Thai']
    name = 'Michael'

    print(countries[2][0])
    print(countries[-1])
'''
'''
    def f(name,age):
        print('Hello '+name,'you are '+str(age),' years old.')
    # def f(*names):
    #     print('Hello '+names[0])


    name = input('Enter you name: ')
    age = input('Enter your age')
    f(name,age)
    def mF(n1,n2):
        return n1 + n2

    print(mF(2,2))
'''

'''
    n1 = int(input('Enter first number: '))
    n2 = int(input('Enter second number: '))
    op = input('Enter operator: ')

    if op == '+':
        print('The add is ', n1+n2)
    elif op == '-':
        print('The subtraction is ', n1-n2)
'''
'''
    readFile = open("/Users/tangmingjun/dev/python/BWDPython/read.txt",'r')
    print(readFile.readable())
    for f in readFile.readlines():
        print(f)
        

    readFile.close



    wFile = open("/Users/tangmingjun/dev/python/BWDPython/new.py",'w')
    wFile.write('print(\'this is new file\')')
'''
'''

    class preson:
        def __init__(self,name,age):
            self.name = name
            self.age = age

    name = input('Enter your name: ')
    age = input('Enter your age: ')

    p1 = preson(name,age)
    print(p1.name,p1.age)
'''
'''

    from new import Student

    class Person(Student):
        pass

    p1 = Person
    print(p1.name,p1.age,p1.gender)
'''
