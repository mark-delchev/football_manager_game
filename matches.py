from match_simulation import *

match_instance = Match()
for i in range(100):
    result = match_instance.simulate_match("CSKA-45", "Real Madrid-97")
    if match_instance.t1_goals >= match_instance.t2_goals:
        print(result)
