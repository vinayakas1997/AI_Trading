#This is the main file 
#"C:\Users\vinay\Desktop\Market_Programs\XAUUSD_first_try_20241411\XAUUSD_DATA_RAW\XAUUSD_2021_all.csv"


from one_time_run import just_run_once

def main():

    file_path=None
    years = [2021,2022,2023]
    dest_path = "check"
    just_run_once(file_path, *years,dest_path=dest_path)
if __name__ == "__main__" :
    main()
