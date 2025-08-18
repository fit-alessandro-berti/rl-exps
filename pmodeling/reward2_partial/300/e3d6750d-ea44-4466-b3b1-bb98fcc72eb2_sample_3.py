import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
SiteSurvey = Transition(label='Site Survey')
StructuralCheck = Transition(label='Structural Check')
IoTSetup = Transition(label='IoT Setup')
CropSelection = Transition(label='Crop Selection')
HydroponicInstall = Transition(label='Hydroponic Install')
WaterRecycling = Transition(label='Water Recycling')
EnergyAudit = Transition(label='Energy Audit')
PlantScheduling = Transition(label='Plant Scheduling')
YieldMonitoring = Transition(label='Yield Monitoring')
RegulationReview = Transition(label='Regulation Review')
StaffTraining = Transition(label='Staff Training')
DataIntegration = Transition(label='Data Integration')
SupplySetup = Transition(label='Supply Setup')
QualityAudit = Transition(label='Quality Audit')
LogisticsPlan = Transition(label='Logistics Plan')

# Create a strict partial order for the workflow
root = StrictPartialOrder(nodes=[
    SiteSurvey, StructuralCheck, IoTSetup, CropSelection, HydroponicInstall, 
    WaterRecycling, EnergyAudit, PlantScheduling, YieldMonitoring, RegulationReview, 
    StaffTraining, DataIntegration, SupplySetup, QualityAudit, LogisticsPlan
])

# Define the order of execution for each activity
root.order.add_edge(SiteSurvey, StructuralCheck)
root.order.add_edge(StructuralCheck, IoTSetup)
root.order.add_edge(IoTSetup, CropSelection)
root.order.add_edge(CropSelection, HydroponicInstall)
root.order.add_edge(HydroponicInstall, WaterRecycling)
root.order.add_edge(WaterRecycling, EnergyAudit)
root.order.add_edge(EnergyAudit, PlantScheduling)
root.order.add_edge(PlantScheduling, YieldMonitoring)
root.order.add_edge(YieldMonitoring, RegulationReview)
root.order.add_edge(RegulationReview, StaffTraining)
root.order.add_edge(StaffTraining, DataIntegration)
root.order.add_edge(DataIntegration, SupplySetup)
root.order.add_edge(SupplySetup, QualityAudit)
root.order.add_edge(QualityAudit, LogisticsPlan)

# Print the root POWL model
print(root)