def fetch_sales():
    print('fetching the sales data')

def filter_valid_sales():
    print("filtering valid sales data")

def summarize_data():
    print("summaries sales data")

def generate_report(): #a single method will call all the above methods 
    fetch_sales()
    filter_valid_sales()
    summarize_data()
    print('report is ready')

generate_report()