import numpy, time, pandas
(p,q) = (1000, 1234567) # domain; database size.
print("p,q = ", (p,q))
r = numpy.random.randint
t = [(r(0,p),r(0,p),r(0,p)) for i in range(q)]
s = time.time()
u = [[(x,-z,y) for (x,y,z) in t if x == xf] for xf in range(p)]
print(time.time()-s, "seconds for partition")
s = time.time()
[i.sort() for i in u]
v = [(x,y) for i in u for (x,z,y) in i[:2]]
print(time.time()-s, "seconds for sorting, picking 2.") 
s = time.time()
[ensi, ensi_arvo, toka, toka_arvo] = [{},{},{},{}]
for (x,y,z) in t:
    if (x not in ensi):
        ensi[x] = y
        ensi_arvo[x] = z        
    elif (z > ensi_arvo[x]):
        (ensi[x],toka[x]) = (y,ensi[x])
        (ensi_arvo[x],toka_arvo[x]) = (z, ensi_arvo[x])
    elif (x not in toka) or ((z > toka_arvo[x]) and (z <= ensi_arvo[x])):
        toka[x] = y
        toka_arvo[x] = z
print(time.time()-s, "seconds for one interation.") 
w = [(k,v) for k , v in ensi.items()]+[(k,v) for k,v in toka.items()]
w.sort()
print(1-sum([(v[i] != w[i]) for i in range(len(v))])/len(v), "similarity")
s = time.time()
t1 = pandas.DataFrame(t, columns=["x", "y", "z"])
print(time.time()-s, "seconds for pandas")
s = time.time()
mz = t1.groupby("x")["z"].nlargest(2)
print(time.time()-s, "seconds for nlargest(2).") 
w1 = [(x, t[y][1]) for (x,y) in mz.index]
print(1-sum([(v[i] != w1[i]) for i in range(len(v))])/len(v), "similarity")




