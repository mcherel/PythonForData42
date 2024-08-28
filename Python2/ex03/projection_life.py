import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import load_csv


def main():
    f_inflat = "../csv_files/"
    f_inflat += "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    f_life = "../csv_files/life_expectancy_years.csv"

    chosen_y = "1900"
    gdp = load_csv.load(f_inflat)
    expectancy = load_csv.load(f_life)

    # data generation
    idx = np.where(expectancy[0] == chosen_y)[0][0]
    data = {}
    data['x'] = gdp[1:, idx].tolist()
    data['y'] = expectancy[1:, idx].tolist()

    # converting to dataframe
    df = pd.DataFrame(data)

    # converting columns to numeric, coercing errors to NaN
    df['x'] = pd.to_numeric(df['x'], errors='coerce')
    df['y'] = pd.to_numeric(df['y'], errors='coerce')

    # drop rows with NaN values
    df_clean = df.dropna()

    # plot the scatter plot
    plt.scatter(df_clean['x'], df_clean['y'])

    # rendering x axis into logarithmic form
    plt.xscale('log')

    # labels
    plt.xlabel('Gross domestic product')  # adds a label to the y-axis.
    plt.ylabel('Life Expectancy')  # adds a label to the x-axis
    plt.title('1900')  # adds a title to the plot. """

    # customise x ticks
    custom_ticks = [300, 1000, 10000]
    custom_labels = ['300', '1k', '10k']
    plt.xticks(ticks=custom_ticks, labels=custom_labels)

    # Graph printing
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
