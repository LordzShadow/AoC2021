### Decode input :)  
Z is a stack where pop is `val = z%26; z = z//26` and 
push is `z = z*26+value`

There basically is two kinds of modules in the input.  
- 1st module only pushes a value to the stack
- 2nd module pushes if the popped value + something is not equal to the digit
- There are 7 of both and we want the stack to be empty in the end
- So we want 7 pushes and 7 pops aka 2nd module value must equal popped + something. 

`ABCDEFGHIJKLMN` - digit representation  
```python
z.push(A+0)
z.push(B+6)
z.push(C+4)
z.push(D+2)
z.push(E+9)
if F != z.pop()-2:
    z.push(F + 1)
z.push(G + 10)
if H != z.pop()-15:
    z.push(H + 6)
if I != z.pop()-10:
    z.push(I + 4)
z.push(J + 6)
if K != z.pop()-10:
    z.push(K + 3)
if L != z.pop()-4:
    z.push(L + 9)
if M != z.pop()-1:
    z.push(M + 15)
if N != z.pop()-1:
    z.push(N + 5)

F = E+9-2 = E+7
H = G+10-15 = G-5
I = D+2-10 = D-8
K = J+6-10 = J-4
L = C+4-4 = C
M = B+6-1 = B+5
N = A+0-1 = A-1
```

#### 94992994195998 MAX  
#### 21191861151161 MIN  

Maths is cuul
