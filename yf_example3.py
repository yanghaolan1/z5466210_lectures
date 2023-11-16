import os
import toolkit_config as cfg
import yf_example2
def qan_prc_to_csv(year):
    """
    parameters
    year:integer
    download stock prices from yahoo finance for a given year into a CSV file
    """
    ticker_symbol = 'QAN.AX'
    start_date = f'{year}-01-01'
    end_date = f'{year}-12-31'
    output_path = os.path.join(cfg.DATA_PATH, f'qan_prc_{year}.csv')
    df = yf_example2.yf_prc_to_csv(
        ticker_symbol = ticker_symbol,
        output_path = output_path,
        start_date = start_date,
        end_date = end_date
    )

if __name__ == "__main__":
    year = 2020,
    qan_prc_to_csv(year)