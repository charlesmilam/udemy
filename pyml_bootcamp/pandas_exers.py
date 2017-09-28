import numpy as np
import pandas as pd

test_data = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}

test_df = pd.DataFrame(test_data)

print(test_df.to_string())
print(test_df)
