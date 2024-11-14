import pandas as pd 
import os 
def read_csv_file_crt_time(file_path: str) -> pd.DataFrame:
    """Summary or Description of the Function

    Parameters:
    argument1 (str): the file path of the csv file

    Returns:
    pandas dataframe: the data frame with the datetime index in isoformat

   """
    df = pd.read_csv(file_path,names=["Date","Time","Open","High","Low","Close","Volume"],)
    df["Datetime"] = pd.to_datetime(df['Date'] + ' ' + df['Time'], format='%Y.%m.%d %H:%M') 
    df.set_index("Datetime",inplace=True)
    df.drop(columns=['Date', 'Time'], inplace=True)
    #print(df.head())
    return df
def to_save_time_req(file_path: str,
                     data: pd.DataFrame,
                     time_frame: int,
                     dest_path: str ):

            """Summary or Description of the Function
            Parameters:
            file_path (str): The file path of the csv file to extract the name of the file
            data (pandas dataframe): The data frame with the datetime index in isoformat(pre-set)
            time_frame (int): The time frame to resample the data
            dest_path (str): The destination path to save the resampled data
            Returns:None

                End result: The data frame is resampled and saved in the proper_data folder with the name of the file and the time frame
            """
            file_name = file_path.split("\\")[-1].split(".")[0]
            df_time_format = data.resample("%sT"%(time_frame)).agg({
                "Open": "first",
                "High": "max",
                "Low": "min",
                "Close": "last",
                "Volume": "sum",
            })
            df_time_format.dropna(inplace = True)
            df_time_format.to_csv(os.path.join(dest_path,f"{file_name}_{time_frame}_min.csv"))
            #print(df_time_format.head())


if __name__=="__main__":
   file = r"XAUUSD_DATA_RAW\XAUUSD_2021_all.csv".split("\\")[-1].split(".")[0]
   print(file)
   temp = read_csv_file_crt_time(r"XAUUSD_DATA_RAW\XAUUSD_2021_all.csv")
   to_save_time_req(r"XAUUSD_DATA_RAW\XAUUSD_2021_all.csv",temp,5)