# Extraction and transformation tools

## The data source
The data source contains global daily Climate Data Records, which file format is netCDF4, `.nc` file extension. It can be extracted from NOAA's NCEI directory at https://www.ncei.noaa.gov/data/cmorph-high-resolution-global-precipitation-estimates/access/daily/0.25deg/.

### Some attributes

#### Summary:
~~~py
import netCDF4 as nc
import xarray as xr
fn = r"CMORPH_V1.0_ADJ_0.25deg-DLY_00Z_20210102.nc"
ds = xr.open_dataset(fn)
print(ds.summary)
~~~

Output:

>The CMORPH CDR is a reprocessed and bias-corrected global precipitation product created on an 8kmx8km grid over the globe (60S-60N) and in a 30-minute temporal resolution for an 18-year period from January 1998 to the present. First, the purely satellite based CMORPH precipitation estimates (raw CMORPH) are reprocessed. The integration algorithm is fixed and the input Level 2 passive microwave (PMW) retrievals of instantaneous precipitation rates are from identical versions throughout the entire data period. Bias correction is then performed for the raw CMORPH through probability density function (PDF) matching against the CPC daily gauge analysis over land and through adjustment against the Global Precipitation Climatology Program (GPCP) pentad merged analysis of precipitation over ocean. The reprocessed, bias-corrected CMORPH exhibits improved performance in representing the magnitude, spatial distribution patterns and temporal variations of precipitation over the global domain from 60S to 60N. Bias in the CMORPH satellite precipitation estimates is almost completely removed over land during warm seasons (May – September), while during co seasons (October - April) CMORPH tends to under-estimate the precipitation due to the less-than-desirable performance of the current generation PMW retrievals in detecting and quantifying snowfall and cold season rainfall. Details of the CMORPH CDR may be found in Xie et al. (2017).

#### References:
~~~py
print(ds.references)
~~~

Output:

> Xie, P., et al. (2017), Reprocessed, Bias-Corrected CMORPH Global High-Resolution Precipitation Estimates from 1998, J. Hydrometeorol., 18, 1617-1641 (DOI:10.1175/JHM-D-16-0168.1)

#### Geospatial resolution:
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

## The extraction

The data extacted corresponds to points on the terrestrial surface of the following locations, regarding a geospacial resolution of -90 to 90 degrees north and -180 to 180 degrees east:
 - Costa Rica (place of interest for being my home country) `$lat$  >= 8.041537 AND $lat$<=11.219708 AND $lon$>=-85.949918 AND $lon$<=-82.552560`,
 - Banten and Jawa Barat, Indonesina provinces (place of interest for being the nearest antipode to Costa Rica) `$lat$  >= -8.15 AND $lat$<=-5.80 AND $lon$>=105.00 AND $lon$<=108.94`,
 - Mawsynram, Meghalaya State, India (place of control, one of the rainiest in the globe according to [The top 10 wettest places on earth,
Escape dot com dot au writers	on March 23,2021, captured on December 18, 2022](https://www.escape.com.au/escape-travel/the-top-10-wettest-places-on-earth/news-story/993eaffca1d3d5fabc0c9d73bef06b96)) `$lat$  >= 25.3000 AND $lat$<=25.5000 AND $lon$>=91.610 AND $lon$<=91.630`,
 - Jaisalmer, Rajasthan, India (place of control, one of the driest in the globe) `$lat$  >= 26.806514 AND $lat$<=26.979810 AND $lon$>=70.676399 AND $lon$<=70.999946`.
 
To translate from the data source geolocation into the target one, these functions were applied to latitude and longitude:
~~~py
from decimal import	Decimal
from decimal import	getcontext

def convierte_latitud_60_a_90(latitud_60_grados:float)->Decimal:
    return Decimal(latitud_60_grados)*Decimal(1.5000)

def convierte_longitud_360_a_180(longitud_360_grados:float)->Decimal:
    return Decimal(longitud_360_grados) if Decimal(longitud_360_grados) <= Decimal(180.0000) else Decimal(longitud_360_grados)-Decimal(360.0000)        

def main():
    getcontext().prec=10

if __name__ == "__main__":
    main()

~~~
