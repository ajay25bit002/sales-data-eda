# Sales Data Exploratory Data Analysis

## Project Objective

Explore a small sample sales dataset to understand sales by product, category, and region. The analysis prints useful summaries and saves simple charts for comparison.

## Dataset Description

`sales_data.csv` contains 24 sample sales records. Each row represents sales of one product in one region.

| Column | Description |
| --- | --- |
| Product | Name of the product sold |
| Category | Product category |
| Quantity | Number of units sold |
| Price | Price per unit in dollars |
| Sales | Total sales for the row in dollars |
| Region | Sales region |

## Technologies Used

- Python
- Pandas
- Matplotlib

## EDA Steps

1. Load the CSV file with Pandas and display the first five rows.
2. Check each column for missing values and fill any missing values with the numeric median or most common text value.
3. Display basic statistical information for the numeric columns.
4. Calculate total sales, the best-selling product by quantity, and the best-performing category by sales.
5. Summarize sales by region and by product.
6. Create and save bar charts for product, category, and region sales.

## Key Findings

- Total sales were **$24,442.00**.
- **Notebook** was the best-selling product by quantity, with **130 units** sold.
- **Electronics** was the best-performing category, with **$18,735.00** in sales.
- The script also prints the region-wise and product-wise sales totals when it runs.

## Conclusion

Electronics contributed the most revenue in this sample, while notebooks led in units sold. Comparing both revenue and quantity helps show the difference between high-value products and frequently purchased products. The charts make it easier to compare these results visually.

## Run the Project

From the project folder, install the required packages and run the analysis:

```bash
pip install pandas matplotlib
python eda_analysis.py
```

The script saves `sales_by_product.png`, `sales_by_category.png`, and `sales_by_region.png` in the project folder.