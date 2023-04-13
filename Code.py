import pandas as pd


def read_data(filename):
    df = pd.read_csv(filename)

    # drop irrelevant columns
    df = df.drop(columns=["Country Code", "Indicator Name", "Indicator Code"])

    # set the index to be the country name
    df = df.set_index("Country Name")

    # pivot the dataframe to get years as columns
    df_years = df.transpose()

    # clean the dataframes
    df_years.index.name = "Year"
    df_years.columns.name = None

    # remove any rows or columns with all NaN values
    df_years = df_years.dropna(axis=1, how="all")

    # pivot the dataframe again to get countries as columns
    df_countries = df_years.transpose()

    return df_years, df_countries


df_years, df_countries = read_data("Arable Land.csv")

df = pd.read_csv("Arable Land.csv")


arable_land = df[df["Indicator Code"] == "AG.LND.ARBL.ZS"]

# Extract data for a few countries
countries = ["United States", "China", "India", "Brazil", "Russia"]
arable_land_countries = arable_land[arable_land["Country Name"].isin(countries)]

# Calculate summary statistics
summary_stats = arable_land_countries.describe()
print(summary_stats)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read arable land data
arable_land_df = pd.read_csv("Arable Land.csv")
arable_land_df.drop(columns=["Indicator Name", "Indicator Code"], inplace=True)

# read freshwater withdrawals data
freshwater_withdrawals_df = pd.read_csv("Water.csv")
freshwater_withdrawals_df.drop(
    columns=["Indicator Name", "Indicator Code"], inplace=True
)

merged_df = pd.merge(
    arable_land_df, freshwater_withdrawals_df, on=["Country Name", "Country Code"]
)

# view the merged dataset
merged_df.head()

# create a correlation matrix
corr_matrix = merged_df[["2019_x", "2019_y"]].corr()

# plot the correlation matrix as a heatmap
sns.heatmap(corr_matrix, cmap="coolwarm", annot=True)
plt.title("Correlation Plot between Arable Land  and Water Withdrawal")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load the Arable Land dataset
arable_land = pd.read_csv("Arable Land.csv")

# Select the columns of interest and transpose the data
arable_land = arable_land[["Country Name", "Country Code", "2018"]]
arable_land = arable_land.set_index("Country Name").transpose()

# Load the Annual Freshwater Withdrawal dataset
freshwater_withdrawal = pd.read_csv("Water.csv")

# Select the columns of interest and transpose the data
freshwater_withdrawal = freshwater_withdrawal[["Country Name", "Country Code", "2017"]]
freshwater_withdrawal = freshwater_withdrawal.set_index("Country Name").transpose()

# Combine the two datasets
combined_data = pd.concat([arable_land, freshwater_withdrawal], axis=0)

# Create a scatter plot of arable land vs freshwater withdrawal for different countries
plt.scatter(combined_data.loc["2018"], combined_data.loc["2017"], alpha=0.5)

# Set the plot title and labels
plt.title("Arable land vs Annual freshwater withdrawals by country")
plt.xlabel("Arable land (% of land area)")
plt.ylabel("Annual freshwater withdrawals (% of internal resources)")

# Show the plot
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import random

# Load the Arable Land dataset
arable_land = pd.read_csv("Arable Land.csv")

# Select the columns of interest and transpose the data
arable_land = arable_land[["Country Name", "Country Code", "2018"]]
arable_land = arable_land.set_index("Country Name").transpose()

# Load the Annual Freshwater Withdrawal dataset
freshwater_withdrawal = pd.read_csv("Water.csv")

# Select the columns of interest and transpose the data
freshwater_withdrawal = freshwater_withdrawal[["Country Name", "Country Code", "2017"]]
freshwater_withdrawal = freshwater_withdrawal.set_index("Country Name").transpose()

# Combine the two datasets
combined_data = pd.concat([arable_land, freshwater_withdrawal], axis=0)

# Select three random countries for plotting
countries = random.sample(combined_data.columns.tolist(), 3)

# Create a scatter plot of arable land vs freshwater withdrawal for the selected countries
plt.scatter(
    combined_data.loc["2018", countries],
    combined_data.loc["2017", countries],
    alpha=0.5,
)

# Add country labels to the plot
for i, country in enumerate(countries):
    plt.annotate(
        country,
        (combined_data.loc["2018", country], combined_data.loc["2017", country]),
    )

# Set the plot title and labels
plt.title("Arable land vs Annual freshwater withdrawals by country")
plt.xlabel("Arable land (% of land area)")
plt.ylabel("Annual freshwater withdrawals (% of internal resources)")

# Show the plot
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Load the Arable Land dataset
arable_land = pd.read_csv("Arable Land.csv")

# Select the columns of interest and transpose the data
arable_land = arable_land[
    [
        "Country Name",
        "Country Code",
        "2010",
        "2011",
        "2012",
        "2013",
        "2014",
        "2015",
        "2016",
        "2017",
        "2018",
    ]
]
arable_land = (
    arable_land.set_index(["Country Name", "Country Code"]).stack().reset_index()
)
arable_land.columns = ["Country Name", "Country Code", "Year", "Arable Land (%)"]
arable_land["Year"] = pd.to_datetime(arable_land["Year"], format="%Y")

# Load the Annual Freshwater Withdrawal dataset
freshwater_withdrawal = pd.read_csv("Water.csv")

# Select the columns of interest and transpose the data
freshwater_withdrawal = freshwater_withdrawal[
    [
        "Country Name",
        "Country Code",
        "2010",
        "2011",
        "2012",
        "2013",
        "2014",
        "2015",
        "2016",
        "2017",
    ]
]
freshwater_withdrawal = (
    freshwater_withdrawal.set_index(["Country Name", "Country Code"])
    .stack()
    .reset_index()
)
freshwater_withdrawal.columns = [
    "Country Name",
    "Country Code",
    "Year",
    "Freshwater Withdrawal (%)",
]
freshwater_withdrawal["Year"] = pd.to_datetime(
    freshwater_withdrawal["Year"], format="%Y"
)

# Merge the two datasets
combined_data = pd.merge(
    arable_land,
    freshwater_withdrawal,
    on=["Country Name", "Country Code", "Year"],
    how="outer",
)

# Plot the time series of arable land and freshwater withdrawal for different countries
countries = ["China", "India", "United States"]
for country in countries:
    data = combined_data.loc[combined_data["Country Name"] == country]
    plt.plot(
        data["Year"], data["Arable Land (%)"], label="{} - Arable Land".format(country)
    )
    plt.plot(
        data["Year"],
        data["Freshwater Withdrawal (%)"],
        label="{} - Freshwater Withdrawal".format(country),
    )

# Set the plot title and labels
plt.title(
    "Time Series of Arable Land and Freshwater Withdrawal for Different Countries"
)
plt.xlabel("Year")
plt.ylabel("Percentage of Land Area / Internal Resources")
plt.legend()

# Show the plot
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load the Arable Land dataset
arable_land = pd.read_csv("Arable Land.csv")

# Select the columns of interest and transpose the data
arable_land = arable_land[
    [
        "Country Name",
        "Country Code",
        "2000",
        "2001",
        "1980",
        "1990",
        "2005",
        "2010",
        "2018",
    ]
]
arable_land = arable_land.set_index("Country Name")

# Load the Annual Freshwater Withdrawal dataset
freshwater_withdrawal = pd.read_csv("Water.csv")

# Select the columns of interest and transpose the data
freshwater_withdrawal = freshwater_withdrawal[
    [
        "Country Name",
        "Country Code",
        "2000",
        "2001",
        "1980",
        "1990",
        "2005",
        "2010",
        "2018",
    ]
]
freshwater_withdrawal = freshwater_withdrawal.set_index("Country Name")

# freshwater_withdrawal
# Select the three countries of interest
countries = ["United States", "India", "China"]
arable_land = arable_land.loc[countries]
freshwater_withdrawal = freshwater_withdrawal.loc[countries]


combined_data = pd.concat([arable_land["2018"], freshwater_withdrawal["2005"]], axis=1)
combined_data.columns = ["Arable Land", "Annual Freshwater Withdrawal"]
combined_data.plot.bar(figsize=(10, 5))
plt.title("Arable Land and Annual Freshwater Withdrawal for Selected Countries in 2018")
plt.xlabel("Country")
plt.ylabel("Percentage")
plt.show()
