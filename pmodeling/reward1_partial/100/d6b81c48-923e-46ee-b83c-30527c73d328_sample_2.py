import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
preflight = Transition(label='Preflight Check')
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

# Define silent transitions for certain activities
skip1 = SilentTransition()
skip2 = SilentTransition()
skip3 = SilentTransition()
skip4 = SilentTransition()

# Define exclusive choices and loops
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[preflight, sensor_calibrate, battery_test, route_update, firmware_patch, flight_launch, telemetry_monitor, anomaly_detect, collision_assess, data_upload, postflight_review, battery_optimize, damage_repair, compliance_report, performance_log, mission_debrief])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[skip1, skip2, skip3, skip4])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop1, loop2, xor1])
root.order.add_edge(loop1, xor1)