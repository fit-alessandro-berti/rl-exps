import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
preflight = Transition(label='Preflight Check')
sensor_calibrate = Transition(label='Sensor Calibrate')
battery_test = Transition(label='Battery Test')
firmware_patch = Transition(label='Firmware Patch')
flight_launch = Transition(label='Flight Launch')
telemetry_monitor = Transition(label='Telemetry Monitor')
anomaly_detect = Transition(label='Anomaly Detect')
collision_assess = Transition(label='Collision Assess')
damage_repair = Transition(label='Damage Repair')
data_upload = Transition(label='Data Upload')
postflight_review = Transition(label='Postflight Review')
battery_optimize = Transition(label='Battery Optimize')
performance_log = Transition(label='Performance Log')
compliance_report = Transition(label='Compliance Report')
mission_debrief = Transition(label='Mission Debrief')

# Define the anomaly detection branch: Collision Assess -> Damage Repair
anomaly_branch = StrictPartialOrder(nodes=[collision_assess, damage_repair])
anomaly_branch.order.add_edge(collision_assess, damage_repair)

# Define the loop: Anomaly Detect, then optionally execute anomaly_branch, and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[anomaly_detect, anomaly_branch])

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    preflight,
    sensor_calibrate,
    battery_test,
    firmware_patch,
    flight_launch,
    telemetry_monitor,
    loop,
    data_upload,
    postflight_review,
    battery_optimize,
    performance_log,
    compliance_report,
    mission_debrief
])

# Define the control-flow dependencies
root.order.add_edge(preflight, sensor_calibrate)
root.order.add_edge(sensor_calibrate, battery_test)
root.order.add_edge(battery_test, firmware_patch)
root.order.add_edge(firmware_patch, flight_launch)
root.order.add_edge(flight_launch, telemetry_monitor)
root.order.add_edge(telemetry_monitor, loop)
root.order.add_edge(loop, data_upload)
root.order.add_edge(data_upload, postflight_review)
root.order.add_edge(postflight_review, battery_optimize)
root.order.add_edge(battery_optimize, performance_log)
root.order.add_edge(performance_log, compliance_report)
root.order.add_edge(compliance_report, mission_debrief)