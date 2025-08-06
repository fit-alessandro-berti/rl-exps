import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the loop nodes
preflight_loop = OperatorPOWL(operator=Operator.LOOP, children=[preflight_check, sensor_calibrate, battery_test, route_update])
firmware_loop = OperatorPOWL(operator=Operator.LOOP, children=[firmware_patch, flight_launch])
anomaly_loop = OperatorPOWL(operator=Operator.LOOP, children=[telemetry_monitor, anomaly_detect, collision_assess, data_upload])
postflight_loop = OperatorPOWL(operator=Operator.LOOP, children=[postflight_review, battery_optimize, damage_repair, compliance_report, performance_log])
mission_loop = OperatorPOWL(operator=Operator.LOOP, children=[mission_debrief])

# Define the exclusive choice nodes
firmware_choice = OperatorPOWL(operator=Operator.XOR, children=[firmware_loop, preflight_loop])
anomaly_choice = OperatorPOWL(operator=Operator.XOR, children=[anomaly_loop, preflight_loop])
postflight_choice = OperatorPOWL(operator=Operator.XOR, children=[postflight_loop, preflight_loop])
mission_choice = OperatorPOWL(operator=Operator.XOR, children=[mission_loop, preflight_loop])

# Define the partial order
root = StrictPartialOrder(nodes=[firmware_choice, anomaly_choice, postflight_choice, mission_choice])
root.order.add_edge(firmware_choice, anomaly_choice)
root.order.add_edge(anomaly_choice, postflight_choice)
root.order.add_edge(postflight_choice, mission_choice)

# Print the root
print(root)