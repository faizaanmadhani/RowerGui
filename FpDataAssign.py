writeObj = open("FpGraphData.txt", "a")

#I need a way to take this data and save it to the inObj Object from Labview

## takeObj = open("samplefile.txt", "r")

inObj = "1.111, 125.200, 3.300, 0.000, 53.000"
SplObj = inObj.split(",")
time = SplObj[0]
fp = SplObj[1]

#convert to coordinates
value = str(time + "," + fp + "\n")

#write to file
writeObj.write(value)
writeObj.write("\n")
writeObj.close()
