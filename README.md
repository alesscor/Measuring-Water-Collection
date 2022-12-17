# Measuring water collection
Related to rain precipitation in Costa Rica and its near antipode, part of current Indonesia, Banten and Jawa Barat. From both places it compares and visualises water precipitation and estimates of local water collection.

It uses information from NOAA's NCEI (National Oceanic and Atmosperic Administration's National Centers for Environmental Information), specifically from [NOAA Climate Data Record (CDR) of CPC Morphing Technique (CMORPH) High Resolution Global Precipitation Estimates, Version 1](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc:C00948). This source provides global daily/hourly precipitation information computed and curated by ground and satellite points of views.

 - The information from NOAA is extracted by a Python tool to compose a data source with global CDRs per day.
 - Names of places of interest, on the abovementioned territories, are obtined thru the free [GeoNames database](http://www.geonames.org/) service.
 - Some ETL is applied on the data source in KNIME Analytics Platform using [Palladian Geo Nodes](https://hub.knime.com/spatialdatalab/extensions/sdl.harvard.features.geospatial/latest).
 - The visualisation and dashboard are provided by a MS PowerBI document.
