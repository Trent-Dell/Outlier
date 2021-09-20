'''
3 standard deviations from the mean is a common cut-off 
for identifying outliers in a Gaussian or Gaussian-like distribution. 
For smaller data samples: 2 standard deviations (95%)
For larger samples, typically 4 standard deviations (99.9%) or more
It depends!!!
'''
#%%
from scipy.stats.stats import median_absolute_deviation, percentileofscore


def std_dev_outliers(data):
    from numpy import mean
    from numpy import std

    # make this user defined in another increment
    numSD = 3

    data = ""
    dataMean, dataStd = mean(data), std(data)
    cutoff = dataStd * numSD
    lower, upper = dataMean - cutoff, dataMean + cutoff

    # look for data in the tails of the cutoff
    outliers = [x for x in data if x < lower or x > upper]
    print(f"Outliers observed: {len(outliers)}")
    outliersRemoved =  [x for x in data if x >= lower and x <= upper]
    print(f"Non-outlier observed: {len(outliersRemoved)}")

    return outliers, outliersRemoved
# %%
from numpy import percentile

def IQR (data):
    q25, q75 = percentile(data, 25), percentile(data, 75)
    iqr = q75 - q25
    cutoff = iqr * 1.5
    lower, upper = q25 - cutoff, q75 + cutoff
    outliers = [x for x in data if x < lower or x > upper]
    print(f"Outliers observed: {len(outliers)}")
    outliersRemoved =  [x for x in data if x >= lower and x <= upper]
    print(f"Non-outlier observed: {len(outliersRemoved)}")
# %%
def local_outlier_factor():
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.neighbors import LocalOutlierFactor
    from sklearn.metrics import mean_absolute_error

    file = "/data/weight.xlsx"
    df = pd.read_excel(file, header = None)
    data = df.values
    # split into input and output elements
    X, y = data[:, :-1], data[:, -1]
    print(X.shape, y.shape) # summarize data set shape
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=1)
    print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

    model = LinearRegression()
    model.fit(X_train, y_train)
    # evaluate model
    yhat = model.predict(X_test)
    # evaluate predictions
    mae = mean_absolute_error(y_test, yhat)
    print(f"Mean Absolute Error: {mae:.3f}")

    # find outliers in the training data set
    lof = LocalOutlierFactor()
    yhat = lof.fit_predict(X_train)

    # select all rows that aren't outliers
    mask = yhat != -1
    X_train, y_train = X_train [mask, :], y_train[mask]
# %%

# %%

# %%
