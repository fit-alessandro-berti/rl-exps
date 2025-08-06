import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
preflight_check = Transition(label='Preflight Check')
sensor_calibrate = Transition(label='Sensor Calibrate')
battery_test = Transition(label='Battery Test')
route_update = Transition(label='Route Update')
firmware_patch = Transition(label='Firmware Patch')
flight_launch = Transition(label='Flight Launch')
telemetry_monitor = Transition(label='Telemetry Monitor')
anomaly_detect = Transition(label='Anomaly Detect')
collision_assess = Transition(label='Collision Assess')
data_upload = Transition(label='Data Upload')
postflight_review = Transition(label='Postflight Review')
battery_optimize = Transition(label='Battery Optimize')
damage_repair = Transition(label='Damage Repair')
compliance_report = Transition(label='Compliance Report')
performance_log = Transition(label='Performance Log')
mission_debrief = Transition(label='Mission Debrief')

# Define the loop node
loop = OperatorPOWL(operator=Operator.LOOP, children=[
    preflight_check,
    sensor_calibrate,
    battery_test,
    route_update,
    firmware_patch,
    flight_launch,
    telemetry_monitor,
    anomaly_detect,
    collision_assess,
    data_upload,
    postflight_review,
    battery_optimize,
    damage_repair,
    compliance_report,
    performance_log,
    mission_debrief
])

# Define the exclusive choice node
xor = OperatorPOWL(operator=Operator.XOR, children=[loop, SilentTransition()])

# Define the root node
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Print the POWL model
print(root)