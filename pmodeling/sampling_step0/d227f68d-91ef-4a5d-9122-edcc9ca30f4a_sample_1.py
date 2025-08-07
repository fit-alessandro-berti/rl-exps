import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions for empty labels
skip = SilentTransition()

# Define partial order nodes
SiteSurveyLayout = OperatorPOWL(operator=Operator.XOR, children=[SiteSurvey, DesignLayout])
PermitCheckFoundation = OperatorPOWL(operator=Operator.XOR, children=[PermitsCheck, FoundationPrep])
FrameHydroSetup = OperatorPOWL(operator=Operator.XOR, children=[FrameAssembly, HydroSetup])
ClimateNutrientCalibration = OperatorPOWL(operator=Operator.XOR, children=[ClimateSetup, NutrientMix])
PestControlAutomation = OperatorPOWL(operator=Operator.XOR, children=[PestControl, AutomationLink])
StaffTrainingYieldTracking = OperatorPOWL(operator=Operator.XOR, children=[StaffTraining, YieldTracking])
DistributionPlan = OperatorPOWL(operator=Operator.XOR, children=[DistributionPlan, skip])

# Define loop nodes
FoundationPrepHydroSetup = OperatorPOWL(operator=Operator.LOOP, children=[FoundationPrep, HydroSetup])
ClimateNutrientCalibrationPestControl = OperatorPOWL(operator=Operator.LOOP, children=[ClimateSetup, NutrientMix, PestControl])
AutomationLinkStaffTraining = OperatorPOWL(operator=Operator.LOOP, children=[AutomationLink, StaffTraining])

# Define the root node
root = StrictPartialOrder(nodes=[SiteSurveyLayout, PermitCheckFoundation, FrameHydroSetup, ClimateNutrientCalibration, PestControlAutomation, StaffTrainingYieldTracking, DistributionPlan, FoundationPrepHydroSetup, ClimateNutrientCalibrationPestControl, AutomationLinkStaffTraining])
root.order.add_edge(SiteSurveyLayout, PermitCheckFoundation)
root.order.add_edge(PermitCheckFoundation, FoundationPrepHydroSetup)
root.order.add_edge(FoundationPrepHydroSetup, FrameHydroSetup)
root.order.add_edge(FrameHydroSetup, ClimateNutrientCalibration)
root.order.add_edge(ClimateNutrientCalibration, PestControlAutomation)
root.order.add_edge(PestControlAutomation, StaffTrainingYieldTracking)
root.order.add_edge(StaffTrainingYieldTracking, DistributionPlan)
root.order.add_edge(FoundationPrepHydroSetup, ClimateNutrientCalibrationPestControl)
root.order.add_edge(ClimateNutrientCalibrationPestControl, AutomationLinkStaffTraining)
root.order.add_edge(AutomationLinkStaffTraining, StaffTrainingYieldTracking)