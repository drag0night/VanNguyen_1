if __name__ == "__main__":
    fr = open('input.txt','r',encoding='utf8')
    dic = dict()
    for word in fr.read().split():
        if word not in dic:
            dic[word] = 1
        else:
            dic[word] += 1
    fr.close()
    fw = open("output.txt",'w',encoding="utf8")
    for count in dic:
        s = count + ": " + str(dic[count]) + "\n"
        fw.write(s)
    fw.close()