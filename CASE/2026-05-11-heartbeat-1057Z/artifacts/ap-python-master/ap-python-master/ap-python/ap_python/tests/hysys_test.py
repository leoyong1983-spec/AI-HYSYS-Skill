import ap_python.aspenhysys as hysys
import os

def main():
    hy = hysys.Application()
    hy.open_file(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Atmospheric Crude Tower.hsc'))
    # set visible
    hy.visible = True

    # # temperature of stream 'Raw Crude'
    path = r'FlowSht.1/StreamObject.400(Raw Crude):Temperature.502.0'
    node = hy.find_node(path)
    print(f'units: {hy.get_units(node)}')
    print(f'value: {hy.get_value(node)}')
    print(f'value for unit R: {hy.get_value(node, "R")}')
    hy.set_value(node, 500.0)
    assert(hy.get_value(node)[0] == 500.0)
    print(f'value: {hy.get_value(node)}')
    hy.set_value(node, 500.0, 'R')
    assert(hy.get_value(node, 'R')[0] == 500.0)
    print(f'value: {hy.get_value(node, "R")}')
    hy.saveas(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Atmospheric Crude Tower1.hsc'))
    hy.close()


if __name__ == '__main__':
    main()
