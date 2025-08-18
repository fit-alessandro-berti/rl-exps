from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the process model
root = StrictPartialOrder(nodes=[SiteSurvey, EnergyPartner, PermitFiling, HydroUnit, AISetup, NutrientPlan, SystemInstall, CropTesting, DataAnalysis, CommunityMeet, YieldAdjust, CarbonAudit, LogisticsPlan, QualityCheck, ScaleReview])

# Add the dependencies
root.order.add_edge(SiteSurvey, EnergyPartner)
root.order.add_edge(SiteSurvey, PermitFiling)
root.order.add_edge(EnergyPartner, HydroUnit)
root.order.add_edge(PermitFiling, HydroUnit)
root.order.add_edge(HydroUnit, AISetup)
root.order.add_edge(AISetup, NutrientPlan)
root.order.add_edge(NutrientPlan, SystemInstall)
root.order.add_edge(SystemInstall, CropTesting)
root.order.add_edge(CropTesting, DataAnalysis)
root.order.add_edge(DataAnalysis, CommunityMeet)
root.order.add_edge(CommunityMeet, YieldAdjust)
root.order.add_edge(YieldAdjust, CarbonAudit)
root.order.add_edge(CarbonAudit, LogisticsPlan)
root.order.add_edge(LogisticsPlan, QualityCheck)
root.order.add_edge(QualityCheck, ScaleReview)

print(root)