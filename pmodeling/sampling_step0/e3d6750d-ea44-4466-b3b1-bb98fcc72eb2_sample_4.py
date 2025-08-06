import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the silent transitions
skip = SilentTransition()

# Define the operators
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[IoTSetup, CropSelection, HydroponicInstall, WaterRecycling, EnergyAudit, PlantScheduling, YieldMonitoring, RegulationReview, StaffTraining, DataIntegration, SupplySetup, QualityAudit, LogisticsPlan])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[SiteSurvey, StructuralCheck, loop1])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop2])
root.order.add_edge(loop2, loop1)

print(root)