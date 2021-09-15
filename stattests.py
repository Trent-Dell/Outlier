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
def normality_tests():
    return

def shapiro_wilk_test():
    return

def dAngostino_k2_test():
    return

def anderson_darling_test():
    return

def correlation_tests():
    return

def pearson_corr_coeff():
    return

def spearman_rank_corr():
    return

def kendall_rank_corr():
    return

def chi_square():
    return

def sationary_test():
    return

def augmented_dickey_fuller():
    return

def kwiatkowski_phillips_schmidt_shin():
    return

def parametric_statistical_hypothesis_tests():
    return

def student_t_test():
    return

def paired_student_t_test():
    return

def ANOVA():
    return

def repeated_measures_ANOVA():
    return

def nonparametric_statistical_hypothesis_tests():
    return

def mann_whitney_u_test():
    return
    
def wilcoxon_signed_rank_test():
    return

def kruskal_wallis_h_test():
    return

def friedman_test():
    return
    
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
    df = pd.read_excel('data/weight.xlsx')     # load data into df
    return df

#%%
# Shapiro-wilk normality test
def shapiro_wilk_test(df):
    choice = "Y"
    while choice.upper() == "Y":
        try:
            CI = float(input(
                f"You're about to perform a normality check.  Which Confidence Interval do you desire?\n"
                f"Enter value between 0.0 and 1.0: "
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
#%%
# extract feature for analysis
def weight_feature():
    weightDF = 
    return weightDF

"""
For future created select feature function
1. iterate through file, extract feature names
2. load into list
3. select one feature for this; future version to allow selection of multiple features
"""
#%%
def menu():
    print(
        f"""
        Menu
        ------------------------------------------------
        1.  Normality Tests
        2.  Shapiro-Wilk Test
        3.  D’Agostino’s K^2 Test
        4.  Anderson-Darling Test
        5.  Correlation Tests
        6.  Pearson’s Correlation Coefficient
        7.  Spearman’s Rank Correlation
        8.  Kendall’s Rank Correlation
        9.  Chi-Squared Test
        10. Stationary Tests
        11. Augmented Dickey-Fuller
        12. Kwiatkowski-Phillips-Schmidt-Shin
        13. Parametric Statistical Hypothesis Tests
        14. Student’s t-test
        15. Paired Student’s t-test
        16. Analysis of Variance Test (ANOVA)
        17. Repeated Measures ANOVA Test
        18. Nonparametric Statistical Hypothesis Tests
        19. Mann-Whitney U Test
        20. Wilcoxon Signed-Rank Test
        21. Kruskal-Wallis H Test
        22. Friedman Test
        """
    )
    test = int(input("\nWhich test do you want to run? "))

    while True:
        if test == 1:
            normality_tests()
        elif test == 2:
            shapiro_wilk_test()
        elif test == 3:
            dAngostino_k2_test()
        elif test == 4:
            anderson_darling_test()
        elif test == 5:
            correlation_tests()
        elif test == 6:
            pearson_corr_coeff()
        elif test == 7:
            spearman_rank_corr()
        elif test == 8:
            kendall_rank_corr()
        elif test == 9:
            chi_square()
        elif test == 10:
            sationary_test()
        elif test == 11:
            augmented_dickey_fuller()
        elif test == 12:
            kwiatkowski_phillips_schmidt_shin()
        elif test == 13:
            parametric_statistical_hypothesis_tests()
        elif test == 14:
            student_t_test()
        elif test == 15:
            paired_student_t_test()
        elif test == 16:
            ANOVA()
        elif test == 17:
            repeated_measures_ANOVA()
        elif test == 18:
            nonparametric_statistical_hypothesis_tests()
        elif test == 19:
            mann_whitney_u_test()
        elif test == 20:
             wilcoxon_signed_rank_test()
        elif test == 21:
            kruskal_wallis_h_test()
        elif test == 22:
            friedman_test()


    return test
# %%
def main():
    test = menu(value)

# %%
if __name__ == '__main__':
    main()
# %%
