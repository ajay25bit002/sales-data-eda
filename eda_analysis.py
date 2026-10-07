from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


PROJECT_FOLDER = Path(__file__).resolve().parent
DATA_FILE = PROJECT_FOLDER / "sales_data.csv"


def main():
    # Load the sales data from the same folder as this script.
    sales_data = pd.read_csv(DATA_FILE)

    print("SALES DATA EXPLORATORY DATA ANALYSIS")
    print("\nFirst five rows:")
    print(sales_data.head())

    print("\nMissing values in each column:")
    print(sales_data.isnull().sum())

    if sales_data.isnull().values.any():
        for column in sales_data.columns:
            if sales_data[column].isnull().any():
                if pd.api.types.is_numeric_dtype(sales_data[column]):
                    sales_data[column] = sales_data[column].fillna(
                        sales_data[column].median()
                    )
                else:
                    sales_data[column] = sales_data[column].fillna(
                        sales_data[column].mode()[0]
                    )
        print("\nMissing values were filled with each column's median or most common value.")
    else:
        print("\nNo missing values were found.")

    print("\nBasic statistical information:")
    print(sales_data.describe())

    total_sales = sales_data["Sales"].sum()
    product_quantities = sales_data.groupby("Product")["Quantity"].sum()
    best_selling_product = product_quantities.idxmax()
    best_selling_quantity = product_quantities.max()

    product_sales = sales_data.groupby("Product")["Sales"].sum().sort_values(
        ascending=False
    )
    category_sales = sales_data.groupby("Category")["Sales"].sum().sort_values(
        ascending=False
    )
    region_sales = sales_data.groupby("Region")["Sales"].sum().sort_values(
        ascending=False
    )
    best_category = category_sales.idxmax()

    print(f"\nTotal sales: ${total_sales:,.2f}")
    print(
        f"Best-selling product by quantity: {best_selling_product} "
        f"({best_selling_quantity} units)"
    )
    print(
        f"Best-performing category: {best_category} "
        f"(${category_sales[best_category]:,.2f} in sales)"
    )
    print("\nSales by region:")
    print(region_sales.to_string(float_format=lambda amount: f"${amount:,.2f}"))
    print("\nSales by product:")
    print(product_sales.to_string(float_format=lambda amount: f"${amount:,.2f}"))

    charts = [
        (product_sales, "Sales by Product", "Product", "sales_by_product.png"),
        (category_sales, "Sales by Category", "Category", "sales_by_category.png"),
        (region_sales, "Sales by Region", "Region", "sales_by_region.png"),
    ]

    for sales, title, x_label, file_name in charts:
        sales.plot(kind="bar", color="steelblue", edgecolor="black")
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel("Sales ($)")
        plt.xticks(rotation=30, ha="right")
        plt.tight_layout()
        plt.savefig(PROJECT_FOLDER / file_name, dpi=150)
        plt.close()

    print("\nCharts saved:")
    print("- sales_by_product.png")
    print("- sales_by_category.png")
    print("- sales_by_region.png")

    print("\nConclusion:")
    print(
        f"The dataset recorded ${total_sales:,.2f} in sales. "
        f"{best_category} was the strongest category, while "
        f"{best_selling_product} sold the most units."
    )


if __name__ == "__main__":
    main()