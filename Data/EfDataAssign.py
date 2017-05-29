writeObj = open("EfGraphData.txt", "a")

#I need a way to take this data and save it to the inObj Object from Labview over wifi

inObj = "1.111, 125.200, 3.300, 0.000, 53.000"
SplObj = inObj.split(",")
time = SplObj[0]
ef = SplObj[4]

#convert to coordinates
value = str(time + "," + ef)

#write to file
writeObj.write(value)
writeObj.close()
