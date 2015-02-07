print("Miles Kilometers Kilometers Miles")
for miles in range(1,11):
    km = miles * 1.609
    print("{0:<6}{1:<11.3f}{2:<11}{3:<5.3f}".format(int(miles), km, 20+(miles-1)*5, (20+(miles-1)*5)/1.609))
