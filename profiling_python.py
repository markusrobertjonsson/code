# In Python 3.10.5

import cProfile

pr = cProfile.Profile()
pr.enable()

# DO STUFF

pr.disable()
s = io.StringIO()
ps = pstats.Stats(pr, stream=s).sort_stats(SortKey.CUMULATIVE)
ps.print_stats(10)
print(s.getvalue())


# ALT
# with cProfile.Profile() as pr:
#     DO STUFF
#     pr.sort_stats(SortKey.CUMULATIVE).print_stats(20)
