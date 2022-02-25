P = input("Principal or ?: ")
R = input("Rate or ?: ")
T = input("Time or ?: ")
SI = input("Simple interest or ?: ")
try:
   c= 0
   while P != "?":
       c= c+1
       break
   while R != "?":
       c = c+1
       break
   while T != "?":
       c = c+1
       break
   while SI != "?":
       c = c+1
       break

   if c == 3:
       print("correct")
       if SI == "?":
           P = float(P)
           R = float(R)
           T = float(T)

           x1 = f"SI = (PRT)/100)"
           print(x1)
           x1 = f">> = ({P}*{R}*{T})/100"
           print(x1)
           x1 = f">> = ({P * R * T})/100"
           print(x1)
           x1 = f">> {(P * R *T)/100}"
           print(x1)
           print("Simple Interest = ", x1)
       elif P == "?":
           SI = float(SI)
           R = float(R)
           T = float(T)

           x1 = f"SI = (PRT)/100)"
           print(x1)
           x1 = f"P = (100*SI)/(T*R)"
           print(x1)
           x1 = f">> = ({100}*{SI})/({T}*{R})"
           print(x1)
           x1 = f">> = ({100 * SI})/({T*R})"
           print(x1)
           x1 = f">> {(100*SI)/(T * R)}"
           print(x1)
           print("Principal = ", x1)
       elif R == "?":
           SI = float(SI)
           P = float(P)
           T = float(T)

           x1 = f"SI = (PRT)/100)"
           print(x1)
           x1 = f"R = (100*SI)/(T*P)"
           print(x1)
           x1 = f">> = ({100}*{SI})/({T}*{P})"
           print(x1)
           x1 = f">> = ({100 * SI})/({T*P})"
           print(x1)
           x1 = f">> {(100*SI)/(T * P)}"
           print(x1)
           print("Rate = ", x1)

       elif T == "?":
           SI = float(SI)
           P = float(P)
           R = float(R)

           x1 = f"SI = (PRT)/100)"
           print(x1)
           x1 = f"T = (100*SI)/(R*P)"
           print(x1)
           x1 = f">> = ({100}*{SI})/({R}*{P})"
           print(x1)
           x1 = f">> = ({100 * SI})/({R*P})"
           print(x1)
           x1 = f">> {(100*SI)/(R * P)}"
           print(x1)
           print("Time = ", x1)

   else:
       print("More than one unknown variable ")
except:
    print("Error something went wrong")