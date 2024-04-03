#while loops and for loops 

#while loops

# x=0
# while (x<=5):
#     print(x)
#     x+=1

# for loops

# for x in range(5,10):
#     print(x)

#array
days=["Mon","Tues","Wed","Thurs","Fri","Sat","Sun"]
for d in days:
    # if (d=="Fri"):break #Loop Stops
    if (d=="Fri"):continue #Skips d
    print(d)
        