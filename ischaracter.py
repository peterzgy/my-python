# coding = utf-8
def ischa(str):
    for c in str:
        if not("\u4e00" <= c <= "\u9fa5"):
            return False
    return True
#print(ischa("123ASC"))
#print(ischa("汉字"))
