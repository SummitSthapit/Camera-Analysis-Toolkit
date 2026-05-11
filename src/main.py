from data_loader import load_data

from computation import (
    compute_average,
    compute_median, 
    compute_standard_deviation,
    compute_variance,
    compute_maximum,    
    compute_minimum,
    newest_camera,  
    expensive_camera
)

from visualization import (
    plot_price_distribution,
    plot_resolution_vs_price,
    plot_release_year_distribution,
    plot_release_trend
)   

def main():

    df = load_data("D:\\Camera Analysis\\data\\camera_dataset.csv")

    df=df.dropna()

    prices= df["Price"]

    average_price=compute_average(prices)
    median_price=compute_median(prices) 
    std_dev_price=compute_standard_deviation(prices)
    variance_price=compute_variance(prices)
    max_price=compute_maximum(prices)
    min_price=compute_minimum(prices)

    expensive_cameras=expensive_camera(df,500)

    newest_model = newest_camera(df)

    plot_price_distribution(df)
    plot_resolution_vs_price(df)
    plot_release_year_distribution(df)
    plot_release_trend(df)

    with open("output/statistics.txt", "w") as f:
        f.write(f"Average Price: {average_price}\n")
        f.write(f"Median Price: {median_price}\n")
        f.write(f"Standard Deviation of Price: {std_dev_price}\n")
        f.write(f"Variance of Price: {variance_price}\n")
        f.write(f"Maximum Price: {max_price}\n")
        f.write(f"Minimum Price: {min_price}\n")
        f.write(f"Newest Camera Model: {newest_model[0]} (Released on {newest_model[1]})\n")
        f.write("Expensive Cameras (Price > 500):\n")
        f.write(expensive_cameras.to_string(index=False) + "\n") 

if __name__ == "__main__":
    main()

