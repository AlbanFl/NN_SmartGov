import string

GROUP_ID = 31
CONFIG_SIZE = 48
CHARS = [0,1,2,3,4,5]
N = 500
N_ENV2 = 200
MIX_THRESHOLD = 0.9
MAXGEN = 30
e = 10
p_cross = 0.8
p_mut = 0.02
# "wheel" ou "tournament"
SELECT_FUNCTION = "tournament"
TOURNAMENT_SIZE = 4
TOURNAMENT_P = 0.9
# "slice" ou "merge"
CROSS_FUNCTION = "slice"
n_test=1

#simulation
base_pollution = 8935