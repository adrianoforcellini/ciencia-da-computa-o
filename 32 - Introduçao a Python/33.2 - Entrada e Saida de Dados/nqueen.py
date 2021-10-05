import sys
n = 8

x = [-1 for x in range(n)]

def safe(k,i):
    for j in range(k):
          if x[j] == i  or abs(x[j] - i) == abs(k - j) :
            return False
    return True

def nqueen(k):
  for i in range(n):
        if safe(k,i):
            x[k] = i 
            if k == n-1:
              print ("SOLUTION", x)
            else:
                nqueen(k+1)

nqueen(0)