import matplotlib.pyplot as plt
from ezdxf.entities.line import Line
from ezdxf.filemanagement import readfile
from ezdxf.units import unit_name

def plot_lines(lines: list[Line]):
    for line in lines:
        xs = [line.dxf.start[0], line.dxf.end[0]]
        ys = [line.dxf.start[1], line.dxf.end[1]]
        plt.plot(xs, ys)
    plt.show()

def main():
    file = readfile('part1.dxf')
    # lines_dashed = file.query('LINE[linetype=="Dashed"]')
    lines_dashed = file.query('LINE')

    print(unit_name(file.header['$INSUNITS']))

    plot_lines([line for line in lines_dashed]) # type: ignore

if __name__ == '__main__':
    main()
