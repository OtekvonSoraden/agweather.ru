# from selenium.webdriver.common.by import By
from datascraper.forecasts import month_name_to_number, get_soup
from datetime import datetime, timedelta
import re


#############################
# ARCHIVE SCRAPER FUNCTIONS #
#############################


def arch_rp5(start_datetime: datetime, url, end_datetime=None):
    """Archive scraper function from RP5 source"""

    #  Default archive end in past 01.05.2023 00:00 local time
    if not end_datetime:
        end_datetime = start_datetime.replace(
            year=2023, month=5, day=1, hour=0)
        step_option = '30'  # 30 days
    else:
        step_option = '1'  # 1 day

    payload = {'pe': step_option}

    # While cycle back in past to end_datetime.
    arch_data, date_ = [], start_datetime
    while date_ > end_datetime:

        payload['ArchDate'] = date_.strftime("%d.%m.%Y")

        # parsing archive table
        soup = get_soup(url, payload)
        atab = soup.find('table', id='archiveTable')

        # Parsing start date from source html page
        start_date_from_source = atab.find('td', class_='cl_dt').\
            get_text().replace('г.', ' ').replace(',', ' ').split()[:-1]
        start_date_from_source = start_datetime.replace(
                year=int(start_date_from_source[0]),
                month=month_name_to_number(start_date_from_source[2]),
                day=int(start_date_from_source[1]),
                hour=0)

        atab = atab.find_all('tr')[1:]
        atab = [row.find_all('td')[-29:] for row in atab]

        datetime_ = start_date_from_source
        prev_time = None
        for i, row in enumerate(atab):

            time = int(row[0].get_text())
            datetime_ = datetime_.replace(hour=time)
            # print('+', datetime_.isoformat())
            # print(prev_time, time)
            if i != 0 and prev_time < time:
                datetime_ -= timedelta(days=1)
            prev_time = time

            # temp = float(row[1].find(
            #     'div', class_='t_0 dfs').get_text())
            temp = row[1].find('div', class_='t_0 dfs')
            temp = float(temp.get_text()) if temp else None

            press = row[2].find('div', class_='p_0 dfs')
            press = float(press.get_text()) if press else None
            wind_vel = row[7].find('div', class_='wv_0')
            wind_vel = wind_vel.get_text() if wind_vel else None
            wind_vel = int(re.findall(r'\d+', wind_vel)[0]) \
                if wind_vel else 0
            record = [datetime_, [temp, press, wind_vel]]
            if record not in arch_data and datetime_ > end_datetime:
                arch_data.append(record)

        date_ -= timedelta(days=30)

    # END While cycle

    return arch_data
