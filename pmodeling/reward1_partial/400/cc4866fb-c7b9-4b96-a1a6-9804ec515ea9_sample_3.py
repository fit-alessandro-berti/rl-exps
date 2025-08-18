import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
SiteSurvey = Transition(label='Site Survey')
DesignPlanning = Transition(label='Design Planning')
PermitFiling = Transition(label='Permit Filing')
StructuralReinforce = Transition(label='Structural Reinforce')
HydroponicSetup = Transition(label='Hydroponic Setup')
SensorInstall = Transition(label='Sensor Install')
EnergyAudit = Transition(label='Energy Audit')
CropSelection = Transition(label='Crop Selection')
NutrientMix = Transition(label='Nutrient Mix')
WasteProcess = Transition(label='Waste Process')
ClimateControl = Transition(label='Climate Control')
StaffTraining = Transition(label='Staff Training')
MarketStudy = Transition(label='Market Study')
CommunityMeet = Transition(label='Community Meet')
LaunchTrial = Transition(label='Launch Trial')
DataMonitor = Transition(label='Data Monitor')

# Define the dependencies between activities
root = StrictPartialOrder(nodes=[
    SiteSurvey,
    DesignPlanning,
    PermitFiling,
    StructuralReinforce,
    HydroponicSetup,
    SensorInstall,
    EnergyAudit,
    CropSelection,
    NutrientMix,
    WasteProcess,
    ClimateControl,
    StaffTraining,
    MarketStudy,
    CommunityMeet,
    LaunchTrial,
    DataMonitor
])

root.order.add_edge(SiteSurvey, DesignPlanning)
root.order.add_edge(DesignPlanning, PermitFiling)
root.order.add_edge(PermitFiling, StructuralReinforce)
root.order.add_edge(StructuralReinforce, HydroponicSetup)
root.order.add_edge(HydroponicSetup, SensorInstall)
root.order.add_edge(SensorInstall, EnergyAudit)
root.order.add_edge(EnergyAudit, CropSelection)
root.order.add_edge(CropSelection, NutrientMix)
root.order.add_edge(NutrientMix, WasteProcess)
root.order.add_edge(WasteProcess, ClimateControl)
root.order.add_edge(ClimateControl, StaffTraining)
root.order.add_edge(StaffTraining, MarketStudy)
root.order.add_edge(MarketStudy, CommunityMeet)
root.order.add_edge(CommunityMeet, LaunchTrial)
root.order.add_edge(LaunchTrial, DataMonitor)

# Print the root POWL model
print(root)