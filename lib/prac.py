# if/else statements.

dog = "cuddly"

if dog == "hungry":
    owner = "refilling food bowl."
elif dog == "thirsty":
    owner = "refilling bowl."
elif dog == "playful":
    owner = "playful tug-of-war."
else:
    owner = "Reading newspaper."
    
# note that owner was not decalared. this is because puthon does not require one to 
# declare a variable before a conditional unlike javascript.

# Truthy and falsey values.
# there are many  data types that python consideres falsey.
# empty lists[], empty tuples (), empty dictionaries{},
# empty sets set(),empty strings '',""zero of any numeric type (0, 0.0),none and false .
# note that using these data types/ vlaues in control flow mean sthe condition is false.

def control_flow(value):
    if value:
        print("yep!")
    else:
        print("nope!")    

control_flow(False)
control_flow(None)
control_flow(True)
control_flow("")
control_flow(0)
control_flow("0")

# CONDITIONAL STATEMENTS.

age = 1 

is_baby = 'baby' if age < 2 else 'not a baby'

# this is equivalent to these 
age = 1 
if age < 2 : 
    is_baby = 'baby'
else:
    is_baby = 'not a baby'

age = 65
is_name = "baby" if age < 1 else "a tolder and so on until an elder."  
print(is_name)                                                                        



qualification = True
qualification = False
is_qualified = "Congratulations you meet the requirements for this job" if qualification == True else "Sorry we are looking for more people with more years of experience in this field"
print(is_qualified)

# answers to questions from genrated by chat gpt
# a list of temepratures in celcius. categorize each temp as either "cold", "moderate" or "hot"
# use a conditional expression to achieve this.
# write a function "categorize_temparature" takes temparature as an argumnet and returns the corresponding category.

def categorize_temparature(temparature):
    # cold temp is below 10 c 
    if temparature < 10:
        return "Cold"
        # print("Cold")
    elif temparature > 10 and temparature < 25:
        return "Moderate"
        # print ("MOderate")
    else :
        return "Hot"
        # print ("Hot")
    
print(categorize_temparature(567))
print(categorize_temparature(23))
print(categorize_temparature(-564353))

# the above method is the tradiditonal way of writing conditional statements.
# to apply a better method (The gog O notation) we are write as follows:
def category (temperature):
    return "Cold" if temperature < 10 else "Moderate" if temperature <= 25 else "Hot"
print(category(2))
print(category(23))
print(category(4546353))
print(category(-254234623))


# Try/Except Statements.

# -> exceptions error messages are a type od error message that we can intercept so that our python application can continue to run.
def divide(num1, num2):
    try:
        quotient = num1 / num2
        return quotient
    except:
       return "An error has occured"

print(divide(81,9))

def another_divide(num1, num2):
    try:
        quotient = num1 / num2
        return quotient
    except ZeroDivisionError:
        return "Error: num2 cannot be equal to 0"
    except TypeError:
        return "Error: input must be of type int or float"
    
print(another_divide(100, 10))

def division_two(num1, num2):
    try:
        quotient= num1 / num2
        return quotient
    except ZeroDivisionError:
        return "Error: num2 cannot be equal to 0"
    except TypeError:
        return "Error: input must be of type int or float"
    finally:
        return "Isn't divions that return  errors in python fun?"
    
print(division_two(3463, 453))

# NOTE. We use finally keyword at the end of try/excet statements allow us to perform actions that we want 
# to occur regaaradless if whether or not an exception has been thrown.


# Dictionary mapping.
# note that python does not have switch/case statements but it can handle those using if/else statements, but for very long sets of conditions, it may worthwhile to use dictionary mapping instead.