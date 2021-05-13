# geoserver-plugin-detector

A python script for finding which plugins are installed in your local GeoServer

This script reads a text file containing the type, names and jar file of all the GeoServer plugins. This was generated by running 

    find . -path '*/target' -prune -o -name pom.xml -print | xargs -i sh -c 'grep -H artifactId {} |head -2 | tail -1'
    
in the `src` directory of the GeoServer project, and then hand editing it to produce 3 columns type name jar file (with out `.jar`). 