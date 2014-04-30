import operator

f = [x.strip() for x in open("/usr/share/dict/words").readlines() if len(x) > 3]

























f.sort(key=operator.itemgetter(1,0), reverse=True)
print f[0:2]
