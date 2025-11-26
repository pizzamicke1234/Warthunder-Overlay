from WarThunder import telemetry
from WarThunder import mapinfo
from pprint import pprint

telem = telemetry.TelemInterface()

def get_map_info():
    while not telem.get_telemetry():
            pass
    map_name = telem.map_info.grid_info['name']
    map_size = telem.map_info.grid_info['size_km']
    return map_name, map_size

    
def find_basic_telemetry():
    print('------------------------------------------------------')
    print('Basic Telemetry:')
    pprint(telem.basic_telemetry)
    print('')
    
def find_comments():
    print('------------------------------------------------------')
    print('Comments:')
    comments = telem.get_comments()
    
    if comments:
        pprint(comments)
    else:
        print('\tNone')
    print('')
    
def find_events():
    print('------------------------------------------------------')
    print('Events:')
    events = telem.get_events()
    
    if events:
        pprint(events)
    else:
        print('\tNone')
    print('')

def find_bomb_points(friendly=True):
    while not telem.get_telemetry():
            pass
    if friendly:
        print('Friendly Bomb Points:')
        bomb_points = [obj for obj in telem.map_info.defend_points() if obj.friendly]
    else:
        print('Enemy Bomb Points:')
        bomb_points = [obj for obj in telem.map_info.bombing_points() if not obj.friendly]
    
    if bomb_points:
        for bomb_point in bomb_points:
            print('\tBombing Point: {}'.format(bomb_point.position_ll))
    else:
        print('\tNone')
    print(' ')

def get_bomb_points(friendly):
    while not telem.get_telemetry():
            pass
    points = []
    if friendly:
        bomb_points = [obj for obj in telem.map_info.defend_points() if obj.friendly]
    else:
        bomb_points = [obj for obj in telem.map_info.bombing_points() if not obj.friendly]
    
    if bomb_points:
        for bomb_point in bomb_points:
            points.append(bomb_point.position_ll)
        return points
    else:
        return None

def get_airfields(friendly):
    runways = []
    num = 0

    if friendly:
        airfields = [obj for obj in telem.map_info.airfields() if obj.friendly]
    else:
        airfields = [obj for obj in telem.map_info.airfields() if not obj.friendly]
    
    if airfields:
        for airfield in airfields:
            num += 1
            e = airfield.east_end_ll
            s = airfield.south_end_ll
            heading = airfield.runway_dir
            length = mapinfo.coord_dist(*airfield.east_end_ll, *airfield.south_end_ll)
            runways.append(num, e, s, heading, length)

        return runways
            
    else:
        return None

def get_planes(friendly):
    if friendly:
        planes = [obj for obj in telem.map_info.planes() if obj.friendly]
    else:
        planes = [obj for obj in telem.map_info.planes() if not obj.friendly]
    
    if planes:
        return planes
    else:
        return None
    

def find_tanks(friendly=True):
    if friendly:
        print('Friendly Tanks:')
        tanks = [obj for obj in telem.map_info.tanks() if obj.friendly]
    else:
        print('Enemy Tanks:')
        tanks = [obj for obj in telem.map_info.tanks() if not obj.friendly]
    
    if tanks:
        for tank in tanks:
            print('\tPosition:\t{}'.format(tank.position_ll))
            print('\tHeading:\t{}'.format(tank.hdg))
            print('')
    else:
        print('\tNone')
    print('')

def find_AAAs(friendly=True):
    if friendly:
        print('Friendly AAAs:')
        AAAs = [obj for obj in telem.map_info.AAAs() if obj.friendly]
    else:
        print('Enemy AAAs:')
        AAAs = [obj for obj in telem.map_info.AAAs() if not obj.friendly]
    
    if AAAs:
        for AAA in AAAs:
            print('\tPosition:\t{}'.format(AAA.position_ll))
    else:
        print('\tNone')
    print('')
