import pandas as pd
import matplotlib.pyplot as plt

# Function to get file paths and their masses from the user
def get_file_paths_and_masses():
    file_paths = []
    masses = []
    num_files = int(input("How many files do you want to plot? "))
    for i in range(num_files):
        file_path = input(f"Enter the file path for file {i+1}: ")
        mass = float(input(f"Enter the mass for file {i+1} (in g): "))
        file_paths.append(file_path)
        masses.append(mass)
    return file_paths, masses

# Get the file paths and masses from the user
file_paths, masses = get_file_paths_and_masses()

# Create a dictionary for normalization factors
normalization_factors = dict(zip(file_paths, masses))

# Initialize the first plot for Voltage vs Time
plt.figure(figsize=(10, 6))
for file_path in file_paths:
    data = pd.read_csv(file_path, delimiter="\t", decimal=",")
    df = pd.DataFrame(data)
    plt.plot(df.iloc[:,1]/3600, df.iloc[:,2], label=file_path.split('/')[-1])  # Use the file name as label

plt.xlabel('Time (h)')
plt.ylabel('Voltage (V)')
plt.title('Voltage vs Time for Multiple Files')
plt.legend()
plt.grid(True)
plt.show(block=False)  # Show the plot without blocking

# Initialize the second plot for Current vs Time
plt.figure(figsize=(10, 6))
for file_path in file_paths:
    data = pd.read_csv(file_path, delimiter="\t", decimal=",")
    df = pd.DataFrame(data)
    plt.plot(df.iloc[:,1]/3600, df.iloc[:,4], label=file_path.split('/')[-1])  # Use the file name as label

plt.xlabel('Time (h)')
plt.ylabel('Current (mA)')
plt.title('Current vs Time for Multiple Files')
plt.legend()
plt.grid(True)
plt.show(block=False)  # Show the plot without blocking

# Initialize the third plot for Capacity vs Time
plt.figure(figsize=(10, 6))
for file_path in file_paths:
    data = pd.read_csv(file_path, delimiter="\t", decimal=",")
    df = pd.DataFrame(data)
    plt.plot(df.iloc[:,1]/3600, df.iloc[:,3], label=file_path.split('/')[-1])  # Use the file name as label

plt.xlabel('Time (h)')
plt.ylabel('Capacity (mAh)')
plt.title('Capacity vs Time for Multiple Files')
plt.legend()
plt.grid(True)
plt.show(block=False)  # Show the plot without blocking

# Initialize the fourth plot for normalized Capacity vs Time
plt.figure(figsize=(10, 6))
for file_path in file_paths:
    data = pd.read_csv(file_path, delimiter="\t", decimal=",")
    df = pd.DataFrame(data)
    normalization_factor = normalization_factors[file_path]
    normalized_capacity = df.iloc[:,3] / normalization_factor
    plt.plot(df.iloc[:,1]/3600, normalized_capacity, label=file_path.split('/')[-1])  # Use the file name as label

plt.xlabel('Time (h)')
plt.ylabel('Normalized Capacity (mAh/g)')
plt.title('Normalized Capacity vs Time for Multiple Files')
plt.legend()
plt.grid(True)
plt.show(block=False)  # Show the plot without blocking

# Initialize the fifth plot for Voltage vs Normalized Capacity
plt.figure(figsize=(10, 6))
for file_path in file_paths:
    data = pd.read_csv(file_path, delimiter="\t", decimal=",")
    df = pd.DataFrame(data)
    normalization_factor = normalization_factors[file_path]
    normalized_capacity = df.iloc[:,3] / normalization_factor
    plt.plot(normalized_capacity, df.iloc[:,2], label=file_path.split('/')[-1])  # Use the file name as label

plt.xlabel('Normalized Capacity (mAh/g)')
plt.ylabel('Voltage (V)')
plt.title('Voltage vs Normalized Capacity for Multiple Files')
plt.legend()
plt.grid(True)
plt.show()  # Show the plot and block execution until all plots are closed