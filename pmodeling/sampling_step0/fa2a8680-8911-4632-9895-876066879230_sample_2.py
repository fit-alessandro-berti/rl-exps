import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
Skip = SilentTransition()

# Define partial orders
# Initial stages
initialStages = StrictPartialOrder(nodes=[ClientMeet, RequirementGather])
initialStages.order.add_edge(ClientMeet, RequirementGather)

# Module design and component sourcing
moduleDesign = StrictPartialOrder(nodes=[ModuleDesign, SupplierVetting, ComponentOrder])
moduleDesign.order.add_edge(ModuleDesign, SupplierVetting)
moduleDesign.order.add_edge(SupplierVetting, ComponentOrder)

# Prototype assembly and rigorous field testing
prototypeAssembly = StrictPartialOrder(nodes=[PrototypeBuild, FieldTesting])
prototypeAssembly.order.add_edge(PrototypeBuild, FieldTesting)

# Software integration and pilot training
softwareIntegration = StrictPartialOrder(nodes=[SoftwareSetup, DataIntegration, PilotTrain])
softwareIntegration.order.add_edge(SoftwareSetup, DataIntegration)
softwareIntegration.order.add_edge(DataIntegration, PilotTrain)

# Compliance check and fleet deploy
fleetDeployment = StrictPartialOrder(nodes=[ComplianceCheck, FleetDeploy])
fleetDeployment.order.add_edge(ComplianceCheck, FleetDeploy)

# Post-deployment stages
postDeployment = StrictPartialOrder(nodes=[RemoteMonitor, MaintenancePlan, PerformanceTune])
postDeployment.order.add_edge(RemoteMonitor, MaintenancePlan)
postDeployment.order.add_edge(MaintenancePlan, PerformanceTune)

# Connect the stages with exclusive choice
root = StrictPartialOrder(nodes=[initialStages, moduleDesign, prototypeAssembly, softwareIntegration, fleetDeployment, postDeployment])
root.order.add_edge(initialStages, moduleDesign)
root.order.add_edge(moduleDesign, prototypeAssembly)
root.order.add_edge(prototypeAssembly, softwareIntegration)
root.order.add_edge(softwareIntegration, fleetDeployment)
root.order.add_edge(fleetDeployment, postDeployment)

# Print the POWL model
print(root)