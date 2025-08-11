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

# Define the workflow
preflight_choice = OperatorPOWL(operator=Operator.XOR, children=[preflight_check, sensor_calibrate, battery_test])
route_update_loop = OperatorPOWL(operator=Operator.LOOP, children=[route_update])
flight_choice = OperatorPOWL(operator=Operator.XOR, children=[flight_launch, telemetry_monitor])
anomaly_detect_loop = OperatorPOWL(operator=Operator.LOOP, children=[anomaly_detect])
collision_assess_loop = OperatorPOWL(operator=Operator.LOOP, children=[collision_assess])
data_upload_choice = OperatorPOWL(operator=Operator.XOR, children=[data_upload, battery_optimize])
damage_repair_loop = OperatorPOWL(operator=Operator.LOOP, children=[damage_repair])
compliance_report_loop = OperatorPOWL(operator=Operator.LOOP, children=[compliance_report])
performance_log_loop = OperatorPOWL(operator=Operator.LOOP, children=[performance_log])
mission_debrief_loop = OperatorPOWL(operator=Operator.LOOP, children=[mission_debrief])

root = StrictPartialOrder(nodes=[preflight_choice, route_update_loop, flight_choice, anomaly_detect_loop, collision_assess_loop, data_upload_choice, damage_repair_loop, compliance_report_loop, performance_log_loop, mission_debrief_loop])
root.order.add_edge(preflight_choice, route_update_loop)
root.order.add_edge(route_update_loop, flight_choice)
root.order.add_edge(flight_choice, anomaly_detect_loop)
root.order.add_edge(anomaly_detect_loop, collision_assess_loop)
root.order.add_edge(collision_assess_loop, data_upload_choice)
root.order.add_edge(data_upload_choice, damage_repair_loop)
root.order.add_edge(damage_repair_loop, compliance_report_loop)
root.order.add_edge(compliance_report_loop, performance_log_loop)
root.order.add_edge(performance_log_loop, mission_debrief_loop)