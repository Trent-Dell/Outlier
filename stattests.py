'''
Normality Tests
Shapiro-Wilk Test
D’Agostino’s K^2 Test
Anderson-Darling Test
Correlation Tests
Pearson’s Correlation Coefficient
Spearman’s Rank Correlation
Kendall’s Rank Correlation
Chi-Squared Test
Stationary Tests
Augmented Dickey-Fuller
Kwiatkowski-Phillips-Schmidt-Shin
Parametric Statistical Hypothesis Tests
Student’s t-test
Paired Student’s t-test
Analysis of Variance Test (ANOVA)
Repeated Measures ANOVA Test
Nonparametric Statistical Hypothesis Tests
Mann-Whitney U Test
Wilcoxon Signed-Rank Test
Kruskal-Wallis H Test
Friedman Test
'''
#%%
def import_data(data):
    # load libraries
    import os
    import pandas as pd

    # set path if not already extant
    path = "data/temp"     
    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed; it already exists." % path)
    df = pd.read_csv('data/')     # load data into df
    return df

#%%
# Shapir-wilk normality test
def shapiro_wilk_test(df):
    choice = "Y"
    while choice.upper() == "Y":
        try:
            CI = float(input(
                f"You're about to perform a normality check.  Which Confidence Interval do you desire?\n"
                f"Enter value between 0.0 and 0.1: "
            ))
            if 0 > CI or CI > 1.0:
                raise ValueError
        except ValueError:
            print ("Only enter a value between 0.0 and 0.1.")
        choice = input("Would you like to try again? (Y/N) ")

    from scipy.stats import shapiro
    stat, p = shapiro(df)
    print(f"{stat:.4f}, {p:.4f}")
    if p > CI:
        print('Probably Gaussian')
    else:
        print("Probably not Gaussian")
# %%
def main():
    shapiro_wilk_test()
# %%
if __name__ == '__main__':
    main()