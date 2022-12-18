# Extraction tools

The data source contains Climate Data Records, which file format is netCDF4, `.nc` file extension. They are extracted from NOAA's NCEI directory at `https://www.ncei.noaa.gov/data/cmorph-high-resolution-global-precipitation-estimates/access/daily/0.25deg/`.

## Some attributes

### Summary:
~~~py
import netCDF4 as nc
import xarray as xr
fn = r"CMORPH_V1.0_ADJ_0.25deg-DLY_00Z_20210102.nc"
ds = xr.open_dataset(fn)
print(ds.summary)
~~~

Output:

>The CMORPH CDR is a reprocessed and bias-corrected global precipitation product created on an 8kmx8km grid over the globe (60S-60N) and in a 30-minute temporal resolution for an 18-year period from January 1998 to the present. First, the purely satellite based CMORPH precipitation estimates (raw CMORPH) are reprocessed. The integration algorithm is fixed and the input Level 2 passive microwave (PMW) retrievals of instantaneous precipitation rates are from identical versions throughout the entire data period. Bias correction is then performed for the raw CMORPH through probability density function (PDF) matching against the CPC daily gauge analysis over land and through adjustment against the Global Precipitation Climatology Program (GPCP) pentad merged analysis of precipitation over ocean. The reprocessed, bias-corrected CMORPH exhibits improved performance in representing the magnitude, spatial distribution patterns and temporal variations of precipitation over the global domain from 60S to 60N. Bias in the CMORPH satellite precipitation estimates is almost completely removed over land during warm seasons (May – September), while during co seasons (October - April) CMORPH tends to under-estimate the precipitation due to the less-than-desirable performance of the current generation PMW retrievals in detecting and quantifying snowfall and cold season rainfall. Details of the CMORPH CDR may be found in Xie et al. (2017).

### References:
~~~py
print(ds.references)
~~~

Output:

> Xie, P., et al. (2017), Reprocessed, Bias-Corrected CMORPH Global High-Resolution Precipitation Estimates from 1998, J. Hydrometeorol., 18, 1617-1641 (DOI:10.1175/JHM-D-16-0168.1)

### Geospatial resolution:
~~~py
print("geospatial_lat_min:",ds.geospatial_lat_min)
print("geospatial_lat_resolution:",ds.geospatial_lat_resolution)
print("geospatial_lat_units:",ds.geospatial_lat_units)
print("geospatial_lon_max:",ds.geospatial_lon_max)
print("geospatial_lon_min:",ds.geospatial_lon_min)
print("geospatial_lon_resolution:",ds.geospatial_lon_resolution)
print("geospatial_lon_units:",ds.geospatial_lon_units)
~~~

Output:
>geospatial_lat_max: 60.0<br/>
>geospatial_lat_min: -60.0<br/>
>geospatial_lat_resolution: 0.25<br/>
>geospatial_lat_units: degrees_north<br/>
>geospatial_lon_max: 360.0<br/>
>geospatial_lon_min: 0.0<br/>
>geospatial_lon_resolution: 0.25<br/>
>geospatial_lon_units: degrees_east<br/>

