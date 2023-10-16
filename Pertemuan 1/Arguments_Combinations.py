def f(a, *b, c=6, **d): 
   print(f"a: {a}")
   print(f"b: {b}")
   print(f"c: {c}")
   print(f"d: {d}")

f(1, 2, 3, x=4, y=5)
f(1, 2, 3, c=7, x=4, y=5)