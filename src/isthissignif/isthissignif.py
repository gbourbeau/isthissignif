import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

def isthissignif(lm):
    """
    Generates brief interpretations of statistical measures for regression models.
    
    Parameters
    ----------
    lm : statsmodels.regression.linear_model.RegressionResultsWrapper
      An OLS regression model from package statsmodels.formula.api that you wish to interpret for significance.
      
    Returns
    -------
    r_res: str
      A brief interpretation of your model's R-squared value.
      
    p_res: str
      A brief interpretation of your model's p-value(s).
      
    conf_res: str
      A brief interpretation of your model's confidence intervals.
      
    Example
    --------
    >>> #importing mtcars dataset from statsmodels
    >>> import statsmodels.api as sm
    >>> mtcars = sm.datasets.get_rdataset("mtcars", "datasets", cache=True).data
    
    >>> #create regression model for mtcars data using statsmodels.formula.api package
    >>> import statsmodels.formula.api as smf
    >>> mtcars_model = smf.ols(formula='mpg ~ cyl', data=mtcars).fit()
    
    >>> from isthissignif import isthissignif 
    >>> isthissignif.isthissignif(mtcars_model)
    ('R-sqr: Variables predict 50% or more of variability in Y',
    'P-value(s): There is more than a 5% chance that the p-values of these variables do not happen by chance',
    'CIs: 95% confidence interval does not contain zero')  
    """
    
    rsq = lm.rsquared 
    if rsq > 0.5: 
        r_res ="R-sqr: Variables predict 50% or more of variability in Y"
    else:
        r_res ="R-sqr: Variables predict less than 50% of variability in Y"
    pvals = pd.Series(lm.pvalues[-1]) 
    for i in pvals:
        if i > 0.05:
            p_res="P-value(s): There is more than a 5% chance that the p-values of these variables happen by chance"
        else:
            p_res="P-value(s): There is more than a 5% chance that the p-values of these variables do not happen by chance"
    conf=lm.conf_int(alpha=0.05, cols=None)
    for i in conf:
        if (conf.iloc[i, 0] <= 0 <= conf.iloc[i, 1]):
            conf_res="CIs: 95% confidence interval contains zero."
        else:
            conf_res="CIs: 95% confidence interval does not contain zero"
    return(r_res,p_res,conf_res)