import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities)
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
preflight_loop = OperatorPOWL(operator=Operator.LOOP, children=[preflight_check, sensor_calibrate, battery_test])
route_update_loop = OperatorPOWL(operator=Operator.LOOP, children=[route_update, firmware_patch])
flight_loop = OperatorPOWL(operator=Operator.LOOP, children=[flight_launch, telemetry_monitor, anomaly_detect, collision_assess, data_upload, postflight_review])
battery_optimize_loop = OperatorPOWL(operator=Operator.LOOP, children=[battery_optimize, damage_repair])
compliance_loop = OperatorPOWL(operator=Operator.LOOP, children=[compliance_report, performance_log, mission_debrief])

# Define the partial order
root = StrictPartialOrder(nodes=[preflight_loop, route_update_loop, flight_loop, battery_optimize_loop, compliance_loop])
root.order.add_edge(preflight_loop, route_update_loop)
root.order.add_edge(route_update_loop, flight_loop)
root.order.add_edge(flight_loop, battery_optimize_loop)
root.order.add_edge(battery_optimize_loop, compliance_loop)

print(root)