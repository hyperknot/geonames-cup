# geonames-cup
Geonames places processor and CUP GPS file converter

Install the requirements: `pip install -r requirements.txt`

Download and unzip the wanted `<country>.zip` file from geonames.org:
[http://download.geonames.org/export/dump/](http://download.geonames.org/export/dump/)

Run `process.py <country>.txt`

The processed file will be `<country>.cup`

Options: the minimum population filter can be specified as `process.py <country>.txt 1000` to filter places with population 1000+ for example. 0 disables the filter, the default is 100.


