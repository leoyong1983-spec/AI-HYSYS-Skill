# 1. Description
python automation package for aspen plus and aspen hysys.

# 2. Installation
## 'pip install ap-python'

# 3. How to use it?
## aspen plus
```python

    import ap_python.aspenplus as aplus
    import os

    # create an application
    ap = aplus.Application()
    # open file
    ap.open_file(os.path.join(os.getcwd(), 'pfdtut.bkp'))
    # set visible
    ap.visible = True
    # variable path: temperature of stream 1
    path = r'\Data\Streams\1\Input\TEMP\MIXED'
    # get node
    node = ap.find_node(path)
    # get node units
    print(f'units: {ap.get_units(node)}')
    # get variable value
    print(f'value: {ap.get_value(node)}')
    # get variable with unit
    print(f'value for unit R: {ap.get_value(node, "R")}')
    # set variable value
    ap.set_value(node, 500.0)
    print(f'value: {ap.get_value(node)}')
    # set variable value with unit
    ap.set_value(node, 500.0, 'R')
    print(f'value: {ap.get_value(node, "R")}')
    # run simulation
    ap.run()
    # save file
    ap.save()
    ap.saveas(os.path.join(os.getcwd(), 'pfdtut1.bkp'))
    # quit application
    ap.close()
```
## aspen hysys
```python

    import ap_python.aspenhysys as hysys
    import os

    # create an application
    hy = hysys.Application()
     # open file
    hy.open_file(os.path.join(os.getcwd(), 'Atmospheric Crude Tower.hsc'))
    # set visible
    hy.visible = True
    # variable moniker: temperature of stream 'Raw Crude'
    path = r'FlowSht.1/StreamObject.400(Raw Crude):Temperature.502.0'
    # get node
    node = hy.find_node(path)
    # get node units
    print(f'units: {hy.get_units(node)}')
    # get variable
    print(f'value: {hy.get_value(node)}')
    # get variable with unit
    print(f'value for unit R: {hy.get_value(node, "R")}')
    # set variable value
    hy.set_value(node, 500.0)
    print(f'value: {hy.get_value(node)}')
    # set variable value with unit
    hy.set_value(node, 500.0, 'R')
    print(f'value: {hy.get_value(node, "R")}')
    # save file
    hy.save()
    hy.saveas(os.path.join(os.getcwd(), 'Atmospheric Crude Tower1.hsc'))
    # quit application
    hy.close()
```
# 3. About variable path/moniker
## aspen plus: copy variable and paste it in variable explorer
![image](https://github.com/bshaoCN/ap-python/blob/master/ap-python/ap_python/tests/screenshots/aplus.1.png)
![image](https://github.com/bshaoCN/ap-python/blob/master/ap-python/ap_python/tests/screenshots/aplus.2.png)
## aspen hysys: copy variable and paste it in excel as link
![image](https://github.com/bshaoCN/ap-python/blob/master/ap-python/ap_python/tests/screenshots/hysys.1.png)
![image](https://github.com/bshaoCN/ap-python/blob/master/ap-python/ap_python/tests/screenshots/hysys.2.png)
![image](https://github.com/bshaoCN/ap-python/blob/master/ap-python/ap_python/tests/screenshots/hysys.3.png)