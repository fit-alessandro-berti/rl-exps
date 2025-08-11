import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

PreflightCheck = Transition(label='Preflight Check')
SensorCalibrate = Transition(label='Sensor Calibrate')
BatteryTest = Transition(label='Battery Test')
RouteUpdate = Transition(label='Route Update')
FirmwarePatch = Transition(label='Firmware Patch')
FlightLaunch = Transition(label='Flight Launch')
TelemetryMonitor = Transition(label='Telemetry Monitor')
AnomalyDetect = Transition(label='Anomaly Detect')
CollisionAssess = Transition(label='Collision Assess')
DataUpload = Transition(label='Data Upload')
PostflightReview = Transition(label='Postflight Review')
BatteryOptimize = Transition(label='Battery Optimize')
DamageRepair = Transition(label='Damage Repair')
ComplianceReport = Transition(label='Compliance Report')
PerformanceLog = Transition(label='Performance Log')
MissionDebrief = Transition(label='Mission Debrief')

skip = SilentTransition()
loop_preflight = OperatorPOWL(operator=Operator.LOOP, children=[PreflightCheck, SensorCalibrate, BatteryTest, RouteUpdate])
loop_flight = OperatorPOWL(operator=Operator.LOOP, children=[FlightLaunch, TelemetryMonitor, AnomalyDetect, CollisionAssess, DataUpload, PostflightReview, BatteryOptimize, DamageRepair])
loop_compliance = OperatorPOWL(operator=Operator.LOOP, children=[ComplianceReport, PerformanceLog, MissionDebrief])

xor_flight = OperatorPOWL(operator=Operator.XOR, children=[loop_flight, skip])
xor_compliance = OperatorPOWL(operator=Operator.XOR, children=[loop_compliance, skip])

root = StrictPartialOrder(nodes=[loop_preflight, xor_flight, xor_compliance])
root.order.add_edge(loop_preflight, xor_flight)
root.order.add_edge(loop_preflight, xor_compliance)
root.order.add_edge(xor_flight, xor_compliance)

print(root)