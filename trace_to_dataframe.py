import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

all_df = pd.read_json(path_or_buf="downtown-crosstown.json", lines=True)
print all_df.head()