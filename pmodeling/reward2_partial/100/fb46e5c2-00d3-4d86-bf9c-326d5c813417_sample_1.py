import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

SiteAnalysis = Transition(label='Site Analysis')
ImpactReview = Transition(label='Impact Review')
ModularDesign = Transition(label='Modular Design')
SystemIntegration = Transition(label='System Integration')
ClimateSetup = Transition(label='Climate Setup')
NutrientMix = Transition(label='Nutrient Mix')
LightConfig = Transition(label='Light Config')
StaffTraining = Transition(label='Staff Training')
PestMonitor = Transition(label='Pest Monitor')
DroneDeploy = Transition(label='Drone Deploy')
HealthScan = Transition(label='Health Scan')
DataLogging = Transition(label='Data Logging')
SupplySync = Transition(label='Supply Sync')
MaintenancePlan = Transition(label='Maintenance Plan')
WasteManage = Transition(label='Waste Manage')

root = StrictPartialOrder(nodes=[SiteAnalysis, ImpactReview, ModularDesign, SystemIntegration, ClimateSetup, NutrientMix, LightConfig, StaffTraining, PestMonitor, DroneDeploy, HealthScan, DataLogging, SupplySync, MaintenancePlan, WasteManage])

# Define dependencies between activities
root.order.add_edge(SiteAnalysis, ImpactReview)
root.order.add_edge(ImpactReview, ModularDesign)
root.order.add_edge(ModularDesign, SystemIntegration)
root.order.add_edge(SystemIntegration, ClimateSetup)
root.order.add_edge(ClimateSetup, NutrientMix)
root.order.add_edge(NutrientMix, LightConfig)
root.order.add_edge(LightConfig, StaffTraining)
root.order.add_edge(StaffTraining, PestMonitor)
root.order.add_edge(PestMonitor, DroneDeploy)
root.order.add_edge(DroneDeploy, HealthScan)
root.order.add_edge(HealthScan, DataLogging)
root.order.add_edge(DataLogging, SupplySync)
root.order.add_edge(SupplySync, MaintenancePlan)
root.order.add_edge(MaintenancePlan, WasteManage)