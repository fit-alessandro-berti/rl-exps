import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define silent transitions (tau labels)
skip = SilentTransition()

# Define loop nodes
battery_loop = OperatorPOWL(operator=Operator.LOOP, children=[battery_test, battery_optimize])

# Define exclusive choice nodes (XOR)
maintenance_tasks = OperatorPOWL(operator=Operator.XOR, children=[route_update, firmware_patch, damage_repair])
flight_control = OperatorPOWL(operator=Operator.XOR, children=[flight_launch, telemetry_monitor, anomaly_detect, collision_assess, data_upload])
postflight_tasks = OperatorPOWL(operator=Operator.XOR, children=[postflight_review, battery_optimize, compliance_report, performance_log, mission_debrief])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    preflight_check,
    sensor_calibrate,
    battery_loop,
    maintenance_tasks,
    flight_control,
    postflight_tasks
])

# Define the dependencies (partial order)
root.order.add_edge(preflight_check, sensor_calibrate)
root.order.add_edge(sensor_calibrate, battery_loop)
root.order.add_edge(battery_loop, maintenance_tasks)
root.order.add_edge(maintenance_tasks, flight_control)
root.order.add_edge(flight_control, postflight_tasks)