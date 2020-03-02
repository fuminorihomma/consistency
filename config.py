class Config:
    dialogAct_model_dir = "./classifier/best_model_state_er.pkl"

debug = True
repetition_threshold = 0.5

# select_candidates_strategy
RANDOM_SELECT = "random_select"
REPETITION_RATIO = "repetition_ratio"
candidate_select_strategy = REPETITION_RATIO

# num of candidates to select from
NUM_CANDIDATES = 10
MAX_NUM_CANDIDATES = 20


# human rule configuration
HAVE_TO_PROPOSE = 3

PASS = "pass"
REPETITION = "repetition"
CONTRADICTION = "contradiction"