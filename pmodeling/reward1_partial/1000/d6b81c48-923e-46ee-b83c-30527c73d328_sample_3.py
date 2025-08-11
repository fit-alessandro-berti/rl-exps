import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
preflight = Transition(label='Preflight Check')
calibrate = Transition(label='Sensor Calibrate')
battery_test = Transition(label='Battery Test')
route_update = Transition(label='Route Update')
firmware_patch = Transition(label='Firmware Patch')
launch = Transition(label='Flight Launch')
monitor = Transition(label='Telemetry Monitor')
anomaly_detect = Transition(label='Anomaly Detect')
collision_assess = Transition(label='Collision Assess')
data_upload = Transition(label='Data Upload')
postflight = Transition(label='Postflight Review')
optimize = Transition(label='Battery Optimize')
damage_repair = Transition(label='Damage Repair')
compliance = Transition(label='Compliance Report')
log = Transition(label='Performance Log')
debrief = Transition(label='Mission Debrief')

# Define the partial order
root = StrictPartialOrder(nodes=[preflight, calibrate, battery_test, route_update, firmware_patch, launch, monitor, anomaly_detect, collision_assess, data_upload, postflight, optimize, damage_repair, compliance, log, debrief])

# Define the dependencies
root.order.add_edge(preflight, calibrate)
root.order.add_edge(preflight, battery_test)
root.order.add_edge(calibrate, route_update)
root.order.add_edge(route_update, firmware_patch)
root.order.add_edge(firmware_patch, launch)
root.order.add_edge(launch, monitor)
root.order.add_edge(monitor, anomaly_detect)
root.order.add_edge(anomaly_detect, collision_assess)
root.order.add_edge(collision_assess, data_upload)
root.order.add_edge(data_upload, postflight)
root.order.add_edge(postflight, optimize)
root.order.add_edge(optimize, damage_repair)
root.order.add_edge(damage_repair, compliance)
root.order.add_edge(compliance, log)
root.order.add_edge(log, debrief)

# Print the root POWL model
print(root)