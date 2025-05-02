import pandas as pd
import numpy as np
import timeit

# Generating a large number of rows for testing
n = 100000
data = {
    'function_name': [f'func_{i}' for i in range(n)],
    'genus': np.random.choice(['Abies', 'Pinus', 'Quercus', 'Fagus'], size=n)
}

df = pd.DataFrame(data)

# Method 1: For loop
def for_loop_method():
    result = {}
    for _, row in df.iterrows():
        genus = row['genus']
        if genus not in result:
            result[genus] = []
        result[genus].append(row['function_name'])
    return result

# Method 2: Boolean indexing
def boolean_indexing_method():
    result = {}
    for genus in ['Abies', 'Pinus']:
        filtered_df = df[df['genus'] == genus]
        result[genus] = filtered_df['function_name'].tolist()
    return result

# Method 3: Map function
def map_method():
    result = {}
    for genus in ['Abies', 'Pinus']:
        genus_functions = list(map(lambda x: x['function_name'], filter(lambda x: x['genus'] == genus, df.to_dict('records'))))
        result[genus] = genus_functions
    return result

# Testing the methods with timeit
print("Timing For loop method:")
print(timeit.timeit(for_loop_method, number=10))

print("Timing Boolean Indexing method:")
print(timeit.timeit(boolean_indexing_method, number=10))

print("Timing Map function method:")
print(timeit.timeit(map_method, number=10))
