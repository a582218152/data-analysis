import pandas
import pandas as pd
import sys
import csv


#python基础方法实现筛选行中的某数据
input_file = sys.argv[1]
output_file = sys.argv[2]
with open(input_file,'r') as csv_in_file:
    with open(output_file,'w') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
   #使用csv中的next函数读出输入文本第一行，赋值给header
        filewriter.writerow(header)
   ##将标题行写入输出文件
        for row_list in filereader:
            supplier = str(row_list[1]).strip()
            cost = str(row_list[3]).strip('$').replace(',', '')
            if supplier == 'Supplier Z' or float(cost) > 600.0:
                filewriter.writerow(row_list)




#pandas中筛选行中的数据

import pandas as pd
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_csv(input_file)
data_frame2 = data_frame['Cost'].str.strip('$').astype(float)
data_frame_value_meets_condition = data_frame.loc[(data_frame['Supplier Name'].str.contains('Z')) | (data_frame2 > 600.0), :]
data_frame_value_meets_condition.to_csv(output_file, index=False)



#筛选行匹配某个集合
data_frame = pd.read_csv(input_file)
important_dates = ['1/20/14', '1/30/14']
data_frame_value_in_set = data_frame.loc[data_frame['Purchase Date'].\ isin(important_dates), :]
data_frame_value_in_set.to_csv(output_file, index=False)


#筛选中匹配正则表达式
data_frame = pd.read_csv(input_file)
data_frame_value_matches_pattern = data_frame.loc[data_frame['Invoice Number'].\ str.startswith("001-"), :]
data_frame_value_matches_pattern.to_csv(output_file, index=False)









