# Regular expressions are expressions that define a search pattern: remember the grep command in ubuntu?
# https://pythex.org to test our expressions
# https://www.debuggex.com/cheatsheet/regex/python for char sets
# mostly used in validations
# TODO Regex explaination: https://regex101.com
# search() --> searchs a string for a match and returns the first match only
# findall() --> returns a list of all matches and returns an empty list if there are no matches
# to use regex: import re
# re.span() returns the position of the match
# re.string() returns the string that you're searching within
# re.group() returns the group that has the matches
# re.split() returns a list that contains the string with each match splitted, can also take a maxsplit
# re.sub() replaces each match with anything that we want, can also take a max replace
#! each of these commands take (pattern,string,max,flags)
# groups in regular expressions are pretty important
# re.group(<group number>) returns the group that got matched
# re.groups() returns all the groups that got matched
# * re flags: IGNORECASE (case insensitive), VERBOSE (allows commenting within the regular expression), DOTALL (since "." matches everything but the newline, this allows to match the newline as well), MULTILINE (default is it searchs from the start of the line the end of the line, this allows to search all lines)
# ----------------
# an object consists of attributes: things that "define" the object; and also consists of methods: what the object DOES
# a class can be defined as a blueprint/object constructor
# class instantiate means to create an instance of your object
# class keyword is used to define classes, class names are usually written in PascalCase (UpperCamelCase)
# each time you create an object from class, python uses a method called __init__ (stands for initialize)
# any method that starts and ends with an underscore is called a dunder/magic method
# * we define our first method in our class called __init__ with a MUST parameter called self (current instance of the object)
# self can be anything
# to create an object we use new()
# syntax
# class Name:
#     Constructor => Does the instantation (Creates instance from a class)
#     Each instance is a seperate object
#     def __init__(self, other data) -> None:
#         body of function
# to know which variable is under which class we use __class__
