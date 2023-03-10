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
 - Banten and Jawa Barat, Indonesina provinces (place of interest for being the nearest antipode to Costa Rica) `$lat$  >= -8.15 AND $lat$<=-5.85 AND $lon$>=105.00 AND $lon$<=108.94`,
 - Mawsynram, Meghalaya State, India (place of control, one of the rainiest in the globe according to ["The top 10 wettest places on earth",
Escape dot com dot au writers	on March 23, 2021, captured on December 18, 2022](https://www.escape.com.au/escape-travel/the-top-10-wettest-places-on-earth/news-story/993eaffca1d3d5fabc0c9d73bef06b96)) `$lat$  >= 25.3000 AND $lat$<=25.5000 AND $lon$>=91.610 AND $lon$<=91.630`,
 - Arica, Chile (place of control, one of the driest in the globe according to ["The 10 Driest Places on Earth", Katharine Gammon,
 Live Science dot com on July 22, 2011, captured on December 18, 2022](https://www.livescience.com/30627-10-driest-places-on-earth.html) and ["Discover the Driest Place on Earth – 500 Years Without a Single Rain Drop!", Kristen Holder, AZ Animals dot com, July 26, 2022, captured on December 18, 2022](https://a-z-animals.com/blog/discover-the-driest-place-on-earth-500-years-without-a-single-rain-drop/)) `$lat$  >= -18.5 AND $lat$<=-18.00 AND $lon$>=-70.40 AND $lon$<=-70.320`.
 
To translate from the data source geolocation into the target resolution, these functions were applied to latitude and longitude, with 10 decimals precision:
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

### Getting the terrestrial surface of interest

The terrestrial surface points of interest must be obtained from the initial squared zones. For this purpose KNIME Analytics Platform Palladian geolocation nodes that interact with GeoNames free service were applied. The nodes applied were:
- **GeoNames Location Source**: to obtain a session of GeoNames service.
- **Reverse Location Lookup**: to obtain information of places on the surface that are near a point of interest, inside of a given radio for looking up.
- **Map Viewer**: to verify what points are selected or left behind by the algorithms, for example if a point resulted with no information because of being too far from the nearest town.
- **Latitude/Longitude to Coordinate**: to transform from double type latitude and longitude into Palladian's coordenates data type.

The following procedure was executed next, the case of Banten and Jawa Barat is shown in figure 1 (equivalent procedure was applied in the case of Costa Rica):

| <img src="Nodos y selección puntos en tierra firme.png" alt="The KNIME nodes to recover names on the land (among further information)" /> |
|:--:|
| **Fig. 1** *The KNIME nodes to recover names on the land (among further information)* |
1. Regard a GeoNames service session as an input.
2. Regard the points that are inside the area of the location of interest as input (they come already filtered in form of square). 
3. Obtain the information, including vernacle name, of each point from the GeoNames service, using a search radio. Example of output is shown in figure 2.

| <img src=" Puntos en tierra firme con faltantes.png" alt="Example with six missing points due to being far of the nearest point with GeoNames information" /> |
|:--:|
| **Fig. 2** *Example with six missing points due to being far of the nearest point with GeoNames information* |

4. Obtain the points whose information have not being found using the first search radio.
5. Visualise the points of interst to "hilite" the ones must be found in a second attempt. Example of input is shown in figure 3, black dots in yellow outline.


| <img src=" Selección puntos en tierra firme.png" alt="Example with six missing points due to being far from the nearest place with GeoNames information" /> |
|:--:|
| **Fig. 3** *Example of "hiliting" the six missing points in yellow outline* |


6. Obtain the "hilited" points to search again.
7. Obtain the vernacle name of each point from the GeoNames service, using a longer search radio.
8. Concatenate the results.
9. Automatically mark if the points corresponds to the country of interest.
10. Filter those points that are in the country of interest.
11. Obtain the name of the place nearest to each point.
12. Complete the information of resulting nearest places.
13. Visualise the obtained points (this node can be used with the output of node [7] to verify points that are left behind).
14. Provide the output of the points from the surface with their information




# To follow-up

- To explain that I still feel skeptical with the process I followed, the precipitation data for the control coordinates that are assumed among the driest and rainiest places, don't seem like that after the transformation I followed.
- To explain that there are new KNIME nodes integrated to OpenStreetMap services that have not been applied yet that may have interesting features in favour of this project.
- Review data of latitude 9°55'13.0"N and -84°16'22.0"E (Mora, San José).
# References to take advantage of
- [Estaciones automáticas](https://www.imn.ac.cr/web/imn/estaciones-automaticas)
- [Estación Automática de la UCR Santa Cruz, Guanacaste](https://www.imn.ac.cr/especial/estacionStacruz.html)
- [Estación Automática Universidad de la Paz, Mora, San José](https://www.imn.ac.cr/especial/estacionUPaz.html)
- [IMN Servicios - Resúmenes climáticos](https://www.imn.ac.cr/web/imn/solicitud-de-servicios?p_auth=H3zy8YLy&p_p_id=PortalIMNFormularioServicios_WAR_PortalIMNFormularioServiciosportlet&p_p_lifecycle=1&p_p_state=normal&p_p_mode=view&p_p_col_id=column-3&p_p_col_count=1&_PortalIMNFormularioServicios_WAR_PortalIMNFormularioServiciosportlet__facesViewIdRender=%2Fviews%2FpagEnvioServicio.xhtml)
- [REGIONES Y SUBREGIONES CLIMATICAS DE COSTA RICA (Solano, Villalobos, ¿1996?)](https://www.imn.ac.cr/documents/10179/20909/Regionalizaci%C3%B3n+clim%C3%A1tica+de+Costa+Rica)
