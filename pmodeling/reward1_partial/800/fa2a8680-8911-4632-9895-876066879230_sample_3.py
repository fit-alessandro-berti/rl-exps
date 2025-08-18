import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
ClientMeet = Transition(label='Client Meet')
RequirementGather = Transition(label='Requirement Gather')
ModuleDesign = Transition(label='Module Design')
SupplierVetting = Transition(label='Supplier Vetting')
ComponentOrder = Transition(label='Component Order')
PrototypeBuild = Transition(label='Prototype Build')
FieldTesting = Transition(label='Field Testing')
TestAnalysis = Transition(label='Test Analysis')
SoftwareSetup = Transition(label='Software Setup')
DataIntegration = Transition(label='Data Integration')
PilotTrain = Transition(label='Pilot Train')
ComplianceCheck = Transition(label='Compliance Check')
FleetDeploy = Transition(label='Fleet Deploy')
RemoteMonitor = Transition(label='Remote Monitor')
MaintenancePlan = Transition(label='Maintenance Plan')
PerformanceTune = Transition(label='Performance Tune')

# Define the relationships between activities
root = StrictPartialOrder(nodes=[
    ClientMeet,
    RequirementGather,
    ModuleDesign,
    SupplierVetting,
    ComponentOrder,
    PrototypeBuild,
    FieldTesting,
    TestAnalysis,
    SoftwareSetup,
    DataIntegration,
    PilotTrain,
    ComplianceCheck,
    FleetDeploy,
    RemoteMonitor,
    MaintenancePlan,
    PerformanceTune
])

# Define the order of activities
root.order.add_edge(ClientMeet, RequirementGather)
root.order.add_edge(RequirementGather, ModuleDesign)
root.order.add_edge(ModuleDesign, SupplierVetting)
root.order.add_edge(SupplierVetting, ComponentOrder)
root.order.add_edge(ComponentOrder, PrototypeBuild)
root.order.add_edge(PrototypeBuild, FieldTesting)
root.order.add_edge(FieldTesting, TestAnalysis)
root.order.add_edge(TestAnalysis, SoftwareSetup)
root.order.add_edge(SoftwareSetup, DataIntegration)
root.order.add_edge(DataIntegration, PilotTrain)
root.order.add_edge(PilotTrain, ComplianceCheck)
root.order.add_edge(ComplianceCheck, FleetDeploy)
root.order.add_edge(FleetDeploy, RemoteMonitor)
root.order.add_edge(RemoteMonitor, MaintenancePlan)
root.order.add_edge(MaintenancePlan, PerformanceTune)

print(root)