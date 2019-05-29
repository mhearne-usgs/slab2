#!/usr/bin/env python

#stdlib imports

#third party imports
import numpy as np

#usgs imports
from neicmap.distance import sdist

def getEventsInCircle(lat,lon,radius,eventlist):
    """
    Select earthquakes from a list of events using a lat/lon center and a radius in km.
    @param lat: Latitude at center of circle.
    @param lon: Longitude at center of circle.
    @param radius: Radius of search in km.
    @param eventlist: List of event dictionaries, each containing (at least) keys lat,lon,depth,mag.
    @return: Filtered list of earthquake dictionaries.
    """
    elat = np.array([e['lat'] for e in eventlist])
    elon = np.array([e['lon'] for e in eventlist])
    d = sdist(lat,lon,elat,elon)/1000.0
    idx = (d <= radius).nonzero()[0]
    
    return (np.array(eventlist)[idx]).tolist()

def main():
    eventlist = [{'lat':33.1,'lon':-118.1,'depth':15.1,'mag':5.4},
                 {'lat':33.2,'lon':-118.2,'depth':15.2,'mag':5.2},
                 {'lat':33.3,'lon':-118.3,'depth':15.3,'mag':5.1},
                 ]
    lat = 31.5
    lon = -119.5
    radius = 225.0
    shortlist = getEventsInCircle(lat,lon,radius,eventlist)
    print 'All events within radius of %.1f km from %.4f,%.4f' % (radius,lat,lon)
    for event in shortlist:
        print event

if __name__ == '__main__':
    main() #do all the work in a main function so sub functions aren't polluted by variables in global namespace
    
                  
