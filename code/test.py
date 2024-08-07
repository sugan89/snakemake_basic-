import pandas as pd

file = r'input\df_grouped_byPlateandPertype.csv'
output_file = r'output\new.csv'



def test(file):
    df=pd.read_csv(file)
    print(df.columns)
    new_df = df.copy()
    new_df.to_csv(output_file)
    print(new_df)

test(file)
    
