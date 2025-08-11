import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
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

skip = SilentTransition()

# Define the partial order and its dependencies
partial_order = StrictPartialOrder(nodes=[
    SiteSurvey,
    DesignLayout,
    PermitsCheck,
    FoundationPrep,
    FrameAssembly,
    HydroSetup,
    ClimateSetup,
    SeedSelection,
    NutrientMix,
    SystemCalibration,
    PestControl,
    AutomationLink,
    StaffTraining,
    YieldTracking,
    DistributionPlan
])

partial_order.order.add_edge(SiteSurvey, DesignLayout)
partial_order.order.add_edge(DesignLayout, PermitsCheck)
partial_order.order.add_edge(PermitsCheck, FoundationPrep)
partial_order.order.add_edge(FoundationPrep, FrameAssembly)
partial_order.order.add_edge(FrameAssembly, HydroSetup)
partial_order.order.add_edge(HydroSetup, ClimateSetup)
partial_order.order.add_edge(ClimateSetup, SeedSelection)
partial_order.order.add_edge(SeedSelection, NutrientMix)
partial_order.order.add_edge(NutrientMix, SystemCalibration)
partial_order.order.add_edge(SystemCalibration, PestControl)
partial_order.order.add_edge(PestControl, AutomationLink)
partial_order.order.add_edge(AutomationLink, StaffTraining)
partial_order.order.add_edge(StaffTraining, YieldTracking)
partial_order.order.add_edge(YieldTracking, DistributionPlan)

# Set the root of the POWL model
root = partial_order