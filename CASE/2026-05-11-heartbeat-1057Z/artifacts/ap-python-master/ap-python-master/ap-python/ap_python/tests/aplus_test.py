import ap_python.aspenplus as aplus
import os

def main():
    # create an application
    ap = aplus.Application()
    # open file
    ap.open_file(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'pfdtut.bkp'))

    # set visible
    ap.visible = True

    # print(f'streams: {ap.print_streams()}')
    # print(f'blocks: {ap.print_blocks()}')

    # temperature of stream 1
    path = r'\Data\Streams\1\Input\TEMP\MIXED'
    node = ap.find_node(path)

    # get value with/without unit
    print(f'units: {ap.get_units(node)}')
    print(f'value: {ap.get_value(node)}')
    print(f'value for unit R: {ap.get_value(node, "R")}')

    # set value with/without unit
    ap.set_value(node, 500.0)
    print(f'value: {ap.get_value(node)}')
    ap.set_value(node, 500.0, 'R')
    print(f'value: {ap.get_value(node, "R")}')
    ap.run()
    # save file    
    # ap.save()
    ap.saveas(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'pfdtut1.bkp'))

    # quit application
    ap.close()


if __name__ == '__main__':
    main()
