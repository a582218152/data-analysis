
import pandas
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_csv(input_file)
data_frame.to_csv(output_file)
