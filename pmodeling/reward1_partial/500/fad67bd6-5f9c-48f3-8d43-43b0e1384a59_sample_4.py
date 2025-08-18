import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) for the process
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    RegulatoryCheck,
    PathDesign,
    WeatherSync,
    TrafficAlign,
    PackageSecure,
    CustomerAlert,
    DroneAssemble,
    FlightTest,
    DataMonitor,
    SafetyAudit,
    EmergencyPlan,
    MaintenancePlan,
    BatteryCycle,
    RouteUpdate,
    PerformanceReview,
    ImpactStudy,
    ComplianceReview
])

# Define the dependencies (partial order)
root.order.add_edge(RegulatoryCheck, PathDesign)
root.order.add_edge(PathDesign, WeatherSync)
root.order.add_edge(WeatherSync, TrafficAlign)
root.order.add_edge(TrafficAlign, PackageSecure)
root.order.add_edge(PackageSecure, CustomerAlert)
root.order.add_edge(CustomerAlert, DroneAssemble)
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

# Print the final result
print(root)