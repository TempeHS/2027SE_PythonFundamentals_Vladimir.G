# Learning python from lecture

"""
Is a comment

end='/n' is new line
end=' ' allows for myself to add something to the end
e.g end='???' Output would be Hello ??? placeholder

parameters are named variables

error messages can be misleading

Can use single or double quotes, be consistent

put / in front of quotation marks to computer to know
they are literal quotes
called escaping

print("Hello, \"friend\"")

print(f"Hello, {name}")
{} are f strings, tells python to format

strings come with pre built functionalities,
Allows us to format and fix up texts entered
by a user

e.g name = name.strip() (Removes whitespace from str)
e.g name = name.capitalize() (Capitalize)
e.g name = name.title() (Capitalize first letter of each word)
e.g name = name.title().strip()

name.split(" ")

= is a assignment, assigns the right value t the left

up arrow in terminal copy's last inputted message

int an interger is a number

signs which can be uses

+
-
*
/
%

interactive mode for python is >>>
code will be executed straight away

e.g >>> 1 + 1
    = 2

Incremently is better than this

A feature worth knowing


"""

# Ask user for name
name = input("What's your name? ")

# Say hello to user
print("Hello, " + name)
