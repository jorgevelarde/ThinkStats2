import nsfg

df = nsfg.ReadFemPreg()
# df = nsfg.CleanFemPreg(df)

d = nsfg.MakePregMap(df)

h = 0
for i in d:
    if 4 in df.outcome[d[i]].value_counts() and df.outcome[d[i]].value_counts()[4] >= 6:
        h += 1

print h
