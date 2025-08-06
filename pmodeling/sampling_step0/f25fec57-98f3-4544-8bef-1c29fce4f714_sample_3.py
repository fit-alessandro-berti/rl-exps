from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
SiteSurvey = Transition(label='Site Survey')
PermitFiling = Transition(label='Permit Filing')
StructureDesign = Transition(label='Structure Design')
SystemInstall = Transition(label='System Install')
HydroponicSetup = Transition(label='Hydroponic Setup')
ClimateConfig = Transition(label='Climate Config')
AIIntegration = Transition(label='AI Integration')
NutrientSourcing = Transition(label='Nutrient Sourcing')
WastePlanning = Transition(label='Waste Planning')
StaffTraining = Transition(label='Staff Training')
CropSeeding = Transition(label='Crop Seeding')
GrowthMonitoring = Transition(label='Growth Monitoring')
QualityTesting = Transition(label='Quality Testing')
HarvestScheduling = Transition(label='Harvest Scheduling')
DistributionPlan = Transition(label='Distribution Plan')
DataAnalysis = Transition(label='Data Analysis')

# Define the silent transitions
skip = SilentTransition()

# Define the exclusive choice nodes
xor1 = OperatorPOWL(operator=Operator.XOR, children=[HarvestScheduling, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[DistributionPlan, skip])

# Define the loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[QualityTesting, xor1])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[DataAnalysis, xor2])

# Define the partial order
root = StrictPartialOrder(nodes=[SiteSurvey, PermitFiling, StructureDesign, SystemInstall, HydroponicSetup, ClimateConfig, AIIntegration, NutrientSourcing, WastePlanning, StaffTraining, CropSeeding, GrowthMonitoring, loop1, loop2, xor2])
root.order.add_edge(SiteSurvey, PermitFiling)
root.order.add_edge(PermitFiling, StructureDesign)
root.order.add_edge(StructureDesign, SystemInstall)
root.order.add_edge(SystemInstall, HydroponicSetup)
root.order.add_edge(HydroponicSetup, ClimateConfig)
root.order.add_edge(ClimateConfig, AIIntegration)
root.order.add_edge(AIIntegration, NutrientSourcing)
root.order.add_edge(NutrientSourcing, WastePlanning)
root.order.add_edge(WastePlanning, StaffTraining)
root.order.add_edge(StaffTraining, CropSeeding)
root.order.add_edge(CropSeeding, GrowthMonitoring)
root.order.add_edge(GrowthMonitoring, loop1)
root.order.add_edge(loop1, QualityTesting)
root.order.add_edge(QualityTesting, xor1)
root.order.add_edge(xor1, HarvestScheduling)
root.order.add_edge(xor1, skip)
root.order.add_edge(HarvestScheduling, DistributionPlan)
root.order.add_edge(DistributionPlan, xor2)
root.order.add_edge(xor2, DataAnalysis)
root.order.add_edge(DataAnalysis, loop2)
root.order.add_edge(loop2, QualityTesting)
root.order.add_edge(QualityTesting, xor1)
root.order.add_edge(xor1, skip)
root.order.add_edge(skip, DistributionPlan)
root.order.add_edge(DistributionPlan, skip)
root.order.add_edge(skip, skip)

# Print the root
print(root)