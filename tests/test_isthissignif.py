from isthissignif import isthissignif
import statsmodels.api as sm
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

def test_isthissignif():
    mtcars = sm.datasets.get_rdataset("mtcars", "datasets", cache=True).data
    df = pd.DataFrame(mtcars)
    model1 = smf.ols(formula='mpg ~ cyl', data=mtcars).fit() 

    assert (isthissignif.isthissignif(model1)[0] == 'R-sqr: Variables predict 50% or more of variability in Y')
    assert (isthissignif.isthissignif(model1)[1] == 'P-value(s): There is more than a 5% chance that the p-values of these variables do not happen by chance')
    assert (isthissignif.isthissignif(model1)[2] == 'CIs: 95% confidence interval does not contain zero')