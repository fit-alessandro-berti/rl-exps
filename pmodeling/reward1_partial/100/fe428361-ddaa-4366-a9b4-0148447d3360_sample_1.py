import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
ClientConsult = Transition(label='Client Consult')
PayloadAssess = Transition(label='Payload Assess')
DroneConfigure = Transition(label='Drone Configure')
RegulationCheck = Transition(label='Regulation Check')
FlightSimulate = Transition(label='Flight Simulate')
RouteOptimize = Transition(label='Route Optimize')
PackageSecure = Transition(label='Package Secure')
PreFlightInspect = Transition(label='Pre-Flight Inspect')
WeatherMonitor = Transition(label='Weather Monitor')
LaunchDrone = Transition(label='Launch Drone')
FlightTrack = Transition(label='Flight Track')
DeliveryConfirm = Transition(label='Delivery Confirm')
DataAnalyze = Transition(label='Data Analyze')
FeedbackCollect = Transition(label='Feedback Collect')
WarrantyRegister = Transition(label='Warranty Register')
IssueResolve = Transition(label='Issue Resolve')
PackageReturn = Transition(label='Package Return')

# Define the silent transitions
skip = SilentTransition()

# Define the exclusive choice for weather and technical failures
weather_or_issue = OperatorPOWL(operator=Operator.XOR, children=[WeatherMonitor, IssueResolve])

# Define the loop for pre-flight inspections
pre_flight_loop = OperatorPOWL(operator=Operator.LOOP, children=[PreFlightInspect])

# Define the partial order
root = StrictPartialOrder(nodes=[
    ClientConsult,
    PayloadAssess,
    DroneConfigure,
    RegulationCheck,
    FlightSimulate,
    RouteOptimize,
    PackageSecure,
    pre_flight_loop,
    weather_or_issue,
    LaunchDrone,
    FlightTrack,
    DeliveryConfirm,
    DataAnalyze,
    FeedbackCollect,
    WarrantyRegister,
    IssueResolve,
    PackageReturn
])

# Define the dependencies (partial order)
root.order.add_edge(ClientConsult, PayloadAssess)
root.order.add_edge(PayloadAssess, DroneConfigure)
root.order.add_edge(DroneConfigure, RegulationCheck)
root.order.add_edge(RegulationCheck, FlightSimulate)
root.order.add_edge(FlightSimulate, RouteOptimize)
root.order.add_edge(RouteOptimize, PackageSecure)
root.order.add_edge(PackageSecure, pre_flight_loop)
root.order.add_edge(pre_flight_loop, weather_or_issue)
root.order.add_edge(weather_or_issue, LaunchDrone)
root.order.add_edge(LaunchDrone, FlightTrack)
root.order.add_edge(FlightTrack, DeliveryConfirm)
root.order.add_edge(DeliveryConfirm, DataAnalyze)
root.order.add_edge(DataAnalyze, FeedbackCollect)
root.order.add_edge(FeedbackCollect, WarrantyRegister)
root.order.add_edge(WarrantyRegister, IssueResolve)
root.order.add_edge(IssueResolve, PackageReturn)

print(root)