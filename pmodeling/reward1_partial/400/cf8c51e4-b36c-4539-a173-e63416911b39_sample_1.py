from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
SiteAnalysis = Transition(label='Site Analysis')
ZoningApproval = Transition(label='Zoning Approval')
StructuralCheck = Transition(label='Structural Check')
BuildingRetrofit = Transition(label='Building Retrofit')
HydroponicSetup = Transition(label='Hydroponic Setup')
ClimateControl = Transition(label='Climate Control')
NutrientDesign = Transition(label='Nutrient Design')
StaffHiring = Transition(label='Staff Hiring')
StaffTraining = Transition(label='Staff Training')
SoftwareInstall = Transition(label='Software Install')
SystemTesting = Transition(label='System Testing')
CropPlanting = Transition(label='Crop Planting')
GrowthMonitor = Transition(label='Growth Monitor')
PestControl = Transition(label='Pest Control')
HarvestPlan = Transition(label='Harvest Plan')

# Define the partial order
root = StrictPartialOrder(nodes=[
    SiteAnalysis,
    ZoningApproval,
    StructuralCheck,
    BuildingRetrofit,
    HydroponicSetup,
    ClimateControl,
    NutrientDesign,
    StaffHiring,
    StaffTraining,
    SoftwareInstall,
    SystemTesting,
    CropPlanting,
    GrowthMonitor,
    PestControl,
    HarvestPlan
])

# Define the dependencies
root.order.add_edge(SiteAnalysis, ZoningApproval)
root.order.add_edge(ZoningApproval, StructuralCheck)
root.order.add_edge(StructuralCheck, BuildingRetrofit)
root.order.add_edge(BuildingRetrofit, HydroponicSetup)
root.order.add_edge(HydroponicSetup, ClimateControl)
root.order.add_edge(ClimateControl, NutrientDesign)
root.order.add_edge(NutrientDesign, StaffHiring)
root.order.add_edge(StaffHiring, StaffTraining)
root.order.add_edge(StaffTraining, SoftwareInstall)
root.order.add_edge(SoftwareInstall, SystemTesting)
root.order.add_edge(SystemTesting, CropPlanting)
root.order.add_edge(CropPlanting, GrowthMonitor)
root.order.add_edge(GrowthMonitor, PestControl)
root.order.add_edge(PestControl, HarvestPlan)

# Print the POWL model
print(root)