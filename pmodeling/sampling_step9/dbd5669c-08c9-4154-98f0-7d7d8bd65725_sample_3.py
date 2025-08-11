import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
SiteSurvey = Transition(label='Site Survey')
DesignLayout = Transition(label='Design Layout')
MaterialSourcing = Transition(label='Material Sourcing')
UnitAssembly = Transition(label='Unit Assembly')
SystemWiring = Transition(label='System Wiring')
SensorInstall = Transition(label='Sensor Install')
WaterTesting = Transition(label='Water Testing')
NutrientMix = Transition(label='Nutrient Mix')
SeedSelection = Transition(label='Seed Selection')
PlantingSetup = Transition(label='Planting Setup')
ClimateControl = Transition(label='Climate Control')
PestManagement = Transition(label='Pest Management')
DataCalibration = Transition(label='Data Calibration')
YieldAnalysis = Transition(label='Yield Analysis')
CommunityMeet = Transition(label='Community Meet')
ComplianceCheck = Transition(label='Compliance Check')
ExpansionPlan = Transition(label='Expansion Plan')

# Define silent transitions (no action)
skip = SilentTransition()

# Define the process structure
# Site Survey -> Design Layout -> Material Sourcing -> Unit Assembly -> System Wiring -> Sensor Install -> Water Testing -> Nutrient Mix -> Seed Selection -> Planting Setup -> Climate Control -> Pest Management -> Data Calibration -> Yield Analysis -> Community Meet -> Compliance Check -> Expansion Plan

# Create the POWL model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[SiteSurvey, DesignLayout, MaterialSourcing, UnitAssembly, SystemWiring, SensorInstall, WaterTesting, NutrientMix, SeedSelection, PlantingSetup, ClimateControl, PestManagement, DataCalibration, YieldAnalysis, CommunityMeet, ComplianceCheck, ExpansionPlan])

# Define the partial order
root = StrictPartialOrder(nodes=[loop1])
root.order.add_edge(loop1, skip)  # Add a dependency from loop1 to skip

# Print the result
print(root)