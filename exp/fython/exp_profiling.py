import pstats

p = pstats.Stats('/home/neb/temp')

p.sort_stats('tottime')

p.print_stats(.1)

# p.print_callees()

# p.print_callers('_io.FileIO')
# p.print_callees('_io.FileIO')
# p.print_callers('load')