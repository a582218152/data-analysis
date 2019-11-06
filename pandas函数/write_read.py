


# pandas数据写入

data_frame = pd.read_csv(int_file)    
data_by_index = data_frame.iloc[:,[0,3]]
data_by_index.to_csv(output_file,index = Fasle)

pd.read.csv  将数据读取
function.to_csv('')  将数据吐出

常规方法使用函数csv.reader 和csv.write来读取和写入数据
pandas中采用pd函数


1.通过列的索引值（其实不在表格中是不存在的索引）来选取
loc和iloc


2.通过列标题而不是索引值来选取

csv_data_by_name = data_frame.loc[:,['Invoice Number']]   #loc通过列标题来选择

3.  drop函数丢弃无关的行

data_frame = pd.read_csv(input_file, header=None) 
data_frame = data_frame.drop([0,1,2,16,17,18]) 
data_frame.columns = data_frame.iloc[0]
data_frame = data_frame.reindex(data_frame.index.drop(3)) 
data_frame.to_csv(output_file, index=False)

4.添加标题行

命名一个header参数
通过pd.read_csv()添加标题行

header_list = ['Supplier Name', 'Invoice Number','Part Number', 'Cost', 'Purchase Date']
data_frame = pd.read_csv(input_file, header=None, names=header_list)
data_frame.to_csv(output_file, index=False)







