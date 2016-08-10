##metafile=file
##sun_elevation=output number
##earth_sun_distance=output number

sunElev="SUN_ELEVATION"
sunDist="EARTH_SUN_DISTANCE"

counter=0
if "_MTL.txt" in metafile:
    with open(metafile, "r") as mfile:
        for line in mfile:
            if counter == 2:
               break;
            
            if sunElev in line:
                counter=counter+1
                words=line.split()
                sun_elevation=float(words[2])
            elif sunDist in line:
                counter=counter+1
                words=line.split()
                earth_sun_distance=float(words[2])
else:
    sun_elevation=-1
    earth_sun_distance=-1
    
