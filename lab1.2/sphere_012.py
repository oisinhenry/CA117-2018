import sys
import math

def main():
    start_r = float(sys.argv[1])
    inc_r = float(sys.argv[2])
    end_r = float(sys.argv[3])

    h1 = 'Radius (m)'
    h4 = '-' * len(h1)
    h2 = 'Area (m^2)'
    h5 = '-' * len(h2)
    h3 = 'Volume (m^3)'
    h6 = '-' * len(h3)

    print('{:>s} {:>15s} {:>15s}'.format(h1, h2, h3))
    print('{:>s} {:>15s} {:>15s}'.format(h4, h5, h6))
    i = 0
    print('{:>10s} {:>15.2f} {:>15.2f}'.format(str(start_r), (4.0 * math.pi * start_r ** 2), (4 / 3 * math.pi * start_r ** 3)))
    
    # for i in range(1,int(end_r)):
    while start_r <= end_r - 0.5:
        start_r += inc_r
        print('{:>10s} {:>15.2f} {:>15.2f}'.format(str(start_r), (4.0 * math.pi * start_r ** 2), (4 / 3 * math.pi * start_r ** 3)))



if __name__ == '__main__':
    main()