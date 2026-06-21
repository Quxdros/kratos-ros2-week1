import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/suraj/ros2_ws/src/turtle_controller/install/turtle_controller'
