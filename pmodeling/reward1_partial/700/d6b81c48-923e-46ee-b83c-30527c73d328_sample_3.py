import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define loops and choices
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[preflight_check, sensor_calibrate, battery_test, route_update])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[firmware_patch, flight_launch, telemetry_monitor, anomaly_detect])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[collision_assess, data_upload, postflight_review])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[battery_optimize, damage_repair, compliance_report])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[performance_log, mission_debrief])

# Define root with dependencies
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)

# Print the result
print(root)