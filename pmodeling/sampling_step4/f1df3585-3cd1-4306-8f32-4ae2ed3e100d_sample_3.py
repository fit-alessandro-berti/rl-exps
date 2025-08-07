from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the partial order model
root = StrictPartialOrder(nodes=[SiteAssess, PlanLayout, InstallRacks, MixNutrients, CalibrateSensors, SetupLighting, ConfigureClimate, SelectSeeds, MonitorGerminate, ApplyBiocontrols, MaintainSystems, AnalyzeData, HarvestCrops, QualityCheck, PackageProduce, DistributeGoods])

# Define the order of execution
root.order.add_edge(SiteAssess, PlanLayout)
root.order.add_edge(PlanLayout, InstallRacks)
root.order.add_edge(InstallRacks, MixNutrients)
root.order.add_edge(MixNutrients, CalibrateSensors)
root.order.add_edge(CalibrateSensors, SetupLighting)
root.order.add_edge(SetupLighting, ConfigureClimate)
root.order.add_edge(ConfigureClimate, SelectSeeds)
root.order.add_edge(SelectSeeds, MonitorGerminate)
root.order.add_edge(MonitorGerminate, ApplyBiocontrols)
root.order.add_edge(ApplyBiocontrols, MaintainSystems)
root.order.add_edge(MaintainSystems, AnalyzeData)
root.order.add_edge(AnalyzeData, HarvestCrops)
root.order.add_edge(HarvestCrops, QualityCheck)
root.order.add_edge(QualityCheck, PackageProduce)
root.order.add_edge(PackageProduce, DistributeGoods)

print(root)