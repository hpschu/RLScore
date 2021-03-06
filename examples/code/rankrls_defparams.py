import numpy as np
from rlscore.learner.all_pairs_rankrls import AllPairsRankRLS
from rlscore.reader import read_sparse
from rlscore.reader import read_sparse
from rlscore.measure import cindex
train_labels = np.loadtxt("./examples/data/rank_train.labels")
test_labels = np.loadtxt("./examples/data/rank_test.labels")
train_features = read_sparse("./examples/data/rank_train.features")
test_features = read_sparse("./examples/data/rank_test.features")
kwargs = {}
kwargs["train_labels"] = train_labels
kwargs["train_features"] = train_features
kwargs["regparam"] = 1
learner = AllPairsRankRLS.createLearner(**kwargs)
learner.train()
model = learner.getModel()
P = model.predict(test_features)
test_perf = cindex(test_labels, P)
print "test set performance: %f" %test_perf
