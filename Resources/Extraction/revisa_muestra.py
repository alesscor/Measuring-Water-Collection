import sys
import netCDF4 as nc
import xarray as xr
sys.path.append("/.../Extraction")
import herramientas_extraccion as he

fn = he.DIRECTORIO_RAIZ+r"\Datos\CMORPH\CMORPH_V1.0_ADJ_0.25deg-DLY_00Z_20210102.nc"
ds = xr.open_dataset(fn)
print(ds)
df = ds.to_dataframe()
df.reset_index(inplace=True)
df.drop(inplace=True, labels=["time_bounds", "lat_bounds", "lon_bounds"],axis=1)
df["lat"] = df["lat"].apply(he.convierte_latitud_60_a_90)
df["lon"] = df["lon"].apply(he.convierte_longitud_360_a_180)

df.to_csv(he.DIRECTORIO_RAIZ+r"\Datos\Datos de prueba CMORPH_V1.0_ADJ_0.25deg-DLY_00Z_20210102.csv",index=False)
# print("cosa:",he.DIRECTORIO_RAIZ)
