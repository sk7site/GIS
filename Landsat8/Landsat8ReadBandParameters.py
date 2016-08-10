##metafile=file
##band=number 1
##radiance_mult=output number
##radiance_add=output number
##radiance_max=output number
##reflectance_mult=output number
##reflectance_add=output number
##reflectance_max=output number

radMult="RADIANCE_MULT_BAND_"+str(band)+" "
radAdd="RADIANCE_ADD_BAND_"+str(band)+" "
radMax="RADIANCE_MAXIMUM_BAND_"+str(band)+" "
refMult="REFLECTANCE_MULT_BAND_"+str(band)+" "
refAdd="REFLECTANCE_ADD_BAND_"+str(band)+" "
refMax="REFLECTANCE_MAXIMUM_BAND_"+str(band)+" "

counter=0
if "_MTL.txt" in metafile:
    with open(metafile, "r") as mfile:
        for line in mfile:
            if counter == 6:
               break;
            
            if radMult in line:
                counter=counter+1
                words=line.split()
                radiance_mult=float(words[2])
            elif radAdd in line:
                counter=counter+1
                words=line.split()
                radiance_add=float(words[2])
            elif refMult in line:
                counter=counter+1
                words=line.split()
                reflectance_mult=float(words[2])
            elif refAdd in line:
                counter=counter+1
                words=line.split()
                reflectance_add=float(words[2])
            elif radMax in line:
                counter=counter+1
                words=line.split()
                radiance_max=float(words[2])
            elif refMax in line:
                counter=counter+1
                words=line.split()
                reflectance_max=float(words[2])
else:
    radiance_mult=-1
    radiance_add=-1
    radiance_max=-1
    reflectance_mult=-1
    reflectance_add=-1 
    reflectance_max=-1
    
