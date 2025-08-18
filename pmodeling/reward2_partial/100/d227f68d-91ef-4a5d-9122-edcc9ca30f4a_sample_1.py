from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
SiteSurvey = Transition(label='Site Survey')
DesignLayout = Transition(label='Design Layout')
PermitsCheck = Transition(label='Permits Check')
FoundationPrep = Transition(label='Foundation Prep')
FrameAssembly = Transition(label='Frame Assembly')
HydroSetup = Transition(label='Hydro Setup')
ClimateSetup = Transition(label='Climate Setup')
SeedSelection = Transition(label='Seed Selection')
NutrientMix = Transition(label='Nutrient Mix')
SystemCalibration = Transition(label='System Calibration')
PestControl = Transition(label='Pest Control')
AutomationLink = Transition(label='Automation Link')
StaffTraining = Transition(label='Staff Training')
YieldTracking = Transition(label='Yield Tracking')
DistributionPlan = Transition(label='Distribution Plan')

# Define the partial order
root = StrictPartialOrder(nodes=[SiteSurvey, DesignLayout, PermitsCheck, FoundationPrep, FrameAssembly, HydroSetup, ClimateSetup, SeedSelection, NutrientMix, SystemCalibration, PestControl, AutomationLink, StaffTraining, YieldTracking, DistributionPlan])

# Define the order
root.order.add_edge(SiteSurvey, DesignLayout)
root.order.add_edge(DesignLayout, PermitsCheck)
root.order.add_edge(PermitsCheck, FoundationPrep)
root.order.add_edge(FoundationPrep, FrameAssembly)
root.order.add_edge(FrameAssembly, HydroSetup)
root.order.add_edge(HydroSetup, ClimateSetup)
root.order.add_edge(ClimateSetup, SeedSelection)
root.order.add_edge(SeedSelection, NutrientMix)
root.order.add_edge(NutrientMix, SystemCalibration)
root.order.add_edge(SystemCalibration, PestControl)
root.order.add_edge(PestControl, AutomationLink)
root.order.add_edge(AutomationLink, StaffTraining)
root.order.add_edge(StaffTraining, YieldTracking)
root.order.add_edge(YieldTracking, DistributionPlan)

print(root)