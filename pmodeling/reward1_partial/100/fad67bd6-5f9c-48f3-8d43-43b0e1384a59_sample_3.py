import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
RegulatoryCheck = Transition(label='Regulatory Check')
PathDesign = Transition(label='Path Design')
WeatherSync = Transition(label='Weather Sync')
TrafficAlign = Transition(label='Traffic Align')
PackageSecure = Transition(label='Package Secure')
CustomerAlert = Transition(label='Customer Alert')
DroneAssemble = Transition(label='Drone Assemble')
FlightTest = Transition(label='Flight Test')
DataMonitor = Transition(label='Data Monitor')
SafetyAudit = Transition(label='Safety Audit')
EmergencyPlan = Transition(label='Emergency Plan')
MaintenancePlan = Transition(label='Maintenance Plan')
BatteryCycle = Transition(label='Battery Cycle')
RouteUpdate = Transition(label='Route Update')
PerformanceReview = Transition(label='Performance Review')
ImpactStudy = Transition(label='Impact Study')
ComplianceReview = Transition(label='Compliance Review')

# Define the exclusive choice (XOR) between Regulatory Check and Path Design
xor = OperatorPOWL(operator=Operator.XOR, children=[RegulatoryCheck, PathDesign])

# Define the loop node for Weather Sync, Traffic Align, and Package Secure
loop = OperatorPOWL(operator=Operator.LOOP, children=[WeatherSync, TrafficAlign, PackageSecure])

# Define the strict partial order
root = StrictPartialOrder(nodes=[xor, loop, DroneAssemble, FlightTest, DataMonitor, SafetyAudit, EmergencyPlan, MaintenancePlan, BatteryCycle, RouteUpdate, PerformanceReview, ImpactStudy, ComplianceReview])
root.order.add_edge(xor, loop)
root.order.add_edge(loop, DroneAssemble)
root.order.add_edge(DroneAssemble, FlightTest)
root.order.add_edge(FlightTest, DataMonitor)
root.order.add_edge(DataMonitor, SafetyAudit)
root.order.add_edge(SafetyAudit, EmergencyPlan)
root.order.add_edge(EmergencyPlan, MaintenancePlan)
root.order.add_edge(MaintenancePlan, BatteryCycle)
root.order.add_edge(BatteryCycle, RouteUpdate)
root.order.add_edge(RouteUpdate, PerformanceReview)
root.order.add_edge(PerformanceReview, ImpactStudy)
root.order.add_edge(ImpactStudy, ComplianceReview)