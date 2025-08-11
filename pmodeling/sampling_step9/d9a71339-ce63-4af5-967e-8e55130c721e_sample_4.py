import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
SiteSurvey = Transition(label='Site Survey')
StructuralCheck = Transition(label='Structural Check')
ModularInstall = Transition(label='Modular Install')
HydroponicSetup = Transition(label='Hydroponic Setup')
NutrientMix = Transition(label='Nutrient Mix')
SensorSetup = Transition(label='Sensor Setup')
AITraining = Transition(label='AI Training')
DataCapture = Transition(label='Data Capture')
MaintenancePlan = Transition(label='Maintenance Plan')
PestScan = Transition(label='Pest Scan')
GrowthMonitor = Transition(label='Growth Monitor')
HarvestSync = Transition(label='Harvest Sync')
QualityTest = Transition(label='Quality Test')
PackagePrep = Transition(label='Package Prep')
LogisticsPlan = Transition(label='Logistics Plan')

# Define silent transitions
skip = SilentTransition()

# Define the loop node for data acquisition and maintenance planning
loop = OperatorPOWL(operator=Operator.LOOP, children=[DataCapture, MaintenancePlan])

# Define the exclusive choice for pest scan and growth monitor
xor = OperatorPOWL(operator=Operator.XOR, children=[PestScan, GrowthMonitor])

# Define the partial order
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Add dependencies between nodes
root.order.add_edge(SiteSurvey, StructuralCheck)
root.order.add_edge(StructuralCheck, ModularInstall)
root.order.add_edge(ModularInstall, HydroponicSetup)
root.order.add_edge(HydroponicSetup, NutrientMix)
root.order.add_edge(NutrientMix, SensorSetup)
root.order.add_edge(SensorSetup, AITraining)
root.order.add_edge(AITraining, DataCapture)
root.order.add_edge(DataCapture, MaintenancePlan)
root.order.add_edge(MaintenancePlan, PestScan)
root.order.add_edge(PestScan, GrowthMonitor)
root.order.add_edge(GrowthMonitor, HarvestSync)
root.order.add_edge(HarvestSync, QualityTest)
root.order.add_edge(QualityTest, PackagePrep)
root.order.add_edge(PackagePrep, LogisticsPlan)