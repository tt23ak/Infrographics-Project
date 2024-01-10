import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file from the local folder
df = pd.read_csv('world food production.csv')

# Sort the DataFrame by 'Rice Production' in descending order
df_sorted_rice = df.sort_values(by='Rice  Production ( tonnes)', ascending=False)

# Filter the DataFrame for the year 2021
df_sorted_rice_ = df_sorted_rice[df_sorted_rice['Year'] == 2021]
df_sorted_rice_ = df_sorted_rice_.drop(df_sorted_rice_.index[1]).reset_index(drop=True)
df_sorted_rice_five = df_sorted_rice_[['Entity', 'Rice  Production ( tonnes)']].head(5)

# Plotting a bar chart for the top five rice-producing countries
plt.figure(figsize=(10, 6))
bars = plt.bar(df_sorted_rice_five['Entity'], df_sorted_rice_five['Rice  Production ( tonnes)'], color='skyblue')

# Adding values on top of each bar
for bar, value in zip(bars, df_sorted_rice_five['Rice  Production ( tonnes)']):
    plt.text(bar.get_x() + bar.get_width() / 2 - 0.15, bar.get_height() + 0.05, str(value), ha='center', va='bottom')

# Adding labels and title
plt.xlabel('Entity', fontweight='bold')
plt.ylabel('Rice Production (tonnes)', fontweight='bold')
plt.title('Rice Production by Entity', fontweight='bold')
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')

# Save the plot as a PNG file
plt.savefig("22088557_1.png", dpi=300)

# Filter the original DataFrame to include only the data for the top five countries
df_top_countries = df[df['Entity'].isin(df_sorted_rice_five['Entity'])]

# Creating a line chart for each country using Seaborn
plt.figure(figsize=(12, 8))
sns.lineplot(x='Year', y='Rice  Production ( tonnes)', hue='Entity', data=df_top_countries, errorbar=None)

# Adding labels and title
plt.xlabel('Year', fontweight='bold')
plt.ylabel('Rice Production (tonnes)', fontweight='bold')
plt.title('Rice Production Trends for Top 5 Countries', fontweight='bold')
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')

# Show the legend outside the plot
plt.legend(title='Country', loc='upper left', frameon=False)

# Save the plot as a PNG file
plt.savefig("22088557_2.png", dpi=300)



# Filter the DataFrame for the year 2021
df_2021 = df[df['Year'] == 2021]

# Grouping the DataFrame by 'Entity' and finding the total production for each country in 2021
grouped_df = df_2021.groupby('Entity')['Rice  Production ( tonnes)'].sum().reset_index()

# Sorting the DataFrame by total production in descending order
sorted_countries = grouped_df.sort_values(by='Rice  Production ( tonnes)', ascending=False)

# Drop the second row
sorted_countries = sorted_countries.drop(sorted_countries.index[1])

# Select the top five countries
top_countries = sorted_countries.head(5)

# Calculating the total world production for the year 2021
total_world_production_2021 = grouped_df['Rice  Production ( tonnes)'].sum()

# Calculating the percentage of production for each top country compared to the world in 2021
top_countries['Percentage'] = (top_countries['Rice  Production ( tonnes)'] / total_world_production_2021) * 100

# Plotting a pie chart
plt.figure(figsize=(20, 20))
wedges, texts, autotexts = plt.pie(top_countries['Percentage'], labels=top_countries['Entity'], autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))

# Adding legend with percentages
legend_labels = [f'{label} ({percentage:.1f}%)' for label, percentage in zip(top_countries['Entity'], top_countries['Percentage'])]
plt.legend(wedges, legend_labels, title='Country', bbox_to_anchor=(1, 0, 0.5, 1))

plt.title('Percentage of Rice Production for Top 5 Countries in 2021')
# Save the plot as a PNG file
plt.savefig("22088557_3.png", dpi=300)



# Summing the production across all food products for each country
df_2021.loc[:, 'Total Production'] = df_2021.iloc[:, 2:].sum(axis=1)

# Sorting the DataFrame by total production in descending order
sorted_countries = df_2021.sort_values(by='Total Production', ascending=False)

# Drop the first two rows
sorted_countries = sorted_countries.iloc[2:]

# Select the top five countries
top_countries = sorted_countries.head(5)

# Plotting a bar chart for the top five countries
plt.figure(figsize=(12, 6))
bars = plt.bar(top_countries['Entity'], top_countries['Total Production'], color='skyblue')

# Adding labels and title
plt.xlabel('Country',fontweight='bold')
plt.ylabel('Total Food Production in 2021',fontweight='bold')
plt.title('Top 5 Countries with Highest Food Production in 2021',fontweight='bold')

# Show the text on top of each bar
for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), round(bar.get_height(), 2),
             ha='center', va='bottom')

# Show the plot
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')
plt.tight_layout()
# Save the plot as a PNG file
plt.savefig("22088557_4.png", dpi=300)
