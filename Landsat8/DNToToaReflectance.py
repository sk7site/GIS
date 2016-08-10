##reflectance_mult=number 0
##reflectance_add=number 0
##sun_elevation=number 0
##inImage=raster
##outImage=output raster

from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry

lyr = processing.getObject(inImage)
entries=[]
rasterCalcEntry=QgsRasterCalculatorEntry()
rasterCalcEntry.ref='IMG@1'
rasterCalcEntry.raster=lyr
rasterCalcEntry.bandNumber=1
entries.append(rasterCalcEntry)

if not ".tif" in outImage:
    outImage=outImage+".tif"

noData=-3.4028234663852886e+38
radElev = sun_elevation*3.14159/180
calc=QgsRasterCalculator('(IMG@1 != 0)*('+str(reflectance_mult)+' * IMG@1 + '+str(reflectance_add)+')/sin('+str(radElev)+') + (IMG@1 = 0) * '+str(noData), outImage, "GTiff",  lyr.extent(), lyr.crs(), lyr.width(), lyr.height(), entries)
calc.processCalculation()