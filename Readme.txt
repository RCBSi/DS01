https://stackoverflow.com/questions/39066260/get-first-and-second-highest-values-in-pandas-columns

Generate t = [... 
   (63365, 53233, 247),
   (74604, 83070, 1012),
   (61472, 41692, 62835),
   (106017, 116489, 107798),
   (45339, 43857, 63219),
   (20541, 3691, 94150),
   (101563, 122074, 23075),
   (43113, 73382, 47338),
   (1603, 89503, 83820),
   (36920, 83218, 52348) ... ]

A q-by-3 matrix of random integers; a list of q triples. The integers range from 0 to p-1 inclusive, and the length of t is q. 

Name the columns: 
  pandas.DataFrame(t, columns=["x", "y", "z"])

For each x, return two values of y for which the z value is as high as possible:



[... (617, 72139), (617, 60587), (618, 32521), (618, 109437) ... ]

Here the value x = 617 is output along with two y values for which a high z value has been observed. 
The two values of y must be different. 

The length of the output is about 2p tuples, and it is shorter exactly in the case that some value of x was not randomly created at least 
twice. 

If we look also at the z values for the rows that are chosen, we will notice that they are all near p:


[t[y] for (x,y) in mz.index[14234:14248]]

[(7117, 122775, 123133),
 (7117, 59412, 121499),
 (7118, 83771, 122861),
 (7118, 68750, 122261),
 (7119, 90341, 122813),
 (7119, 97641, 120786),
 (7120, 39384, 123436),
 (7120, 75910, 122322),
 (7121, 28462, 123278),
 (7121, 19352, 121052),
 (7122, 118341, 123316),
 (7122, 67250, 123232),
 (7123, 12600, 122557),
 (7123, 52992, 121454)]

Note that the index 14234//2 == 7117, i.e. mz has exactly two rows for each x value. 
