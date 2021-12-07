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




