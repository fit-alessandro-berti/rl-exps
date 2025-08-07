import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
preflight = Transition(label='Preflight Check')
sensor_cal = Transition(label='Sensor Calibrate')
battery_test = Transition(label='Battery Test')
firmware_patch = Transition(label='Firmware Patch')
flight_launch = Transition(label='Flight Launch')
telemetry_mon = Transition(label='Telemetry Monitor')
anomaly_detect = Transition(label='Anomaly Detect')
collision_assess = Transition(label='Collision Assess')
data_upload = Transition(label='Data Upload')
postflight_review = Transition(label='Postflight Review')
battery_optimize = Transition(label='Battery Optimize')
damage_repair = Transition(label='Damage Repair')
compliance_report = Transition(label='Compliance Report')
performance_log = Transition(label='Performance Log')
mission_debrief = Transition(label='Mission Debrief')

# Build the maintenance cycle: preflight -> calibration -> battery test -> firmware patch -> launch
cycle = StrictPartialOrder(nodes=[
    preflight, sensor_cal, battery_test, firmware_patch, flight_launch
])
cycle.order.add_edge(preflight, sensor_cal)
cycle.order.add_edge(sensor_cal, battery_test)
cycle.order.add_edge(battery_test, firmware_patch)
cycle.order.add_edge(firmware_patch, flight_launch)

# Loop for in-flight monitoring and data handling
# A: telemetry monitor, anomaly detect, collision assess
A = StrictPartialOrder(nodes=[
    telemetry_mon, anomaly_detect, collision_assess
])
A.order.add_edge(telemetry_mon, anomaly_detect)
A.order.add_edge(anomaly_detect, collision_assess)

# B: data upload, postflight review
B = StrictPartialOrder(nodes=[data_upload, postflight_review])
B.order.add_edge(data_upload, postflight_review)

# LOOP operator: do A, then either exit or do B then A again
flight_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[A, B]
)

# Assemble the overall process
root = StrictPartialOrder(nodes=[
    cycle,
    flight_loop,
    battery_optimize,
    damage_repair,
    compliance_report,
    performance_log,
    mission_debrief
])

# Sequence the cycle and flight loop
root.order.add_edge(cycle, flight_loop)

# Parallelize postflight tasks
root.order.add_edge(flight_loop, battery_optimize)
root.order.add_edge(flight_loop, damage_repair)

# Concurrency of compliance and performance
root.order.add_edge(flight_loop, compliance_report)
root.order.add_edge(flight_loop, performance_log)

# Finally, mission debrief happens after all loops complete
root.order.add_edge(battery_optimize, mission_debrief)
root.order.add_edge(damage_repair, mission_debrief)
root.order.add_edge(compliance_report, mission_debrief)
root.order.add_edge(performance_log, mission_debrief)