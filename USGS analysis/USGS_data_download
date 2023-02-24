from valid_station import valid_station
from daily_data import daily_data
import os
import datetime
import pandas as pd


start = datetime.datetime.now()

print('Run started')

parent_dir = r'D:/OneDrive/OneDrive - The University of Alabama/NIDIS/usgs_data'

state_raw = pd.read_csv('D:/OneDrive/OneDrive - The University of Alabama/NIDIS/usgs_data/states.txt', delimiter=',')

state = ['al']

for i in range(len(state)):

    error_stations = []

    directory = state[i]

    path_1 = os.path.join(parent_dir, directory)

    os.makedirs(path_1)

    path_2 = os.path.join(path_1, 'error_stations')

    os.makedirs(path_2)

    raw_data = valid_station(status='all', state=state[i])

    raw_data = raw_data[raw_data['stat_cd'] == 3]

    raw_data = raw_data[raw_data['site_tp_cd'] == 'ST']

    dup_list = raw_data[raw_data.duplicated(subset=['site_no'])]['site_no'].tolist()

    modified_data = raw_data['site_no']

    for j in range(len(modified_data)):

        print(j, '/', len(modified_data))

        data_raw_streamflow = daily_data(site=str(modified_data.iloc[j])).reset_index()

        if len(data_raw_streamflow) != 0:

            min_year = data_raw_streamflow.datetime.dt.year.min()

            max_year = data_raw_streamflow.datetime.dt.year.max()

            if modified_data.iloc[j] not in dup_list:

                data_raw_streamflow.columns = ['Datetime', 'USGS_flow', 'qualifiers', 'USGS_ID']

                data_raw_streamflow['variable'] = 'streamflow'

                data_raw_streamflow.USGS_ID = data_raw_streamflow.USGS_ID.apply('="{}"'.format)

                data_raw_streamflow['measurement_unit'] = 'ft\u00b3/s'

                data_raw_streamflow = data_raw_streamflow[
                    ['Datetime', 'USGS_flow', 'variable', 'USGS_ID', 'measurement_unit',
                     'qualifiers']]

                path_writing = r'D:/OneDrive/OneDrive - The University of Alabama/NIDIS/usgs_data/' + state[i] + '/'

            if modified_data.iloc[j] in dup_list:

                path_writing = r'D:/OneDrive/OneDrive - The University of Alabama/NIDIS/usgs_data/' + state[i] + \
                               '/error_stations/'

            sheet = str(modified_data.iloc[j]) + "_" + str(min_year) + '_' + str(max_year)

            data_raw_streamflow.to_csv(path_writing + sheet + ".csv", index=False, encoding="cp1252")

        else:

            error_stations.append(modified_data.iloc[j])

    path_writing = r'D:/OneDrive/OneDrive - The University of Alabama/NIDIS/usgs_data/' + state[i] + '/'

    raw_data.to_csv(path_writing + 'station information' + ".csv", index=False)

    total_stations = len(raw_data) - len(dup_list)

    duplicate_stations = len(dup_list)

    empty_stations = len(error_stations)

    if os.path.exists(path_writing + "info.txt") is False:

        f = open(path_writing + "info.txt", "x")

        f.write("Creation of first files on " + datetime.datetime.today().strftime('%d %B %Y'))

    else:

        f = open(path_writing + "info.txt", "r")

        lines = len(f.readlines())

        f = open(path_writing + "info.txt", "a")

        f.write("\nUpdate " + str(lines - 1) + ' on ' + datetime.datetime.today().strftime('%d %B %Y'))

    f.write("\nTotal number of stations = " + str(total_stations))

    f.write("\nTotal number of duplicate stations = " + str(duplicate_stations))

    f.write("\nTotal number of empty stations = " + str(empty_stations))

    f.write("\nThese stations had no data = " + ", ".join(error_stations))

    f.write("\nThese stations had duplicates = " + ", ".join(dup_list))

    f.write("\n=================================================================================================")

    f.close()

    print(state[i], 'finished')

    print(state[i], 'Run Time:', str(datetime.datetime.now() - start))

print('Total Run Time:', str(datetime.datetime.now() - start))

'''aa = valid_station(status='all', state=['az'])

bb = daily_data(site='09502750').reset_index()'''
