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


#### VBA CODE ###
#### Remove this code from file to compile Python code ##
Sub loadNumbers()

    Dim ws As Worksheet
    Set ws = Worksheets("Sheet1")
    
    num = 3
    
    For r = 1 To 35
    
        For c = 1 To 25
        
            ws.Cells(r, c) = num
            num = num + 2
        Next c
    Next r
    
    MsgBox Math.Sqr(num)
End Sub

Sub remove_mod()
    Dim ws As Worksheet
    Set ws = Worksheets("Sheet1")
    
    Dim myArray() As Variant
    myArray = Array(3, 5, 7, 9, 11, 13, 17, 19, 23, 29, 31, 37, 41, 42)
    
    For a = 0 To UBound(myArray)
        
        
        For r = 1 To 35
        
            For c = 1 To 25
            
                If ws.Cells(r, c) = myArray(a) Then
                    'skip
                ElseIf ws.Cells(r, c) Mod myArray(a) = 0 Then
                    ws.Cells(r, c) = ""
                End If
            Next c
        Next r
    Next a
End Sub

Sub remove_mod_n_only()
    Dim ws As Worksheet
    Set ws = Worksheets("Sheet1")
    
    Dim myArray() As Variant
    myArray = Array(3)
    
    For a = 0 To UBound(myArray)
        
        
        For r = 1 To 35
        
            For c = 1 To 25
            
                If ws.Cells(r, c) = myArray(a) Then
                    'skip
                ElseIf ws.Cells(r, c) Mod myArray(a) = 0 Then
                    ws.Cells(r, c) = ""
                End If
            Next c
        Next r
    Next a
End Sub


Sub show_prime()
    Dim ws As Worksheet
    Set ws = Worksheets("Sheet1")
    
    Dim offset As Integer
    offset = 1
    
    For r = 1 To 35
    
        For c = 1 To 19
        
            If ws.Cells(r, c) > 0 Then
                ws.Cells(offset, 27) = ws.Cells(r, c)
                offset = offset + 1
            End If
        Next c
    Next r
End Sub
