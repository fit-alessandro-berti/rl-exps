import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define silent transitions
skip = SilentTransition()

# Define sub-processes
subProcess1 = StrictPartialOrder(nodes=[SiteAnalysis, StructureCheck, ClimateSetup, HydroponicsInstall])
subProcess2 = StrictPartialOrder(nodes=[NutrientMix, SeedSelect, LightSchedule, IrrigationPlan, HealthMonitor, PestControl])
subProcess3 = StrictPartialOrder(nodes=[RoboticHarvest, CleanPackaging, DistributionPlan, DataCollection, CycleFeedback])

# Define partial order
root = StrictPartialOrder(nodes=[subProcess1, subProcess2, subProcess3])
root.order.add_edge(subProcess1, subProcess2)
root.order.add_edge(subProcess2, subProcess3)