from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model
SiteAnalysis = Transition(label='Site Analysis')
StructureCheck = Transition(label='Structure Check')
ClimateSetup = Transition(label='Climate Setup')
HydroponicsInstall = Transition(label='Hydroponics Install')
NutrientMix = Transition(label='Nutrient Mix')
SeedSelect = Transition(label='Seed Select')
LightSchedule = Transition(label='Light Schedule')
IrrigationPlan = Transition(label='Irrigation Plan')
HealthMonitor = Transition(label='Health Monitor')
PestControl = Transition(label='Pest Control')
RoboticHarvest = Transition(label='Robotic Harvest')
CleanPackaging = Transition(label='Clean Packaging')
DistributionPlan = Transition(label='Distribution Plan')
DataCollection = Transition(label='Data Collection')
CycleFeedback = Transition(label='Cycle Feedback')

# Define the partial order
root = StrictPartialOrder(nodes=[SiteAnalysis, StructureCheck, ClimateSetup, HydroponicsInstall, NutrientMix, SeedSelect, LightSchedule, IrrigationPlan, HealthMonitor, PestControl, RoboticHarvest, CleanPackaging, DistributionPlan, DataCollection, CycleFeedback])

# Define the order of execution
root.order.add_edge(SiteAnalysis, StructureCheck)
root.order.add_edge(StructureCheck, ClimateSetup)
root.order.add_edge(ClimateSetup, HydroponicsInstall)
root.order.add_edge(HydroponicsInstall, NutrientMix)
root.order.add_edge(NutrientMix, SeedSelect)
root.order.add_edge(SeedSelect, LightSchedule)
root.order.add_edge(LightSchedule, IrrigationPlan)
root.order.add_edge(IrrigationPlan, HealthMonitor)
root.order.add_edge(HealthMonitor, PestControl)
root.order.add_edge(PestControl, RoboticHarvest)
root.order.add_edge(RoboticHarvest, CleanPackaging)
root.order.add_edge(CleanPackaging, DistributionPlan)
root.order.add_edge(DistributionPlan, DataCollection)
root.order.add_edge(DataCollection, CycleFeedback)