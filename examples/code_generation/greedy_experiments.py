cfiles = {"train_features":'./examples/data/class_train.features',
                          "train_labels":'./examples/data/class_train.labels',
                          "test_features":'./examples/data/class_test.features',
                          "test_labels":'./examples/data/class_test.labels'}

defparams = {"train_features":"train_features", "train_labels":"train_labels", "test_features":"test_features", "test_labels":"test_labels"}

experiments = {"greedyrls":{
                "learner":"GreedyRLS",
                "lpath":"rlscore.learner.greedy_rls",
                "measure":"auc",
                "lfparams": defparams,
                "lparams": {"regparam":1, "bias":1, "subsetsize":10, "use_default_callback":True, "test_measure":"auc"},
                "files": cfiles},
               }

