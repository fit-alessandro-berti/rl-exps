import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
SiteSurvey = Transition(label='Site Survey')
EnergyPartner = Transition(label='Energy Partner')
PermitFiling = Transition(label='Permit Filing')
HydroUnit = Transition(label='Hydro Unit')
AISetup = Transition(label='AI Setup')
NutrientPlan = Transition(label='Nutrient Plan')
SystemInstall = Transition(label='System Install')
CropTesting = Transition(label='Crop Testing')
DataAnalysis = Transition(label='Data Analysis')
CommunityMeet = Transition(label='Community Meet')
YieldAdjust = Transition(label='Yield Adjust')
CarbonAudit = Transition(label='Carbon Audit')
LogisticsPlan = Transition(label='Logistics Plan')
QualityCheck = Transition(label='Quality Check')
ScaleReview = Transition(label='Scale Review')

# Define transitions for sub-processes
SubProcess1 = StrictPartialOrder(nodes=[SiteSurvey, EnergyPartner, PermitFiling], order={(SiteSurvey, EnergyPartner), (EnergyPartner, PermitFiling)})
SubProcess2 = StrictPartialOrder(nodes=[HydroUnit, AISetup, NutrientPlan, SystemInstall], order={(HydroUnit, AISetup), (AISetup, NutrientPlan), (NutrientPlan, SystemInstall)})
SubProcess3 = StrictPartialOrder(nodes=[CropTesting, DataAnalysis, CommunityMeet, YieldAdjust], order={(CropTesting, DataAnalysis), (DataAnalysis, CommunityMeet), (CommunityMeet, YieldAdjust)})
SubProcess4 = StrictPartialOrder(nodes=[CarbonAudit, LogisticsPlan, QualityCheck, ScaleReview], order={(CarbonAudit, LogisticsPlan), (LogisticsPlan, QualityCheck), (QualityCheck, ScaleReview)})

# Define the root process as an exclusive choice of the sub-processes
root = OperatorPOWL(operator=Operator.XOR, children=[SubProcess1, SubProcess2, SubProcess3, SubProcess4])