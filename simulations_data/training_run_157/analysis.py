
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Read the data, explicitly handling the header
data = pd.read_csv('energyvst.dat', comment='#', sep='\s+', header=None)


# Manually setting the column names based on the commented header line
column_names = ['time (fs)', 'E total (H)', 'E non-SCC (H)', 'E SCC (H)', 'E spin (H)', 'E external (H)', 'E rep (H)', 'E kinetic nuclear (H)', 'E dispersion (H)']
data.columns = column_names


# # Convert columns to numeric, coerce any errors to NaN
# for col in data.columns:
#     data[col] = pd.to_numeric(data[col], errors='coerce')

# print(data.head())  # Check the first few rows of the DataFrame
# print(data.dtypes)  # Check the data types of each column

# Plotting Total Energy over Time
plt.figure(figsize=(10, 6))
plt.plot(data['time (fs)'], data['E total (H)'], label='Total Energy', marker='o', linestyle='-', markersize=4)

# Optional: plotting other components for comparison
plt.plot(data['time (fs)'], data['E non-SCC (H)'], label='Non-SCC Energy', linestyle='--')
plt.plot(data['time (fs)'], data['E SCC (H)'], label='SCC Energy', linestyle='-.')
# Add more plots as needed for other energy components

plt.xlabel('Time (fs)')
plt.ylabel('Energy (Hartree)')
plt.title('Energy Components over Time')
plt.legend()
plt.grid(True)
plt.show()







# Read the data, explicitly handling the header
data = pd.read_csv('forcesvst.dat', comment='#', delim_whitespace=True, header=None)

# Manually setting the column names based on the commented header line
column_names = ['time (fs)', 'Force atom 1 x', 'Force atom 1 y', 'Force atom 1 z', 'Force atom 2 x', 'Force atom 2 y', 'Force atom 2 z']
data.columns = column_names

# Plotting Total Energy over Time
plt.figure(figsize=(10, 6))
plt.plot(data['time (fs)'], data['Force atom 1 x'], label='Force atom 1 x', marker='o', linestyle='-', markersize=4)

# Optional: plotting other components for comparison
plt.plot(data['time (fs)'], data['Force atom 1 y'], label='Force atom 1 y', linestyle='--')
plt.plot(data['time (fs)'], data['Force atom 1 z'], label='Force atom 1 z', linestyle='-.')
# Add more plots as needed for other energy components

plt.xlabel('Time (fs)')
plt.ylabel('Force atom 1')
plt.title('Force Components over Time')
plt.legend()
plt.grid(True)
plt.show()








# Load the data, skipping the first line which is the header
data = pd.read_csv('laser.dat', delim_whitespace=True, skiprows=1, header=None, names=['Time_fs', 'E_x_eV_ang', 'E_y_eV_ang', 'E_z_eV_ang'])

# Plotting
plt.figure(figsize=(10, 6))

# Plot each electric field component against time
plt.plot(data['Time_fs'], data['E_x_eV_ang'], label='E_x (eV/ang)')
plt.plot(data['Time_fs'], data['E_y_eV_ang'], label='E_y (eV/ang)', linestyle='--')
plt.plot(data['Time_fs'], data['E_z_eV_ang'], label='E_z (eV/ang)', linestyle='-.')
plt.xlabel('Time (fs)')
plt.ylabel('Electric Field (eV/angstrom)')
plt.title('Electric Field Components Over Time')
plt.legend()
plt.grid(True)
plt.show()







# Load the data from mu.dat, skipping the first line which is the header
data_mu = pd.read_csv('mu.dat', delim_whitespace=True, skiprows=1, header=None, names=['Time_fs', 'mu_x_e_ang', 'mu_y_e_ang', 'mu_z_e_ang'])



# Plotting components of dipole moment
plt.figure(figsize=(10, 6))

# Plot each dipole moment component against time
plt.plot(data_mu['Time_fs'], data_mu['mu_x_e_ang'], label='mu_x (e.angstrom)')
plt.plot(data_mu['Time_fs'], data_mu['mu_y_e_ang'], label='mu_y (e.angstrom)', linestyle='--')
plt.plot(data_mu['Time_fs'], data_mu['mu_z_e_ang'], label='mu_z (e.angstrom)', linestyle='-.')

plt.xlabel('Time (fs)')
plt.ylabel('Dipole Moment (e.angstrom)')
plt.title('Dipole Moment Components Over Time')
plt.legend()
plt.grid(True)
plt.show()




# Calculate the magnitude of the dipole moment vector for each time point
data_mu['Magnitude'] = np.sqrt(data_mu['mu_x_e_ang']**2 + data_mu['mu_y_e_ang']**2 + data_mu['mu_z_e_ang']**2)

# Plotting
plt.figure(figsize=(10, 6))

# Plot the magnitude of the dipole moment against time
plt.plot(data_mu['Time_fs'], data_mu['Magnitude'], label='Magnitude (e.angstrom)', color='black')

plt.xlabel('Time (fs)')
plt.ylabel('Magnitude of Dipole Moment (e.angstrom)')
plt.title('Magnitude of Dipole Moment Over Time')
plt.legend()
plt.grid(True)
plt.show()







# Assuming the file has a dynamic number of columns, we'll load it dynamically
# Skip the first row (header) and use the first column as index (time)
data_qsvst = pd.read_csv('qsvst.dat', delim_whitespace=True, comment='#', header=None)

# Adding column names based on the pattern observed
column_names = ['Time_fs', 'Total_Net_Charge_e'] + [f'Charge_atom_{i+1}_e' for i in range(data_qsvst.shape[1] - 2)]
data_qsvst.columns = column_names

# Plotting
plt.figure(figsize=(12, 8))

# Plot total net charge over time
plt.subplot(2, 1, 1)
plt.plot(data_qsvst['Time_fs'], data_qsvst['Total_Net_Charge_e'], label='Total Net Charge', color='black')
plt.xlabel('Time (fs)')
plt.ylabel('Total Net Charge (e)')
plt.title('Total Net Charge Over Time')
plt.legend()
plt.grid(True)

# Plot charge of the first few atoms over time as an example
plt.subplot(2, 1, 2)
for i in range(1, min(5, data_qsvst.shape[1] - 1)):  # Plotting up to 4 atoms as an example
    plt.plot(data_qsvst['Time_fs'], data_qsvst[f'Charge_atom_{i}_e'], label=f'Atom {i} Charge', linestyle='--')

plt.xlabel('Time (fs)')
plt.ylabel('Charge (e)')
plt.title('Charge of Individual Atoms Over Time')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()












# Load the data, skipping the first two lines which are comments and headers
data_molpopul1 = pd.read_csv('molpopul1.dat', delim_whitespace=True, comment='#', header=None)

# Since the first column is time, and the rest are orbital populations, setting column names accordingly
column_names = ['Time_fs'] + [f'Population_orb_{i}' for i in range(1, data_molpopul1.shape[1])]
data_molpopul1.columns = column_names

# Plotting
plt.figure(figsize=(12, 8))

# Plot the population of each of the first few orbitals as an example
for i in range(1, min(5, data_molpopul1.shape[1])):  # Adjust this range as needed
    plt.plot(data_molpopul1['Time_fs'], data_molpopul1[f'Population_orb_{i}'], label=f'Orbital {i}')

plt.xlabel('Time (fs)')
plt.ylabel('Population')
plt.title('Molecular Orbital Populations Over Time')
plt.legend()
plt.grid(True)
plt.show()
