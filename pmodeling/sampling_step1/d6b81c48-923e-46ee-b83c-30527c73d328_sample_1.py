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

# Define silent transitions
skip = SilentTransition()

# Define the POWL model
loop_preflight = OperatorPOWL(operator=Operator.LOOP, children=[preflight_check])
loop_sensor = OperatorPOWL(operator=Operator.LOOP, children=[sensor_calibrate])
loop_battery = OperatorPOWL(operator=Operator.LOOP, children=[battery_test])
loop_route = OperatorPOWL(operator=Operator.LOOP, children=[route_update])
loop_firmware = OperatorPOWL(operator=Operator.LOOP, children=[firmware_patch])
loop_launch = OperatorPOWL(operator=Operator.LOOP, children=[flight_launch])
loop_monitor = OperatorPOWL(operator=Operator.LOOP, children=[telemetry_monitor])
loop_detect = OperatorPOWL(operator=Operator.LOOP, children=[anomaly_detect])
loop_assess = OperatorPOWL(operator=Operator.LOOP, children=[collision_assess])
loop_upload = OperatorPOWL(operator=Operator.LOOP, children=[data_upload])
loop_review = OperatorPOWL(operator=Operator.LOOP, children=[postflight_review])
loop_optimize = OperatorPOWL(operator=Operator.LOOP, children=[battery_optimize])
loop_repair = OperatorPOWL(operator=Operator.LOOP, children=[damage_repair])
loop_report = OperatorPOWL(operator=Operator.LOOP, children=[compliance_report])
loop_log = OperatorPOWL(operator=Operator.LOOP, children=[performance_log])
loop_debrief = OperatorPOWL(operator=Operator.LOOP, children=[mission_debrief])

# Construct the root POWL model
root = StrictPartialOrder(nodes=[loop_preflight, loop_sensor, loop_battery, loop_route, loop_firmware, loop_launch, loop_monitor, loop_detect, loop_assess, loop_upload, loop_review, loop_optimize, loop_repair, loop_report, loop_log, loop_debrief])
root.order.add_edge(loop_preflight, loop_sensor)
root.order.add_edge(loop_sensor, loop_battery)
root.order.add_edge(loop_battery, loop_route)
root.order.add_edge(loop_route, loop_firmware)
root.order.add_edge(loop_firmware, loop_launch)
root.order.add_edge(loop_launch, loop_monitor)
root.order.add_edge(loop_monitor, loop_detect)
root.order.add_edge(loop_detect, loop_assess)
root.order.add_edge(loop_assess, loop_upload)
root.order.add_edge(loop_upload, loop_review)
root.order.add_edge(loop_review, loop_optimize)
root.order.add_edge(loop_optimize, loop_repair)
root.order.add_edge(loop_repair, loop_report)
root.order.add_edge(loop_report, loop_log)
root.order.add_edge(loop_log, loop_debrief)

print(root)