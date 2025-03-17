# Tidy Data Project: Mutant Moneyball Data

![Mutant Moneyball](https://rallyrd.com/wp-content/uploads/2023/02/Rally-3.jpg)

## Project Overview 
This project focuses on cleaning and tidying a dataset, Mutant Moneyball, which was adapted from GitHub. The dataset holds holds cleaned up data used in the Rally's Mutant Moneyball article which has X-Men value data from the X-Men's creation in 1963 up to 1993. 

The goal of this project is to transform a wide, untidy datset into a tidy format, making it easier to analyze and visualize. The project demonstrates our understanding of tidy data principles such as:
- Each variable forms a column
- Each observatuon forms a row
- Each type of observational unit forms a table

## Instructions 
To run this notebook, follow these steps:

### Step 1: Set Up 
1. **Make a Copy of the Notebook:**
- Open the Jupyter Notebook (`Yamanaka_TidyDataProject.ipynb`) in your preferred environment (e.g., Google Colab, Jupyter Lab, or Jupyter Notebook).

2. **Download the Dataset:**
- Download the dataset `mutant_moneyball.csv` from this repository 

3. **Install Dependencies:**
Ensure that you have the following Python libraries installed:
- Pandas
- Seaborn
- Matplotlib

You can install them with the following code:
pip install pandas seaborn matplotlib

These libraries are essential for data manipulation, cleaning, and visualizations. 

### Step 2: Run the Notebook 
1. **Follow and run the notebook cells sequentially to:**
- Load and upload the dataset
- Melt the datset into a tidy format
- Clean and transform the data
- Create visualizations
- Generate a pivot table 

**Additionally,** you can use the comments throughout the notebook to help explain what steps I took and why they were important. 

## Data Description 
The dataset mutant_moneyball.csv is adapted from the Mutant Moneyball Open Data repository on Github. The original dataset holds all the cleaned up data used in the Rally article Mutant Moneyball: The Search for the Most Valuable X-Men Team. It includes information about the value of X-Men comic books from 1963 to 1993, cateogrized by decade and source (Heritage Auctions, eBay, Wizard Price Guide, and Overstreet Price Guide). 

### Dataset Variables
The dataset contains the following variables related to the value of X-Men comic books across different decades and sources (information sourced from Mutant Moneyball Open Data Github Repository): 

| Variable Name | Summary |
|--------|---------|
|Member  | The name of the X-Men team member the data is connected to. |
|TotalValue60s_heritage | Total value of each X-Men team member's total number of issues as reflected by Heritage highest sale of comics released between 1963 and 1969.|
|TotalValue70s_heritage | Total value of each X-Men team member's total number of issues as reflected by Heritage highest sale of comics released between 1970 and 1979. |
|TotalValue80s_heritage | Total value of each X-Men team member's total number of issues as reflected by Heritage highest sale of comics released between 1980 and 1989. |
|TotalValue90s_heritage | Total value of each X-Men team member's total number of issues as reflected by Heritage highest sale of comics released between 1990 and 1992. |
|TotalValue60s_ebay | Total value of each X-Men team member's total number of issues released between 1963 and 1969 as reflected by ebay sales in 2022 in which sellers tagged the issue as VG (Very Good) Condition. |
|TotalValue70s_ebay | Total value of each X-Men team member's total number of issues released between 1970 and 1979 as reflected by ebay sales in 2022 in which sellers tagged the issue as VG (Very Good) Condition. |
|TotalValue80s_ebay | Total value of each X-Men team member's total number of issues released between 1980 and 1989 as reflected by ebay sales in 2022 in which sellers tagged the issue as VG (Very Good) Condition. |
|TotalValue90s_ebay | Total value of each X-Men team member's total number of issues released between 1990 and 1992 as reflected by ebay sales in 2022 in which sellers tagged the issue as VG (Very Good) Condition. |
|TotalValue60s_wiz | Total value of each X-Men team member's total number of issues released between 1963 and 1969 as they were valued in April 1993's Wizard Price Guide. |
|TotalValue70s_wiz | Total value of each X-Men team member's total number of issues released between 1970 and 1979 as they were valued in April 1993's Wizard Price Guide. |
|TotalValue80s_wiz | Total value of each X-Men team member's total number of issues released between 1980 and 1989 as they were valued in April 1993's Wizard Price Guide. |
|TotalValue90s_wiz | Total value of each X-Men team member's total number of issues released between 1990 and 1992 as they were valued in April 1993's Wizard Price Guide. |
|TotalValue60s_oStreet | Total value of each X-Men team member's total number of issues released between 1963 and 1969 as they were valued in 2015's Overstreet Price Guide.|
|TotalValue70s_oStreet | Total value of each X-Men team member's total number of issues released between 1970 and 1979 as they were valued in 2015's Overstreet Price Guide. |
|TotalValue80s_oStreet | Total value of each X-Men team member's total number of issues released between 1980 and 1989 as they were valued in 2015's Overstreet Price Guide. |
|TotalValue90s_oStreet | Total value of each X-Men team member's total number of issues released between 1990 and 1992 as they were valued in 2015's Overstreet Price Guide. |

## Visuals

### Visualizations

### Code Snippet: Melting the DataFrame

## References