import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

MAIN = "TEST1"
# Step 1: Read CSV file and extract last two columns
df = pd.read_csv(f'{MAIN}.csv')
x_values = df.iloc[:, -2]  # Second to last column
y_values = df.iloc[:, -1]  # Last column

# Step 2: Create plot
plt.figure(figsize=(10, 6))  # Adjust figure size as needed
plt.plot(x_values, y_values)
plt.xlabel('seconds lapsed from start of the test')  # You can customize the label
plt.ylabel('Number of documents in the database')  # You can customize the label
plt.title('Number Of Documents VS Time')  # You can customize the title
plt.grid(True)  # Optionally, add grid lines

# Format y-axis tick labels to display in full
formatter = FuncFormatter(lambda x, _: '{:,.0f}'.format(x))
plt.gca().yaxis.set_major_formatter(formatter)
plt.savefig(f'{MAIN}.png', bbox_inches='tight')
