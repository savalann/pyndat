from valid_station import valid_station
import matplotlib.pyplot as plt
import numpy as np
import datetime
import pandas as pd
import glob
import os
import seaborn as sns

start = datetime.datetime.now()


def data_preparation():

    state_raw = (pd.read_csv('D:/OneDrive/OneDrive - The University of Alabama/NIDIS/usgs_data/states.txt',
                             delimiter=','))  # Read file containing the state names.

    state = (state_raw.iloc[:, 0].str.replace(r"'", "")).tolist()  # Convert the state names to a list.

    #state = ['al', 'az']

    path_writing = r'D:/OneDrive/OneDrive - The University ' \
                   r'of Alabama/NIDIS/stations_statistics'  # The path of files for saving and reading them.

    frames = {}

    for i in range(len(state)):  # Reading the problematic stations

        path_reading = r'D:/OneDrive/OneDrive - The University ' \
                       r'of Alabama/NIDIS/usgs_data/' + state[i] + '/'  # The path for reading the problematic stations

        with open(path_reading + "info.txt", "r") as f:  # Open the text files containing the station names.

            lines = f.readlines()[5]  # Read the line with station names.

            error_list = [x.replace('\'', '') for x in lines[32:-1].split(', ')]  # Read the station names and convert
            # them to list.

        raw_data = valid_station(status='all', state=state[i])  # Get the stations list.

        data = raw_data[raw_data['stat_cd'] == 3]  # Get the station list which have average of each day.

        data = data[data['site_tp_cd'] == 'ST']  # Get the station list which have stream data.

        data['begin_date'] = pd.to_datetime(data['begin_date'])  # Convert the type of the date columns to datetime.

        data['end_date'] = pd.to_datetime(data['end_date'])  # Convert the type of the date columns to datetime.

        if error_list:  # See whether the error list is not empty.

            data = data[~data['site_no'].isin(error_list)]  # Remove the problematic stations from the list.

        frames[state[i]] = data

    return frames


def conus_statistic():

    state_data = data_preparation()

    all_percent = np.zeros(10)  # The percent of the least number of years of data.

    all_stations = 0  # Valid station numbers

    missing_station = 0  # Number of station with missing data.

    missing_value = 0  # The missing data value in each state.

    states = list(state_data.keys())

    for jj in range(len(states)):

        data_percent = np.zeros(10)

        data = state_data[states[jj]]

        all_stations += len(data)  # Number of station in each state.

        for j in range(10):  # Find the minimum number of years of data in each state.

            data_percent[j] = np.round(data.loc[data['count_nu'] > 365 * (j + 1) * 10].shape[0], 0)

        all_percent += data_percent  # Find the minimum number of years of data in the CONUS.

        for z in range(len(data)):  # Find the stations with missing data.

            delta = (data.iloc[z, 22] - data.iloc[z, 21]).days + 1  # Find the range of data based on information table.

            if delta > data.iloc[z, 23]:  # Compare the range with number of data based on information table.

                missing_station += 1  # Number of stations with missing value.

                missing_value += data.iloc[z, 23] / delta * 100  # Summing up the percentage of missing value
                # of all stations.

    indexes_dataframe = []  # The index list for dataframe.

    indexes_fig = []  # The index list for figure.

    for i in range(10):  # Creating the index list for dataframe and figure.

        indexes_dataframe.append('More than ' + str((i + 1) * 10) + ' years data (%)')

        indexes_fig.append(str((i + 1) * 10) + ' years')

    all_percent_final = pd.DataFrame(np.round(all_percent / all_stations * 100, 0), index=indexes_dataframe,
                                     columns=['missing data value (%)'])    # Finding the percentage of stations
    # with various number of minimum data (e.g. at least 10 years of data or at least 20 years of data).

    conus_missing_stations = round(missing_station / all_stations * 100, 0)  # The percentage of stations
    # with missing data in the CONUS.

    conus_missing_value = round(missing_value / all_stations, 0)  # The percentage of the missing data in the CONUS.

    fig, axs = plt.subplots(dpi=300, tight_layout=True)

    axs.bar(indexes_fig, all_percent_final.iloc[:, 0].to_numpy())

    plt.xticks(rotation=30, ha='right')

    axs.set(xlabel='Number of Minimum Years of Data', ylabel='Number of Stations (%)',
            title='Number of Stations with Minimum Years of Data in CONUS')

    plt.show()

    return all_percent_final, all_stations, conus_missing_stations, conus_missing_value, fig

now_test = conus_statistic()

now_test[4].savefig("n_1")

def state_statistic():

    state_data = data_preparation()

    all_state_percent = np.zeros((len(state_data), 10))  # The percent of the least number of years of data for
    # each state.

    all_state_missing = np.zeros((len(state_data), 3))  # The percent of missing data and missing data value
    # in each state

    states = list(state_data.keys())

    for jj in range(len(states)):

        data_percent = np.zeros(10)

        data = state_data[states[jj]]

        for j in range(10):  # Find the minimum number of years of data in each state.

            all_state_percent[jj, j] = np.round(data.loc[data['count_nu'] > 365 * (j + 1) * 10].shape[0]
                                               / len(data) * 100, 0)

        missing_station = 0  # Number of station with missing data.

        missing_value = 0  # The missing data value in each state.

        for z in range(len(data)):  # Find the stations with missing data in each state.

            delta = (data.iloc[z, 22] - data.iloc[z, 21]).days + 1  # Find the range of data based on information table.

            if delta > data.iloc[z, 23]:  # Compare the range with number of data based on information table.

                missing_station += 1  # Number of stations with missing value.

                missing_value += data.iloc[z, 23] / delta * 100  # Summing up the percentage of missing value
                # of all stations.

        all_state_missing[jj, 0] = len(data)

        all_state_missing[jj, 1] = np.round(missing_station / len(data), 2) * 100

        all_state_missing[jj, 2] = np.round(missing_value / len(data), 0)

    indexes_dataframe = []  # The index list for dataframe.

    for i in range(10):  # Creating the index list for dataframe and figure.

        indexes_dataframe.append('More than ' + str((i + 1) * 10) + ' years data (%)')

    all_state_percent = pd.DataFrame(all_state_percent, index=states, columns=indexes_dataframe).reset_index()

    all_state_missing = pd.DataFrame(all_state_missing, index=states,
                                     columns=['Number of stations', 'stations with missing data (%)',
                                              'missing data value (%)']).reset_index()

    return all_state_missing, all_state_percent


now_test_1 = state_statistic()[1]

now_test_1 = now_test_1.set_index('index')

test_2 = now_test_1.div(now_test_1.max(axis=1), axis=0)

fig, axs = plt.subplots(dpi=300, figsize=(10, 15), tight_layout=True)

plt.rcParams["font.family"] = "Times New Roman"

axs = sns.heatmap(test_2, linewidth=0.5, fmt=".0f", annot=now_test_1, annot_kws={'fontsize': 15},
                  cbar=False)

plt.title(label='Number of Stations with Minimum Years of Data in Each State (%)', fontsize=22, pad=10)

axs.set_xticklabels([str(i) for i in range(10, 110, 10)], rotation=0, size=18)

plt.yticks(rotation=0, size=18)

plt.xlabel(xlabel='Minimum Years of Data', size=20)

plt.ylabel(ylabel='States', size=20)

plt.savefig("n_2")



now_test_2 = state_statistic()[0]

now_test_2 = now_test_2.set_index('index')

test_2 = now_test_2.div(now_test_2.max(axis=0), axis=1)

fig, axs = plt.subplots(dpi=300, figsize=(10, 15), tight_layout=True)

plt.rcParams["font.family"] = "Times New Roman"

axs = sns.heatmap(test_2, linewidth=0.5, fmt=".0f", annot=now_test_2, annot_kws={'fontsize': 15},
                  cbar=False)

plt.xticks(rotation=0, size=18)

plt.yticks(rotation=0, size=18)

plt.title(label='Missing Data in Each State', size=22)

plt.ylabel(ylabel='States', size=20)

plt.savefig("n_3")
































'''    
aa = state_statistic()

bb = conus_statistic()

state = list(data_preparation().keys())

for i in range(len(state)):

    print(state[i])

    folder_path = r'D:/OneDrive/OneDrive - The University of Alabama/NIDIS/usgs_data/' + state[i]

    aa = glob.glob(os.path.join(folder_path, '*.csv'))

    for filename in glob.glob(os.path.join(folder_path, '*.csv')):

        if filename[68:-4] != 'station information':

            df = pd.read_csv(filename, encoding='unicode_escape')






'''




state = list(data_preparation().keys())

df_test = pd.DataFrame(np.zeros([len(state), 122]), index=state)

for i in range(len(state)):

    print(state[i])

    folder_path = r'D:/OneDrive/OneDrive - The University of Alabama/NIDIS/usgs_data/' + state[i]

    aa = glob.glob(os.path.join(folder_path, '*.csv'))

    for filename in glob.glob(os.path.join(folder_path, '*.csv')):

        if filename[68:-4] != 'station information':

            df = pd.read_csv(filename, encoding='unicode_escape')

            df['Datetime'] = pd.to_datetime(df['Datetime'])  # Convert the type of the date columns to datetime.

            uu = df['Datetime'].dt.year.drop_duplicates().reset_index(drop=True)

            for z in uu:

                df_test.iloc[i, z-1900-1] += 1



df_test.loc['Total']= df_test.sum()

test = df_test.iloc[:-1, :]

test_2 = df_test.div(df_test.max(axis=1), axis=0)
import seaborn as sns
flights_long = sns.load_dataset("flights")
flights = flights_long.pivot("month", "year", "passengers")



fig, axs = plt.subplots(dpi=300,figsize=(40,40), tight_layout=True)

plt.rcParams["font.family"] = "Times New Roman"

axs = sns.heatmap(test_2.T, linewidth=0.5, fmt=".0f", annot=df_test.T, annot_kws={'fontsize': 18},
                  cbar_kws={"anchor": (1.0, 0.5), 'pad': -0.1,  'aspect': 40, 'shrink': 0.5, 'extend': 'min'})

cbar = axs.collections[0].colorbar

cbar.set_ticks([0, 0.5, 0.9])

cbar.set_ticklabels(['low', 'medium', 'high'], rotation=45)

cbar.ax.tick_params(labelsize=25)

cbar.ax.yaxis.set_ticks_position('left')

plt.title(label='Number of Stations Based on Data Length in Each State', fontsize=30, pad=10)

plt.rc('xtick', labelsize=20)

axs.set_yticklabels([str(i) for i in range(1900, 2022)], rotation=0, size=20)

plt.xlabel(xlabel='States', fontsize=25)

plt.ylabel(ylabel='Years', fontsize=25)

plt.savefig("n_4")
















print('Total Run Time:', str(datetime.datetime.now() - start))

