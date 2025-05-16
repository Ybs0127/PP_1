inFp=None
inStr=""
i=1

inFp=open("/Users/youngbinsong/Desktop/example.txt", encoding="utf-8")

while True :
    inStr = inFp.readline()
    if inStr == "":
        break
    print(f"{i}:  {inStr}", end="")
    i += 1

inFp.close()