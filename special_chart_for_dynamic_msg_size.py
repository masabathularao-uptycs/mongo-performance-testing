import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

MAIN = "dynamic_msg_size"
# Step 1: Read CSV file and extract last two columns
df = pd.read_csv(f'{MAIN}.csv',header=None)
# print(df)
x_values = df.iloc[:, -2]  # Second to last column
print(x_values)
y_values = df.iloc[:, -1]  # Last column
x_values_for_rate=y_values/(3*0.75*1024)


# Step 2: Create plot
plt.figure(figsize=(10, 6))  # Adjust figure size as needed
plt.plot(x_values, y_values)
plt.xlabel('seconds elapsed from start of the test')  # You can customize the label
plt.ylabel('Number of documents in the database')  # You can customize the label
plt.title('Number Of Documents VS Time')  # You can customize the title
plt.grid(True)  # Optionally, add grid lines

# Format y-axis tick labels to display in full
formatter = FuncFormatter(lambda x, _: '{:,.0f}'.format(x))
plt.gca().yaxis.set_major_formatter(formatter)
plt.savefig(f'{MAIN}_doc_vs_time.png', bbox_inches='tight')

plt.close()

# Calculate rate of insertion
insertion_rate = [0]  # Start with zero rate for the first data point
for i in range(1, len(y_values)):
    rate = (y_values[i] -y_values[i-1]) # / (y_values[i] - y_values[i-1])
    insertion_rate.append(rate)

# Plot the rate of insertion 
plt.figure(figsize=(10, 6))  # Adjust figure size as needed

plt.plot(x_values_for_rate, insertion_rate)
plt.xlabel('size of the document')
plt.ylabel('Rate of Insertion per min')
plt.title('Rate of Insertion Over Time')
plt.xticks(range(0, int(max(x_values_for_rate)), 5))
plt.grid(True)
plt.savefig(f'{MAIN}_rate_of_insertion.png', bbox_inches='tight')