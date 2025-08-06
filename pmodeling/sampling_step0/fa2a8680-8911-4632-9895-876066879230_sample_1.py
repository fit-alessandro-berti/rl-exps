import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

loop = OperatorPOWL(operator=Operator.LOOP, children=[ModuleDesign, SupplierVetting, ComponentOrder, PrototypeBuild, FieldTesting, TestAnalysis, SoftwareSetup, DataIntegration, PilotTrain, ComplianceCheck])
xor = OperatorPOWL(operator=Operator.XOR, children=[FleetDeploy, MaintenancePlan, PerformanceTune])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)