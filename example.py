import pandas as pd

# Example DataFrame with country names as the index
data = {'Column1': [1, 2, 3], 'Column2': [4, 5, 6]}
country_names = ['CountryA', 'CountryB', 'CountryC']
df = pd.DataFrame(data, index=country_names)

# Accessing the index
print(df.index)