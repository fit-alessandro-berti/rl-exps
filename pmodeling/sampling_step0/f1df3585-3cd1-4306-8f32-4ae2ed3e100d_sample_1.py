import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
SiteAssess = Transition(label='Site Assess')
PlanLayout = Transition(label='Plan Layout')
InstallRacks = Transition(label='Install Racks')
MixNutrients = Transition(label='Mix Nutrients')
CalibrateSensors = Transition(label='Calibrate Sensors')
SetupLighting = Transition(label='Setup Lighting')
ConfigureClimate = Transition(label='Configure Climate')
SelectSeeds = Transition(label='Select Seeds')
MonitorGerminate = Transition(label='Monitor Germinate')
ApplyBiocontrols = Transition(label='Apply Bio-controls')
MaintainSystems = Transition(label='Maintain Systems')
AnalyzeData = Transition(label='Analyze Data')
HarvestCrops = Transition(label='Harvest Crops')
QualityCheck = Transition(label='Quality Check')
PackageProduce = Transition(label='Package Produce')
DistributeGoods = Transition(label='Distribute Goods')

# Define silent transitions
skip = SilentTransition()

# Define loops
SiteLayoutLoop = OperatorPOWL(operator=Operator.LOOP, children=[SiteAssess, PlanLayout, InstallRacks, MixNutrients, CalibrateSensors, SetupLighting, ConfigureClimate])
SelectSeedLoop = OperatorPOWL(operator=Operator.LOOP, children=[SelectSeeds, MonitorGerminate, ApplyBiocontrols])
MaintainSystemLoop = OperatorPOWL(operator=Operator.LOOP, children=[MaintainSystems, AnalyzeData])
HarvestLoop = OperatorPOWL(operator=Operator.LOOP, children=[HarvestCrops, QualityCheck, PackageProduce, DistributeGoods])

# Define XOR nodes
SelectSeedXOR = OperatorPOWL(operator=Operator.XOR, children=[SelectSeedLoop, skip])
SiteLayoutXOR = OperatorPOWL(operator=Operator.XOR, children=[SiteLayoutLoop, SelectSeedXOR])

# Define root
root = StrictPartialOrder(nodes=[SiteLayoutXOR, HarvestLoop])
root.order.add_edge(SiteLayoutLoop, SelectSeedLoop)
root.order.add_edge(SelectSeedLoop, SelectSeedXOR)
root.order.add_edge(SiteLayoutLoop, SiteLayoutXOR)
root.order.add_edge(SelectSeedXOR, HarvestLoop)
root.order.add_edge(HarvestLoop, HarvestLoop)