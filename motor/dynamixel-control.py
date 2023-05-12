import dynamixel_sdk as dxl

# Control table addresses for Dynamixel AX-12A
ADDR_PRO_TORQUE_ENABLE = 24
ADDR_PRO_GOAL_POSITION = 30
ADDR_PRO_PRESENT_POSITION = 36

# Protocol version used
PROTOCOL_VERSION = 1

# Default settings
DXL_ID = 1
BAUDRATE = 1000000
DEVICENAME = '/dev/ttyUSB0'  # Modify it according to your environment

# Initialize the Dynamixel driver
port_handler = dxl.PortHandler(DEVICENAME)
packet_handler = dxl.PacketHandler(PROTOCOL_VERSION)

# Open the serial port
if port_handler.openPort():
    print("Succeeded to open the serial port!")
else:
    print("Failed to open the serial port!")
    exit(1)

# Set baudrate
if port_handler.setBaudRate(BAUDRATE):
    print("Succeeded to change the baudrate!")
else:
    print("Failed to change the baudrate!")
    exit(1)

# Enable torque
packet_handler.write1ByteTxRx(port_handler, DXL_ID, ADDR_PRO_TORQUE_ENABLE, 1)

# Set initial position
initial_position = 512  # Assuming initial position is at the center
packet_handler.write2ByteTxRx(port_handler, DXL_ID, ADDR_PRO_GOAL_POSITION, initial_position)

# Set goal position for rotation
goal_position = 512 + 80  # Rotate 80 degrees from the initial position
packet_handler.write2ByteTxRx(port_handler, DXL_ID, ADDR_PRO_GOAL_POSITION, goal_position)

# Wait until the motor reaches the goal position
while True:
    present_position = packet_handler.read2ByteTxRx(port_handler, DXL_ID, ADDR_PRO_PRESENT_POSITION)[0]
    if present_position >= goal_position:
        break

# Set goal position to return to initial position
packet_handler.write2ByteTxRx(port_handler, DXL_ID, ADDR_PRO_GOAL_POSITION, initial_position)

# Wait until the motor reaches the initial position
while True:
    present_position = packet_handler.read2ByteTxRx(port_handler, DXL_ID, ADDR_PRO_PRESENT_POSITION)[0]
    if present_position == initial_position:
        break

# Disable torque
packet_handler.write1ByteTxRx(port_handler, DXL_ID, ADDR_PRO_TORQUE_ENABLE, 0)

# Close the serial port
port_handler.closePort()
