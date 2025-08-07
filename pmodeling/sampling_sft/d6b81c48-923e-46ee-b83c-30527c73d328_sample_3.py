import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL Transitions
preflight      = Transition(label='Preflight Check')
sensor_cal     = Transition(label='Sensor Calibrate')
battery_test   = Transition(label='Battery Test')
route_update   = Transition(label='Route Update')
firmware_patch = Transition(label='Firmware Patch')
flight_launch  = Transition(label='Flight Launch')
telemetry_mon  = Transition(label='Telemetry Monitor')
anomaly_detect = Transition(label='Anomaly Detect')
collision_assess = Transition(label='Collision Assess')
data_upload    = Transition(label='Data Upload')
postflight_rev = Transition(label='Postflight Review')
battery_opt    = Transition(label='Battery Optimize')
damage_repair  = Transition(label='Damage Repair')
compliance_rep = Transition(label='Compliance Report')
performance_log = Transition(label='Performance Log')
mission_debrief = Transition(label='Mission Debrief')

# Build the main flight sequence as a partial order
flight_seq = StrictPartialOrder(nodes=[
    preflight, sensor_cal, battery_test, route_update,
    firmware_patch, flight_launch, telemetry_mon,
    anomaly_detect, collision_assess, data_upload,
    postflight_rev, battery_opt, damage_repair,
    compliance_rep, performance_log, mission_debrief
])

# Define the control-flow dependencies
flight_seq.order.add_edge(preflight, sensor_cal)
flight_seq.order.add_edge(sensor_cal, battery_test)
flight_seq.order.add_edge(battery_test, route_update)
flight_seq.order.add_edge(route_update, firmware_patch)
flight_seq.order.add_edge(firmware_patch, flight_launch)
flight_seq.order.add_edge(flight_launch, telemetry_mon)
flight_seq.order.add_edge(telemetry_mon, anomaly_detect)
flight_seq.order.add_edge(anomaly_detect, collision_assess)
flight_seq.order.add_edge(collision_assess, data_upload)
flight_seq.order.add_edge(data_upload, postflight_rev)
flight_seq.order.add_edge(postflight_rev, battery_opt)
flight_seq.order.add_edge(battery_opt, damage_repair)
flight_seq.order.add_edge(damage_repair, compliance_rep)
flight_seq.order.add_edge(compliance_rep, performance_log)
flight_seq.order.add_edge(performance_log, mission_debrief)

# Define the loop: after each mission, do a partial review
loop_body = flight_seq
skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, skip])

# Build the overall root process
root = StrictPartialOrder(nodes=[
    loop, compliance_rep, mission_debrief
])
root.order.add_edge(loop, compliance_rep)
root.order.add_edge(compliance_rep, mission_debrief)

print(root)