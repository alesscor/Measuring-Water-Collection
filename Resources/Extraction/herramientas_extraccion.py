from decimal import	Decimal
from decimal import	getcontext

DIRECTORIO_RAIZ=r"G:\My Drive\Courses\CPIC\PowerBI Avanzado\Proyecto"
URL_RAIZ="https://www.ncei.noaa.gov/data/cmorph-high-resolution-global-precipitation-estimates/access/daily/0.25deg/"
URL_ULTIMO_AÑO_MES=(2022,5)
EXTENSION="nc"
PRECISION=10


def convierte_latitud_60_a_90(latitud_60_grados:float)->Decimal:
    return Decimal(latitud_60_grados)*Decimal(1.5)

def convierte_longitud_360_a_180(longitud_360_grados:float)->Decimal:
    return Decimal(longitud_360_grados) if Decimal(longitud_360_grados) <= Decimal(180.0000) else Decimal(longitud_360_grados)-Decimal(360.0000)        

def main():
    getcontext().prec=PRECISION

if __name__ == "__main__":
    main()
