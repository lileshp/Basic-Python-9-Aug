
#Tokens
    smallest unit/element of programming lang.

    Keywords
    Literals/Constants
    Identifier
    Operator


    Keyword
     Python Keyword module is used to avail the list of all the keywords.
     The reserved words cannot be used as a variable name.
     all keywords in lowercase letter except(True, False, None)
        False	await	    else	import	    pass
        None	break	    except	in	    raise
        True	class	    finally	is	    return
        and	continue    for	        lambda	    try
        as	def	    from	nonlocal    while
        assert	del	    global	not	    with
        async	elif	    if	        or	    yield

    variable:
        a = 50
        city = "Bhopal"
        res = True
        marks = 20.6
        a = "John"
        _enroll = 123456789
    Literals:
            any raw value which is assigned in any variable or constant
    constants:
            constant a type of variable but with fixed value.
            there is no scope of constant in python.
            COLLEGE = "LNCT"
            CITY = "BHOPAL"
            COLLEGE = "JNCT"

    Identifiers:
        A python identifiers is a name used to identify a variable, function,
        class, module, or any other object.

        rules to declare identifiers name:
                1. not start with digits[0-9]
                2. can not contain any space
                3. can not contain any special character (_)
                4. should not use keywords in identifiers name.
                5. class name start with a uppercase letter and all identifiers
                    with a lowercase letter.
                6. starting an identifier with a single underscore indicates
                    that identifier is a private.
                        _name = "John"
                7. starting an identifier with two leading underscore indicates
                    that identifier as strongly private identifier.
                        __acc = 235698741520
                8. if the identifier also ends with two trailing underscore, the
                    identifier is a language-defined special name.
                        __name__

                
firstName = "John"
last_name = "Mathew"



name_of_student_from_mumbai = "John" #snake case
nameOfStudentFromMumbai = "John" #camel case
class NameOfStudentFromMumbai: #pascal case
    pass

        

##Operators
1. Arithmetic
2. comparison/relational
3. assignment
4. Logical
5. bitwise
6. membership
7. identity


Arithmetic
    + - * / % **(exponent) //(floor division)
assignments
    = += -= *= /= //= %= **=
relational:
    == < > <= >= !=
logical
    and or not

Bitwise
    &(and), |(or), ^(xor), <<(left shift), >>(right shift)
    &(and) => each bit of the output is 1, if the corresponding bit of x and
            of y is 1, otherwise it's 0.
    |(or) => each bit of the output is 0, if the corresponding bit of x and
            y is 0, otherwise it's 1.
    ^(Xor)=> each bit of the output is the same as the corresponding bit in a
            if that bit in y is 0
    <<(left shift) >>(right shift)

    00000000
    128 64 32 16 8 4 2 1
    
    
  a = 60 = 00111100
  b = 12 = 00001100
  a & b = 00001100
  a | b = 00111100
  a ^ b = 00110000
  a << 2 = 11110000
  a >> 3 = 00000111

Membership:
    in, not in
  
Identity:
    is, is not



#DataTypes:
 1. Number/Integer
 2. String
 3. List
 4. Tuple
 5. Dictionary
 6. Set


1. Number:
        Number is a immutable object.
        int()
        float()
        0-9
        number is non iterable object
        
2. String:
        String is an immutable object.
        you can update an existing string by reassigning a variable to
        another string.
        str()
        string is iterable object.
        slicing operator use with string. [start:end:steps]
        string concat = +
        string repeat = *
        membership operator = in ,not in

        function:
            str(), len()
        methods:
            count(), isalpha(), isdigit(), lower(), upper(), replace()
            split(), strip(), title(), islower(), isupper()
        
      
##Function vs Methods

def fname():
    print("This is function")

class One:
    def show(self):
        print("This is Method")
class Two:
    def blind(self):
        print("This is Method")

fname()
a = One()
a.show()

b = Two()
b.show()


int()
str()
age = 54
name = "john"

##List
    list ordered group of items or elements. list elements dont
    have to be of the same type.
    list are mutable object that can change thier values.
    list items seperated by comma and enclosed with square
    brackets.
    index from L -> R = 0, R -> L = -1
    we can slicing operator in list as string.
    concate = +
    repetition = *
    membership = in, not in
    []
    list()


##Tuple
    tuple ordered group of items or elements. Tuple elements dont
    have to be of the same type.
    tuples are immutable object.
    tuple items seperated by comma and enclosed with ()
    index from L -> R = 0, R -> L = -1
    slicing operator
    membership
    ()
    tuple()
    
##Dictionary
    marks = [90,80,76,84,50]
    dict()
    dict kind of hash table type which consist of key:value pairs
    of unordered elements.
        key : must be immutable data type, usually number or string
        value : can be any arbitrary object of python.
    dictionary are mutable object that can change thier value.
    items are seperated by commas, each key is seperated from its
    value by colon(:) and enclosed with curly braces({})
    {}

#set
    set are unordered collection of simple objects.
    {}
    set()
    a.intersection(b) => return common elements present on both sets
    a.union(b) => return all the elements present in both of sets.
    a-b = return values which are present in a but not present in b.
##Comprehension
            































            
