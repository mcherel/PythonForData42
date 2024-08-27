import matplotlib.pyplot as plt
import numpy as np
import load_csv



def main():
    file = "../csv_files/life_expectancy_years.csv"
    lines = load_csv.load(file)
    x = []
    y = []
    countries = [ i[0] for i in lines[1:]]
    france_idx = countries.index('France')

    """ stripped_rows = list([[field.strip()
                             for field in row]
                             for row in reader[1:]]) """
    for year in lines[0][1:]:
         x.append(int(year.strip()))
    for value in lines[france_idx][1:]:
         y.append(float(value.strip()))
    #print(len(x))
    #print(len(y))
    #print(x)
    #print(y)
    if len(x) != len(y):
         print("Data length mismach between years and life expectancy")

    # Plotting
    plt.plot(x, y, color='b', label='Life Expectancy in France')
    plt.title('France Life Expectancy Projections')
    # plt.xticks(rotation=25)
    plt.xlabel('Year') # adds a label to the x-axis
    plt.ylabel('Life expectancy') # adds a label to the y-axis.
    #plt.grid(True)
    plt.xlim(min(x), max(x))
    plt.ylim(min(y), max(y))
    #plt.xticks(x)
    """ fig, ax = plt.subplots()
    ax.set_xticks(np.arange(0, max(x), 50))
    ax.set_yticks(np.arange(0, max(y), 50)) """
    """     # Check if the ddata file exists
    if os.path.exists(file):
            # Loading  data into two lists
            data = pd.read_csv(file)
            X = data['km'].values.reshape(-1, 1)
            y = data['price'].values.reshape(-1, 1)

            #Plot the data
            plt.scatter(X, y, label='Car prices')
            plt.xlabel('Mileage (km)') # adds a label to the x-axis
            plt.ylabel('Price ($)') # adds a label to the y-axis.
            plt.title('Car Price Prediction') # adds a title to the plot.

    else:
            print(f"There is no {file}")
            if os.path.exists(training_data_file):
                os.remove(training_data_file)
            exit()

    #Plot regression line from training data if available
    if os.path.exists(training_data_file):
            theta0, theta1 = open_csv.open_csv(training_data_file)

            # Adding a red line
            xmin, xmax = X.min(), X.max()
            ordonne = np.linspace(xmin, xmax)
            plt.plot(ordonne, theta1 * ordonne + theta0, color='r', label='Linear Regression Line')

            # Prediction
            y_predict = estimate_price.hypothesis(theta0, theta1, X)

            # Print Mean Absolute Error (MAE)
            print(f'MAE: \t{metrics.mean_absolute_error(y, y_predict)}')

            # Print Mean Squared Error (MSE)
            print(f'MSE: \t{metrics.mean_squared_error(y, y_predict)}')

            # Print Root Mean Squared Error (RMSE)
            print(f'RMSE: \t{np.sqrt(metrics.mean_squared_error(y, y_predict))}')

            # Print R-squared (R²)
            print(f'R²: \t{metrics.r2_score(y, y_predict)}') """


    # Graph printing
    plt.legend() # ensures the labels are displayed.
    
    # Show plot
    plt.show()


if __name__ == "__main__":
      main()