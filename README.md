# isthissignif

Use _isthissignif_ to test whether or not your OLS regression model is "statistically significant" based on different criteria.

Note: this package is under development and currently only extends to OLS regression model objects generated using the statsmodels package.

## Why use _isthissignif_?

P-values are often used by researchers to gauge statistical significance — and while these measures useful, they are often misused or misinterpreted. Beyond this, the p-value is not the only meaningful statistical measure one can interpret from their model. 

In 2016, the American Statistical Association (ASA) released an updated statement on p-values. The ASA advocates for supplementing p-values with other statistical approaches, such as confidence intervals, likelihood ratios, effect sizes, etc.:

   >In view of the prevalent misuses of and misconceptions concerning p-values, some statisticians prefer to supplement or even replace p-values with other approaches. These include methods that emphasize estimation over testing, such as confidence, credibility, or prediction intervals; Bayesian methods; alternative measures of evidence, such as likelihood ratios or Bayes Factors; and other approaches such as decision-theoretic modeling and false discovery rates. All these measures and approaches rely on further assumptions, but they may more directly address the size of an effect (and its associated uncertainty) or whether the hypothesis is correct. (Wasserstein and Lazar 5)

_isthissignif_ provides a brief overview of select statistical measures in your model that might indicate significance. The package pulls your model's p-values, confidence intervals, and r-squared value from your regression output and provides a brief interpretation. In running your model through _isthissignif_, you will immediately have a jumping-off point for further analysis that extends beyond a p-value.

Ronald L. Wasserstein & Nicole A. Lazar (2016) The ASA's Statement on p-Values: Context, Process, and Purpose, The American Statistician, 70:2, 129-133, DOI: 10.1080/00031305.2016.1154108


## Installation

```bash
$ pip install isthissignif
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`isthissignif` was created by Gracen Bourbeau. It is licensed under the terms of the MIT license.

## Credits

`isthissignif` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
