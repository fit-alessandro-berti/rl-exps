import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the loop for battery optimization and damage repair
battery_optimize_loop = OperatorPOWL(operator=Operator.LOOP, children=[battery_optimize, damage_repair])

# Define the exclusive choice for postflight review and compliance report
postflight_review_xor = OperatorPOWL(operator=Operator.XOR, children=[postflight_review, compliance_report])

# Define the root POWL model
root = StrictPartialOrder(nodes=[preflight_check, sensor_calibrate, battery_test, route_update, firmware_patch, flight_launch, telemetry_monitor, anomaly_detect, collision_assess, data_upload, battery_optimize_loop, postflight_review_xor, damage_repair, compliance_report, performance_log, mission_debrief])

# Add edges to represent dependencies between activities
root.order.add_edge(preflight_check, sensor_calibrate)
root.order.add_edge(sensor_calibrate, battery_test)
root.order.add_edge(battery_test, route_update)
root.order.add_edge(route_update, firmware_patch)
root.order.add_edge(firmware_patch, flight_launch)
root.order.add_edge(flight_launch, telemetry_monitor)
root.order.add_edge(telemetry_monitor, anomaly_detect)
root.order.add_edge(anomaly_detect, collision_assess)
root.order.add_edge(collision_assess, data_upload)
root.order.add_edge(data_upload, battery_optimize_loop)
root.order.add_edge(battery_optimize_loop, postflight_review_xor)
root.order.add_edge(postflight_review_xor, damage_repair)
root.order.add_edge(postflight_review_xor, compliance_report)
root.order.add_edge(damage_repair, performance_log)
root.order.add_edge(performance_log, mission_debrief)