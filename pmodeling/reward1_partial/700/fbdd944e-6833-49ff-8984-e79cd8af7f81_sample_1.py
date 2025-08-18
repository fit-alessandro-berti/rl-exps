import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
ClientOnboard = Transition(label='Client Onboard')
NeedsAssess = Transition(label='Needs Assess')
DroneConfig = Transition(label='Drone Config')
RouteProgram = Transition(label='Route Program')
ComplianceCheck = Transition(label='Compliance Check')
InsuranceVerify = Transition(label='Insurance Verify')
LeaseContract = Transition(label='Lease Contract')
FleetDeploy = Transition(label='Fleet Deploy')
MonitorSetup = Transition(label='Monitor Setup')
UsageTrack = Transition(label='Usage Track')
MaintenancePlan = Transition(label='Maintenance Plan')
IncidentManage = Transition(label='Incident Manage')
BillingProcess = Transition(label='Billing Process')
PerformanceReport = Transition(label='Performance Report')
ContractRenew = Transition(label='Contract Renew')
PriceAdjust = Transition(label='Price Adjust')
FeedbackCollect = Transition(label='Feedback Collect')

# Define the partial order
root = StrictPartialOrder(nodes=[
    ClientOnboard, NeedsAssess, DroneConfig, RouteProgram, ComplianceCheck, InsuranceVerify,
    LeaseContract, FleetDeploy, MonitorSetup, UsageTrack, MaintenancePlan, IncidentManage,
    BillingProcess, PerformanceReport, ContractRenew, PriceAdjust, FeedbackCollect
])
root.order.add_edge(ClientOnboard, NeedsAssess)
root.order.add_edge(NeedsAssess, DroneConfig)
root.order.add_edge(DroneConfig, RouteProgram)
root.order.add_edge(RouteProgram, ComplianceCheck)
root.order.add_edge(ComplianceCheck, InsuranceVerify)
root.order.add_edge(InsuranceVerify, LeaseContract)
root.order.add_edge(LeaseContract, FleetDeploy)
root.order.add_edge(FleetDeploy, MonitorSetup)
root.order.add_edge(MonitorSetup, UsageTrack)
root.order.add_edge(UsageTrack, MaintenancePlan)
root.order.add_edge(MaintenancePlan, IncidentManage)
root.order.add_edge(IncidentManage, BillingProcess)
root.order.add_edge(BillingProcess, PerformanceReport)
root.order.add_edge(PerformanceReport, ContractRenew)
root.order.add_edge(ContractRenew, PriceAdjust)
root.order.add_edge(PriceAdjust, FeedbackCollect)