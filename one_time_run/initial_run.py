import pandas as pd 
from data_process import read_csv_file_crt_time, to_save_time_req

def just_run_once(file_path: str, *years: int,dest_path: str):
    """
    Summary or Description of the Function

    Parameters:
    file_path (str): The file path of the csv file saved
    year (int): Expected to be int_list 

    Returns:None
    """
    for year in years:

        file_path = "XAUUSD_DATA_RAW\XAUUSD_%s_all.csv"%(year)
        data = read_csv_file_crt_time(file_path)
        to_save_time_req(file_path,data,5,dest_path)
        to_save_time_req(file_path,data,15,dest_path)
        to_save_time_req(file_path,data,30,dest_path)
        to_save_time_req(file_path,data,60,dest_path)
        to_save_time_req(file_path,data,240,dest_path)
        to_save_time_req(file_path,data,1440,dest_path)
        to_save_time_req(file_path,data,10080,dest_path)