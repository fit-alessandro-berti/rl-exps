from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities) with their labels
SiteSurvey = Transition(label='Site Survey')
StructuralCheck = Transition(label='Structural Check')
ModularInstall = Transition(label='Modular Install')
HydroponicSetup = Transition(label='Hydroponic Setup')
NutrientMix = Transition(label='Nutrient Mix')
SensorSetup = Transition(label='Sensor Setup')
AITraining = Transition(label='AI Training')
DataCapture = Transition(label='Data Capture')
MaintenancePlan = Transition(label='Maintenance Plan')
PestScan = Transition(label='Pest Scan')
GrowthMonitor = Transition(label='Growth Monitor')
HarvestSync = Transition(label='Harvest Sync')
QualityTest = Transition(label='Quality Test')
PackagePrep = Transition(label='Package Prep')
LogisticsPlan = Transition(label='Logistics Plan')

# Create the partial order
root = StrictPartialOrder(nodes=[
    SiteSurvey, StructuralCheck, ModularInstall, HydroponicSetup, NutrientMix, SensorSetup, AITraining,
    DataCapture, MaintenancePlan, PestScan, GrowthMonitor, HarvestSync, QualityTest, PackagePrep, LogisticsPlan
])

# Define the dependencies (partial order)
root.order.add_edge(SiteSurvey, StructuralCheck)
root.order.add_edge(StructuralCheck, ModularInstall)
root.order.add_edge(ModularInstall, HydroponicSetup)
root.order.add_edge(HydroponicSetup, NutrientMix)
root.order.add_edge(NutrientMix, SensorSetup)
root.order.add_edge(SensorSetup, AITraining)
root.order.add_edge(AITraining, DataCapture)
root.order.add_edge(DataCapture, MaintenancePlan)
root.order.add_edge(MaintenancePlan, PestScan)
root.order.add_edge(PestScan, GrowthMonitor)
root.order.add_edge(GrowthMonitor, HarvestSync)
root.order.add_edge(HarvestSync, QualityTest)
root.order.add_edge(QualityTest, PackagePrep)
root.order.add_edge(PackagePrep, LogisticsPlan)

print(root)