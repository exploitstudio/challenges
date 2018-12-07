import sys
import random
import math
from Crypto.Util import number

p = number.getPrime(9,None)
g = random.randint(5,200)
x = random.randint(0,p-1)
y = random.randint(0,p-1)

aliceKey = pow(g,x,p)
bobKey = pow(g,y,p)

alicePriv = pow(bobKey,x,p)
bobPriv = pow(aliceKey,y,p)

if bobPriv != alicePriv:
    print"Whoah! Something is terribly wrong."
else:
    print "\n"

print "g = " +str(g)
print "p = " +str(p)
print "Alice's public key: " +str(aliceKey)
print "Bob's public key : " +str(bobKey)

answer = raw_input("\nWhats the secret? ")

if int(answer) == alicePriv:
    print "Correct! Now shoo."
else:
    print "Thats wrong!"
