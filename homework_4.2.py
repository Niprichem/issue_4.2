import os

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt


def get_name_count_list(source, name_list, start_year, finish_year):
    data = {}
    for year in range(start_year, finish_year + 1):
        file_name = 'yob{}.txt'.format(year)
        file_data = pd.read_csv(os.path.join(source, file_name), names=['Name', 'Gender', 'Count'])
        file_data_filtered = file_data[file_data['Name'].isin(name_list)].groupby('Name').sum()
        data[year] = file_data_filtered
    data_all = pd.concat(data, names=['Year'])
    return data_all


def main():
    source = 'names'
    name_list = ['Ruth', 'Robert']
    start_year = 1900
    finish_year = 2000
    data = get_name_count_list(source, name_list, start_year, finish_year)
    data.groupby([data.index.get_level_values(0), 'Name']).sum().unstack('Name').plot()


if __name__ == '__main__':
    main()
