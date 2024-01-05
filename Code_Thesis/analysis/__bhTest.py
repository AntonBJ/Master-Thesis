import numpy as np
from scipy.stats import false_discovery_control
'''# Your array of p-values
p_values = np.array([0.03783778, 0.10265262, 0.1059301, 0.11768054, 0.12470931, 0.13701531,
                     0.17499326, 0.18255279, 0.18985543, 0.19426618, 0.29046597, 0.29715138,
                     0.31326115, 0.36602186, 0.36859554, 0.37297287, 0.43754055, 0.44539445,
                     0.46792285, 0.48699114, 0.50840972, 0.52794501, 0.54159452, 0.54441726,
                     0.54968063, 0.56106255, 0.59094134, 0.6308342, 0.65972744, 0.67552019,
                     0.68003537, 0.68579356, 0.70916378, 0.71257932, 0.7425958, 0.74872072,
                     0.75617886, 0.81673406, 0.84323871, 0.8498986, 0.87210674, 0.87349128,
                     0.87608194, 0.92151515, 0.9299641, 0.93036624, 0.95367913, 0.9559937,
                     0.96500011, 0.96511976, 0.97631791, 0.98258153])

# Step 1: Sort the p-values in ascending order
sorted_indices = np.argsort(p_values)
sorted_p_values = p_values[sorted_indices]

# Step 2: Calculate Benjamini-Hochberg critical values
num_tests = len(sorted_p_values)
bh_critical_values = np.arange(1, num_tests + 1) / num_tests * 0.05  # Assuming FDR level of 0.05

# Create a dictionary to store critical values corresponding to p-values in original order
p_value_critical_dict = {p_values[i]: bh_critical_values[i] for i in range(len(p_values))}

# Step 3: Determine rejected null hypotheses
rejected_indices = np.where(sorted_p_values <= bh_critical_values)[0]
rejected_p_values = sorted_p_values[rejected_indices]
rejected_indices_original_order = sorted_indices[rejected_indices]

rejected_critical_values = [p_value_critical_dict[p] for p in rejected_p_values]

print("Rejected p-values:", rejected_p_values)
print("Indices of rejected p-values in the original order:", rejected_indices_original_order)
print("Critical values corresponding to rejected p-values:", rejected_critical_values)

print(p_value_critical_dict)'''

import pandas as pd

# Your p-values
p_values = [0.68579356, 0.87608194, 0.75617886, 0.65972744, 0.87210674, 0.19426618,
            0.87349128, 0.59094134, 0.54159452, 0.92151515, 0.36602186, 0.7425958,
            0.95367913, 0.54441726, 0.50840972, 0.46792285, 0.36859554, 0.13701531,
            0.18985543, 0.18255279, 0.37297287, 0.44539445, 0.48699114, 0.31326115,
            0.96500011, 0.71257932, 0.70916378, 0.43754055, 0.54968063, 0.9299641,
            0.67552019, 0.84323871, 0.74872072, 0.29715138, 0.56106255, 0.52794501,
            0.12470931, 0.97631791, 0.8498986, 0.81673406, 0.11768054, 0.9559937,
            0.03783778, 0.68003537, 0.6308342, 0.10265262, 0.98258153, 0.1059301,
            0.29046597, 0.96511976, 0.17499326, 0.93036624]

# Perform Benjamini-Hochberg procedure
p_values_sorted = sorted((p, i) for i, p in enumerate(p_values))
m = len(p_values)
adjusted_p_values = [min(p * m / (i + 1), 1.0) for i, (p, _) in enumerate(p_values_sorted)]

# Create a pandas DataFrame with original p-values and adjusted p-values
df = pd.DataFrame({
    'Original_p_values': [p for p, _ in p_values_sorted],
    'Adjusted_p_values': adjusted_p_values
})

print(df)

fdr_kst = false_discovery_control(p_values[0], method='bh')
print(fdr_kst)