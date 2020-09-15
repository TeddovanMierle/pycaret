from build.lib.pycaret.classification import interpret_model
import os, sys

from pycaret.classification import plot_model
sys.path.insert(0, os.path.abspath(".."))

import pandas as pd
import pytest
import pycaret.classification
import pycaret.datasets

def test():
    # loading dataset
    data = pycaret.datasets.get_data('juice')
    assert isinstance(data, pd.core.frame.DataFrame)

    # init setup
    clf1 = pycaret.classification.setup(data, target='Purchase', log_experiment=True, silent=True, html=False, session_id=123, fold=2)
    
    model = pycaret.classification.create_model('lr')

    available_plots = [
        "parameter",
        "auc",
        "confusion_matrix",
        "threshold",
        "pr",
        "error",
        "class_report",
        "rfe",
        "learning",
        "manifold",
        "calibration",
        "vc",
        "dimension",
        "feature",
        "boundary",
        "lift",
        "gain",
    ]

    for plot in available_plots:
        plot_model(model, plot=plot)

    models = [pycaret.classification.create_model('et'), pycaret.classification.create_model('xgboost')]

    available_shap = ["summary", "correlation", "reason"]

    for model in models:
        for plot in available_shap:
            interpret_model(model, plot=plot)

    assert 1 == 1
    
if __name__ == "__main__":
    test()
