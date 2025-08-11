import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
SiteSurvey = Transition(label='Site Survey')
PermitApproval = Transition(label='Permit Approval')
DesignLayout = Transition(label='Design Layout')
SystemProcure = Transition(label='System Procure')
NutrientPrep = Transition(label='Nutrient Prep')
StructureBuild = Transition(label='Structure Build')
SensorInstall = Transition(label='Sensor Install')
ClimateSetup = Transition(label='Climate Setup')
SeedSelect = Transition(label='Seed Select')
GerminateSeeds = Transition(label='Germinate Seeds')
MonitorGrowth = Transition(label='Monitor Growth')
DataAnalyze = Transition(label='Data Analyze')
PestControl = Transition(label='Pest Control')
HarvestCrop = Transition(label='Harvest Crop')
PackageGoods = Transition(label='Package Goods')
ShipProducts = Transition(label='Ship Products')

# Define the silent transitions
Skip = SilentTransition()

# Define the exclusive choice for seed selection and germination
XorSeedSelection = OperatorPOWL(operator=Operator.XOR, children=[SeedSelect, Skip])

# Define the loop for monitoring and data analysis
LoopMonitorData = OperatorPOWL(operator=Operator.LOOP, children=[MonitorGrowth, DataAnalyze])

# Define the root POWL model
root = StrictPartialOrder(nodes=[SiteSurvey, PermitApproval, DesignLayout, SystemProcure, NutrientPrep, StructureBuild, SensorInstall, ClimateSetup, XorSeedSelection, GerminateSeeds, LoopMonitorData, PestControl, HarvestCrop, PackageGoods, ShipProducts])
root.order.add_edge(SiteSurvey, PermitApproval)
root.order.add_edge(PermitApproval, DesignLayout)
root.order.add_edge(DesignLayout, SystemProcure)
root.order.add_edge(SystemProcure, NutrientPrep)
root.order.add_edge(NutrientPrep, StructureBuild)
root.order.add_edge(StructureBuild, SensorInstall)
root.order.add_edge(SensorInstall, ClimateSetup)
root.order.add_edge(ClimateSetup, XorSeedSelection)
root.order.add_edge(XorSeedSelection, GerminateSeeds)
root.order.add_edge(GerminateSeeds, LoopMonitorData)
root.order.add_edge(LoopMonitorData, PestControl)
root.order.add_edge(PestControl, HarvestCrop)
root.order.add_edge(HarvestCrop, PackageGoods)
root.order.add_edge(PackageGoods, ShipProducts)