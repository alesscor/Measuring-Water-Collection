import sys
import glob
import pandas as pd
import netCDF4 as nc
import xarray as xr
sys.path.append("/.../Extraction")
import herramientas_extraccion as he

fn = he.DIRECTORIO_RAIZ+r"\Datos\Lugares de interés y control.csv"
df = pd.read_csv(fn)
df.drop(inplace=True, labels=["Location Name","Location Type","Clasificación"],axis=1)
print(df.columns)
df_resultado = None

for i,archivo in enumerate(glob.glob(he.DIRECTORIO_RAIZ+r"\Datos\CMORPH\*.nc")): 
    # print(i,archivo)
    if True:
        ds_i = xr.open_dataset(archivo)
        df_i = ds_i.to_dataframe()
        df_i.reset_index(inplace=True)
        df_i.drop(inplace=True, labels=["time_bounds", "lat_bounds", "lon_bounds"],axis=1)
        # print(ds_i)
        # print(df_i.columns)        
        # df_i.to_csv(r"G:\My Drive\Courses\CPIC\PowerBI Avanzado\Proyecto\Datos\Caso_"+ str(i )+ r".csv")
        df_i["lat"] = df_i["lat"].apply(he.convierte_latitud_60_a_90)
        df_i["lon"] = df_i["lon"].apply(he.convierte_longitud_360_a_180)        
        # print(df_i.columns)

        combinación = pd.merge(df,df_i,how="inner",on=["lat","lon","nv"])

        # print(combinación.columns)
        # print(combinación)
        if df_resultado is None:
            df_resultado = combinación
        else:
            df_resultado = pd.concat([df_resultado,combinación],ignore_index=True)
    if False and i==6:
        break
    # print(df_resultado.columns)
    print(df_resultado)
df_resultado.to_csv(he.DIRECTORIO_RAIZ+r"\Datos\CMORPH zonas de interés y control.csv", index=False)