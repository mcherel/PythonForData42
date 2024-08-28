import matplotlib.pyplot as plt
import numpy as np
import load_csv


def main():
    file = "../csv_files/life_expectancy_years.csv"
    lines = load_csv.load(file)
    x = []
    y = []
    countries = [i[0] for i in lines[1:]]
    chosen_countries = ['France']
    countries_idx = []
    try:
        for country in chosen_countries:
            countries_idx.append(countries.index(country) + 1)
    except ValueError:
        print(f"{country} not found in the list of countries.")
        return
    for year in lines[0][1:]:
        x.append(int(year.strip()))
    # France's life expectancy
    for value in lines[countries_idx[0]][1:]:
        y.append(float(value.strip()))

    # is data loaded correctly
    if len(x) != len(y):
        print("Data length mismach between years and life expectancy")

    # Plotting
    plt.plot(x, y, color='b')
    plt.title('France Life Expectancy Projections')
    plt.xlabel('Year')  # adds a label to the x-axis
    plt.ylabel('Life expectancy')  # adds a label to the y-axis.

    # dynamic margin
    y_margin = (max(y) - min(y)) * 0.1
    y_min = min(y) - y_margin
    y_max = max(y) + y_margin

    plt.margins(x=0.05, y=0.05)
    plt.xticks(np.arange(min(x), max(x) + 1, 40))
    plt.yticks(np.arange(int(min(y) // 10 * 10), int(max(y) + 20), 10))
    plt.ylim(y_min, y_max)

    # Show plot
    plt.show()


if __name__ == "__main__":
    main()
