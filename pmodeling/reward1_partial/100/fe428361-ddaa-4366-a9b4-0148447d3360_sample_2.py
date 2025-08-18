from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model
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

# Define the partial order structure
root = StrictPartialOrder(nodes=[
    ClientConsult,
    PayloadAssess,
    DroneConfigure,
    RegulationCheck,
    FlightSimulate,
    RouteOptimize,
    PackageSecure,
    PreFlightInspect,
    WeatherMonitor,
    LaunchDrone,
    FlightTrack,
    DeliveryConfirm,
    DataAnalyze,
    FeedbackCollect,
    WarrantyRegister,
    IssueResolve,
    PackageReturn
])

# Define the order relationships between the nodes
root.order.add_edge(ClientConsult, PayloadAssess)
root.order.add_edge(PayloadAssess, DroneConfigure)
root.order.add_edge(DroneConfigure, RegulationCheck)
root.order.add_edge(RegulationCheck, FlightSimulate)
root.order.add_edge(FlightSimulate, RouteOptimize)
root.order.add_edge(RouteOptimize, PackageSecure)
root.order.add_edge(PackageSecure, PreFlightInspect)
root.order.add_edge(PreFlightInspect, WeatherMonitor)
root.order.add_edge(WeatherMonitor, LaunchDrone)
root.order.add_edge(LaunchDrone, FlightTrack)
root.order.add_edge(FlightTrack, DeliveryConfirm)
root.order.add_edge(DeliveryConfirm, DataAnalyze)
root.order.add_edge(DataAnalyze, FeedbackCollect)
root.order.add_edge(FeedbackCollect, WarrantyRegister)
root.order.add_edge(WarrantyRegister, IssueResolve)
root.order.add_edge(IssueResolve, PackageReturn)