import matplotlib.pyplot as plt
import numpy as np
import load_csv


def main():
    file = "../csv_files/population_total.csv"
    lines = load_csv.load(file)
    x = []
    y = []
    y1 = []
    end_year = 2040
    countries = [i[0] for i in lines[1:]]
    chosen_countries = ['France', 'Russia']
    countries_idx = []
    try:
        for country in chosen_countries:
            countries_idx.append(countries.index(country) + 1)
    except ValueError:
        print(f"{country} not found in the list of countries.")
        return
    for year in lines[0][1:]:
        if int(year) <= end_year:
            x.append(int(year.strip()))
    # France's life expectancy
    for i, value in enumerate(lines[countries_idx[0]][1:]):
        year = int(lines[0][i + 1])
        if year <= end_year:
            y.append(float(value.replace("M", "").strip()))
    # Russia's life expectancy
    for i, value in enumerate(lines[countries_idx[1]][1:]):
        year = int(lines[0][i + 1])
        if year <= end_year:
            y1.append(float(value.replace("M", "").strip()))

    # is data loaded correctly
    if len(x) != len(y):
        print("Data length mismach between years and life expectancy")
    # crop data to year 2040
    cropped_x = [year for year in x if year <= end_year]
    cropped_y = [y[i] for i in range(len(y)) if x[i] <= end_year]
    cropped_y.extend([y1[i] for i in range(len(y)) if x[i] <= end_year])

    # plotting
    plt.title('Population Projections')
    plt.xlabel('Year')  # adds a label to the x-axis
    plt.ylabel('Population')  # adds a label to the y-axis.
    plt.plot(x, y, color='g', label='Population France')
    plt.plot(x, y1, color='b', label='Population Russia')
    plt.legend(loc='lower right')

    # dynamic margin
    y_margin = (max(cropped_y) - min(cropped_y)) * 0.1
    y_min = min(cropped_y) - y_margin
    y_max = max(cropped_y) + y_margin

    plt.margins(x=0.05, y=0.05)
    plt.xticks(np.arange(int(min(cropped_x) // 10 * 10),
                         max(cropped_x) + 1, 40))
    plt.yticks(np.arange(int(min(cropped_y) // 10 * 10),
                         int(max(cropped_y)), 20))
    plt.ylim(y_min, y_max)

    # Show plot
    plt.show()


if __name__ == "__main__":
    main()
