import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[SiteAssess, PlanLayout, InstallRacks, MixNutrients, CalibrateSensors, SetupLighting, ConfigureClimate, SelectSeeds, MonitorGerminate, ApplyBiocontrols, MaintainSystems])
xor = OperatorPOWL(operator=Operator.XOR, children=[AnalyzeData, HarvestCrops, QualityCheck, PackageProduce, DistributeGoods])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)