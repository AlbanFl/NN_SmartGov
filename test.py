f = open("config.txt", "r")
content = f.readlines()
f.close()
cpt = 0
maxPoll = -999.0
minPoll = 9999.0
maxSat = -999.0
minSat = 99999.0
#cpt = 0
for line in content:
    line = line.strip("\n")
    tmp = line.split(":")
    poll = float(tmp[1].split("_")[0])
    sat = float(tmp[1].split("_")[1])
    if poll > maxPoll:
        maxPoll = poll
    if poll < minPoll:
        minPoll = poll
    if sat > maxSat :
        maxSat = sat
    if sat < minSat :
        minSat = sat

print("Min sat : ", minSat)
print("Max sat : ", maxSat)
print("Min poll : ", minPoll)
print("Max poll : ", maxPoll)