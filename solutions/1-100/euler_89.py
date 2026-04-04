import pathlib
import time
from math import *
from scripts.divisors import properDivisorsOf
from scripts.primes import primesUntilN

def numeralToNumber(numeral:str):
    og_numeral = numeral
    number = 0
    special = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
    specialValues = [4, 9, 40, 90, 400, 900]
    for i in range(6):
        if special[i] in numeral:
            numeral = ''.join(numeral.split(special[i]))
            number += specialValues[i]
    symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    symbolValues = [1, 5, 10, 50, 100, 500, 1000]
    for i in range(7):
        number += symbolValues[i]*numeral.count(symbols[i])
    return number
    

def numberToNumeral(number):
    numeral = ''
    numeral += number//1000 * 'M'
    number = number%1000
    if number >= 900:
        numeral += 'CM'
        number -=900
    else:
        numeral += number//500 * 'D'
        number = number%500
    if number>=400:
        numeral += 'CD'
        number -= 400
    else:
        numeral += number // 100 * 'C'
        number = number % 100
    if number >= 90:
        numeral += 'XC'
        number -= 90
    else:
        numeral += 'L' * (number //50)
        number = number % 50
    if number >= 40:
        numeral += 'XL'
        number -= 40
    else:
        numeral += 'X' * (number // 10)
        number = number % 10
    if number == 9:
        numeral += 'IX'
        number -= 9
    elif number == 4:
        numeral += 'IV'
        number -= 4
    else:
        numeral += number // 5 * 'V'
        number = number % 5
        numeral += 'I' * number
        number = number % 1
    if number != 0:
        input('ERROR')
        return None
    return numeral
    

def Euler89():
    numeralsString = pathlib.Path('./resources/roman.txt').read_text()
    numerals = numeralsString.split('\n')
    shorterNumerals = []
    for numeral in numerals:
        number = numeralToNumber(numeral)
        shortNumeral = numberToNumeral(number)
        check = numeralToNumber(shortNumeral)
        if check != number:
            input((numeral, number, shortNumeral, check))
        shorterNumerals.append(shortNumeral)
    charsB4 = len(''.join(numerals))
    charsAfter = len(''.join(shorterNumerals))
    return charsB4 - charsAfter

start = time.time()
print(Euler89())
print(f'Took {time.time()-start}s')