#Software Nuggets - Youtube Video 

#Sieve of Eratosthenes is a method to find the prime numbers and 
#composite numbers among a group of numbers (<10M)
#
#This method was introduced by Greek Mathematician Eratosthenes 
#in the third century B.C.

n=1751
inputList = list( range(3, n, 2))

#init primeNumbersList with two
primeNumbersList = [2]

while inputList:
    nextNum = inputList.pop(0)  
    primeNumbersList = primeNumbersList + [nextNum]

    if(nextNum*nextNum > n):
        primeNumbersList = primeNumbersList + inputList
        inputList = []
    else:
        for element in inputList:
                if(element % nextNum) == 0:
                    inputList.remove(element)

print(primeNumbersList)