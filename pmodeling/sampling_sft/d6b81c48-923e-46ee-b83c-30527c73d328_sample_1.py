import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
preflight_check     = Transition(label='Preflight Check')
sensor_calibrate    = Transition(label='Sensor Calibrate')
battery_test        = Transition(label='Battery Test')
route_update        = Transition(label='Route Update')
firmware_patch      = Transition(label='Firmware Patch')
flight_launch       = Transition(label='Flight Launch')
telemetry_monitor   = Transition(label='Telemetry Monitor')
anomaly_detect      = Transition(label='Anomaly Detect')
collision_assess    = Transition(label='Collision Assess')
damage_repair       = Transition(label='Damage Repair')
data_upload         = Transition(label='Data Upload')
postflight_review   = Transition(label='Postflight Review')
battery_optimize    = Transition(label='Battery Optimize')
compliance_report   = Transition(label='Compliance Report')
performance_log     = Transition(label='Performance Log')
mission_debrief     = Transition(label='Mission Debrief')

# Loop for in-flight anomaly detection: do anomaly detect, then optionally assess collision and repair damage, then re-detect
in_flight_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[anomaly_detect,
              X(collision_assess, damage_repair)
              ]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    preflight_check,
    sensor_calibrate,
    battery_test,
    route_update,
    firmware_patch,
    flight_launch,
    telemetry_monitor,
    in_flight_loop,
    data_upload,
    postflight_review,
    battery_optimize,
    compliance_report,
    performance_log,
    mission_debrief
])

# Define the control-flow dependencies
root.order.add_edge(preflight_check, sensor_calibrate)
root.order.add_edge(preflight_check, battery_test)
root.order.add_edge(sensor_calibrate, route_update)
root.order.add_edge(battery_test, route_update)
root.order.add_edge(route_update, firmware_patch)
root.order.add_edge(firmware_patch, flight_launch)
root.order.add_edge(flight_launch, telemetry_monitor)
root.order.add_edge(telemetry_monitor, in_flight_loop)
root.order.add_edge(in_flight_loop, data_upload)
root.order.add_edge(data_upload, postflight_review)
root.order.add_edge(postflight_review, battery_optimize)
root.order.add_edge(battery_optimize, compliance_report)
root.order.add_edge(compliance_report, performance_log)
root.order.add_edge(performance_log, mission_debrief)