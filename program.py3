import itertools
def main():
  Lt=[]
  people=list(input("Enter the people names : ").split())
  nc=int(input("Enter no of criteria : "))
  cond=[]
  for _ in range(nc):
    aa=list(input("Enter condition %d people names : "%(_+1)).split())
    bb=list(input("Enter condition %d Supporters : "%(_+1)).split())
    cc=list(input("Enter condition %d Killers : "%(_+1)).split())
    cond.append((aa,bb,cc))
  nb=int(input("Enter boat size : "))
  boaters=list(input("Enter the boaters names : ").split())
  Rt=people[:]
  stack=[[Lt[:],Rt[:],True]]
  def solved():
    return Rt==[]
  def check (tup):
    y,x,c1=tup[:]
    x,y=sorted(x[:]), sorted(y[:])
    for s in stack:
      a,b,c2=s
      if c1==c2 and a==x and b==y:
        return False
    return True
  def minus(x,y):
    tmp=x[:]
    for i in y:
     if i in tmp:
      tmp.remove(i)
    return tmp
  def movable (move, boo):
    for movei in move:
      if movei in boaters:
        break
    else:
        return False
    for i in (Rt+move,minus(Lt, move)) if boo else (minus (Rt, move),Lt+move):
      for condi in cond:
         a,b,c=condi
         if set(a)&set(i) and not set(b)&set(i) and set(c)&set(i):
           return False
    if not check((Rt+move,minus(Lt, move),True) if boo else (minus (Rt, move),Lt+move,False)):
      return False
    return True
  def possibilities (boo):
    for j in range(1,nb+1):
     for i in itertools.combinations(Lt if boo else Rt,j):
      if movable(list (i), boo):
        yield list(i)
  def game (boo=False):
    if solved(): return True
    for i in list(possibilities(boo)):
      for j in i:
         (Lt if boo else Rt).remove(j)
         (Rt if boo else Lt).append(j)
      stack.append([sorted (Lt)[:], sorted(Rt)[:], boo])
      if game(not boo):
         return True
      else:
        stack.pop()
        for j in i:
         (Rt if boo else Lt).remove(j)
         (Lt if boo else Rt).append(j)
    return False
  print (game (),stack)
  for s in range(len(stack)-1):
    if stack[s][2]:
            temp=minus(stack[s+1][0],stack[s][0])
            print("MOVE LEFT :"+", ".join(temp))
    else:
            temp=minus(stack[s+1][1],stack[s][1])
            print("MOVE RighT :"+", ".join(temp))
if __name__=="__main__":
  main()
  input()
