import sys.argv

if sys.argv[1] == '--help' or sys.argv[1] == '-h' or len(sys.argv) > 2 or len(sys.argv) < 2:
    print('--CircuitDoom LIBDOOM--')
    print('Last updated: 11:23AM (EST) 1/29/2021')
    print('make_lvl_images <iwad>')
    print('Creates level images')
else:
    print('--CircuitDoom LIBDOOM--')
    raise NotImplementedError()
