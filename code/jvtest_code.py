# import nsfg
#
# df = nsfg.ReadFemPreg()
# # df = nsfg.CleanFemPreg(df)
#
# d = nsfg.MakePregMap(df)
#
# h = 0
# for i in d:
#     if 4 in df.outcome[d[i]].value_counts() and df.outcome[d[i]].value_counts()[4] >= 6:
#         h += 1
#
# print h

import thinkstats2
import thinkplot
import nsfg

hist = thinkstats2.Hist([1, 2, 2, 3, 5])
thinkplot.Hist(hist)

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]
hist = thinkstats2.Hist(live.birthwgt_lb, label="birthwgt_lb")
# thinkplot.Hist(hist)
# thinkplot.Show(xlabel='pounds', ylabel='frequency')
# thinkplot.Hist(hist)
# hist = thinkstats2.Hist(live.totalwgt_lb, label="birthwgt_lb")
# thinkplot.Hist(hist)
# hist = thinkstats2.Hist(live.totalwgt_lb, label="totalwgt_lb")
# thinkplot.Hist(hist)
# thinkplot.Hist(hist)
# for weeks, freq in hist.Smallest(10):
#     print(weeks, freq)

# thinkplot.Show(xlabel='weeks', ylabel='frequency')
# hist = thinkstats2.Hist(live.prglngth, label="preglen")
# thinkplot.Hist(hist)

firsts = live[live.birthord == 1]
others = live[live.birthord != 1]
first_hist = thinkstats2.Hist(firsts.prglngth)
other_hist = thinkstats2.Hist(others.prglngth)

width = 0.45
thinkplot.PrePlot(2)

# hist = thinkstats2.Hist(live.prglngth, label="preglen")
# first_hist = thinkstats2.Hist(firsts.prglngth)


thinkplot.Show(xlabel='weeks', ylabel='frequency', xlim=[27, 46])
thinkplot.PrePlot(2)
