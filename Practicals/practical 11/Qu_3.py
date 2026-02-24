# Write  a  Python  program  to  perform  following  operations  on  set:  intersection  of sets, union of sets, set difference, symmetric difference, clear a set.

yash = {'ai','tech','MAANG','Family','curiosity'}
sr = {'chocolate','Family','Business','traveling','health'}

# Union
sm = yash.union(sr)
print("union: ",sm)

# Intersection
sm = yash.intersection(sr)
print("intersection: ",sm)

# symmetric difference
sm = yash.symmetric_difference(sr)
print("symmetric_difference: ",sm)

# clear
sr.clear()
print("clearing a set: ",sr)