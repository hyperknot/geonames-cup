#!/usr/bin/env python3

import os
import sys
import csv

from aerofiles.seeyou import Writer


def process(file_path, minpop=100):
    data = parse_geonames_txt(file_path, minpop)
    dirname, txt_name = os.path.split(file_path)
    cup_path = os.path.join(dirname, txt_name[:-3] + 'cup')
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
        for name, coordinates in data.items():
            writer.write_waypoint(name, name, '', coordinates['lat'], coordinates['lon'])



if len(sys.argv) == 1:
    sys.exit('Usage: process.py country.txt <min population>')

if len(sys.argv) == 2:
    process(sys.argv[1])

if len(sys.argv) == 3:
    process(sys.argv[1], int(sys.argv[2]))

