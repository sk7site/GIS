##inImage_red=raster
##inImage_nir=raster
##outImage=output raster

from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry

lyr = processing.getObject(inImage_red)
entries=[]
rasterCalcEntry=QgsRasterCalculatorEntry()
rasterCalcEntry.ref='R@1'
rasterCalcEntry.raster=lyr
rasterCalcEntry.bandNumber=1
entries.append(rasterCalcEntry)

lyr = processing.getObject(inImage_nir)
rasterCalcEntry=QgsRasterCalculatorEntry()
rasterCalcEntry.ref='NIR@1'
rasterCalcEntry.raster=lyr
rasterCalcEntry.bandNumber=1
entries.append(rasterCalcEntry)

if not ".tif" in outImage:
    outImage=outImage+".tif"

noData=-3.4028234663852886e+38
calc=QgsRasterCalculator('1.0*(NIR@1 - R@1)/(NIR@1 + R@1)+0.0', outImage, "GTiff",  lyr.extent(), lyr.crs(), lyr.width(), lyr.height(), entries)
calc.processCalculation()