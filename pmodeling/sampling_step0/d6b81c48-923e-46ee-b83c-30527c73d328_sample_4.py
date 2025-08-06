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

# Define the silent transition for the loop
skip = SilentTransition()

# Define the loop for the in-flight operations
loop_in_flight = OperatorPOWL(operator=Operator.LOOP, children=[telemetry_monitor, anomaly_detect, collision_assess, data_upload])

# Define the exclusive choice for pre-flight and post-flight operations
xor_pre_postflight = OperatorPOWL(operator=Operator.XOR, children=[preflight_check, postflight_review])

# Define the exclusive choice for in-flight and post-flight operations
xor_in_postflight = OperatorPOWL(operator=Operator.XOR, children=[loop_in_flight, mission_debrief])

# Define the loop for the battery maintenance operations
loop_battery = OperatorPOWL(operator=Operator.LOOP, children=[battery_test, battery_optimize])

# Define the exclusive choice for in-flight and post-flight operations
xor_battery = OperatorPOWL(operator=Operator.XOR, children=[loop_battery, compliance_report])

# Define the exclusive choice for in-flight, post-flight, and battery operations
xor_all = OperatorPOWL(operator=Operator.XOR, children=[xor_in_postflight, xor_battery])

# Define the loop for the full maintenance cycle
root = StrictPartialOrder(nodes=[xor_all])
root.order.add_edge(xor_all, xor_pre_postflight)
root.order.add_edge(xor_all, xor_in_postflight)
root.order.add_edge(xor_all, xor_battery)
root.order.add_edge(xor_in_postflight, loop_in_flight)
root.order.add_edge(xor_battery, loop_battery)