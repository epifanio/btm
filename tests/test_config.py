# our constants.

import os

local_path = os.path.dirname(__file__)
data_path = os.path.join(local_path, 'data')

base_xml = os.path.abspath(os.path.join(data_path, 'fagatelebay.xml'))
base_csv = os.path.abspath(os.path.join(data_path, 'fagatelebay.csv'))
base_excel = os.path.abspath(os.path.join(data_path, 'fagatelebay.xlsx'))
malformed_csv = os.path.abspath(
    os.path.join(data_path, 'missing_comma_zone.csv'))
zones_excel = os.path.abspath(os.path.join(data_path, 'fagatelebay_zone.xlsx'))
zones_xml = os.path.abspath(os.path.join(data_path, 'fagatelebay_zone.xlsx'))
bathy_raster = os.path.abspath(os.path.join(data_path, 'bathy5m_clip.tif'))
# a set of precomputed results with Broad(1,5) and Fine(1,3)
# to facilitate running the test suite.
slope_raster = os.path.abspath(os.path.join(data_path, 'slope.tif'))
broad_std_raster = os.path.abspath(os.path.join(data_path, 'broad_std.tif'))
fine_std_raster = os.path.abspath(os.path.join(data_path, 'fine_std.tif'))
# Kurtosis, stored as a NumPy array
kurtosis_npy = os.path.abspath(os.path.join(data_path, 'kurtosis.npy'))
# area of interest for ACR tests
aoi = os.path.abspath(os.path.join(data_path, 'areaofinterest.shp'))
aoi_multipart = os.path.abspath(os.path.join(data_path, 'areaofinterest_mp.shp'))

# an MXD with two bpi layers
bpi_grids_mxd = os.path.abspath(os.path.join(data_path, 'bpi_grids.mxd'))
# same as above, but as an APRX for Pro
bpi_grids_aprx = os.path.abspath(os.path.join(data_path, 'bpi_grids.aprx'))

pyt_file = os.path.abspath(
    os.path.join(local_path, '..', 'Install', 'toolbox', 'btm.pyt'))
