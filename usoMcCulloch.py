import McCullochPitts as m

mp = m.McCullochPitts(2, "OR", 100)

mp.train()

mp.evaluate([0, 1])

mp.truth_table_check()


