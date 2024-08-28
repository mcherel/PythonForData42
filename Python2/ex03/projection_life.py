import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import load_csv

def main():
    f_inflat = "../csv_files/income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    f_life = "../csv_files/life_expectancy_years.csv"
    
    chosen_y = "1900"
    gdp = load_csv.load(f_inflat)
    expectancy = load_csv.load(f_life)
    """  X = data['km'].values.reshape(-1, 1)
    y = data['price'].values.reshape(-1, 1)
    """
    idx = np.where(expectancy[0] == chosen_y)[0][0]
    data = {}
    data['x'] = gdp[1:, idx].tolist()
    data['y'] = expectancy[1:, idx].tolist()
    # converting to dataframe
    df = pd.DataFrame(data)

    # converting columns to numeric, coercing errors to NaN
    df['x'] = pd.to_numeric(df['x'], errors='coerce')
    df['y'] = pd.to_numeric(df['y'], errors='coerce')

    # drop rows with Nan values
    df_clean = df.dropna()

    # data generation
    x = np.concatenate([np.linspace(300, 1000, 6, endpoint=False), np.linspace(1000, 10000, 8)])
    y = np.random.uniform(1, 10, size=x.shape)
    # plot the scatter plot
    plt.scatter(df_clean['x'], df_clean['y'])
    plt.xlabel('Gross domestic product') # adds a label to the y-axis.
    plt.ylabel('Life Expectancy') # adds a label to the x-axis
    plt.title('1900') # adds a title to the plot. """

    
    

    # customise x ticks
    custom_ticks = [300, 1000, 10000]
    custom_labels = ['300', '1k', '10k']
    ticks_positions = [x.min(), 3000, x.max()]
    plt.xticks(ticks=custom_ticks, labels=custom_labels)
    plt.xlim(x.min(), x.max())
    """ for line in expectancy:
          for i in len(line):
                if i == idx:
                    x.append(line[i]) """
    """ print(x)
    print(y)
    print(type(x))
    x_int = x.astype(int)
    y_int = y.astype(float) """
    print(data)
    

    # plot the collected data
    """ plt.scatter(x, y)
    plt.xlabel('Gross domestic product') # adds a label to the y-axis.
    plt.ylabel('Life Expectancy') # adds a label to the x-axis
    plt.title('1900') # adds a title to the plot. """
    #plt.xticks(np.arange(min(x), max(x) + 1))
    #plt.yticks(np.arange(min(y), max(y) + 1), 5)


    # Graph printing
    plt.legend() # ensures the labels for the scatter plot and regression line are displayed.
    plt.show()


if __name__ == "__main__":
     main()