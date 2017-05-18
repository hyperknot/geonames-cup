#!/usr/bin/env python3

import os
import sys
import csv

from aerofiles.seeyou import Writer


presets = {
    'full': 0,
    'medium': 100,
    'small': 5000
}


def process(file_path):
    for preset, minpop in presets.items():
        data = parse_geonames_txt(file_path, minpop)
        dirname, txt_name = os.path.split(file_path)
        cup_path = os.path.join(dirname, txt_name[:-4] + '-{}.cup'.format(preset))
        write_cup(cup_path, data)


def parse_geonames_txt(file_path, minpop):
    if not os.path.isfile(file_path):
        sys.exit('File not found')

    data = dict()

    with open(file_path) as csv_file:
        reader = csv.reader(csv_file, delimiter='\t')

        for line in reader:
            name = line[1]
            lat = line[4]
            lon = line[5]
            feature_class = line[6]
            feature_code = line[7]
            population = int(line[14])

            if feature_class != 'P':
                continue

            if feature_code in ['PPLX']:
                continue

            if minpop and population < minpop:
                continue

            data[name] = {
                'lat': float(lat),
                'lon': float(lon),
            }

    return data


def write_cup(file_path, data):
    with open(file_path, 'wb') as fp:
        writer = Writer(fp)
        print(len(data), 'points')
        for name in sorted(data.keys()):
            coordinates = data[name]
            writer.write_waypoint(name, name, '', coordinates['lat'], coordinates['lon'])



if len(sys.argv) == 1:
    sys.exit('Usage: process.py country.txt')

if len(sys.argv) == 2:
    process(sys.argv[1])

# if len(sys.argv) == 3:
    # process(sys.argv[1], int(sys.argv[2]))

