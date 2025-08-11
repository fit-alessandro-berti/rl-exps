import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
SiteSurvey = Transition(label='Site Survey')
LoadTest = Transition(label='Load Test')
ClimateStudy = Transition(label='Climate Study')
PermitCheck = Transition(label='Permit Check')
SystemDesign = Transition(label='System Design')
EquipmentBuy = Transition(label='Equipment Buy')
SensorSetup = Transition(label='Sensor Setup')
IrrigationFit = Transition(label='Irrigation Fit')
SolarInstall = Transition(label='Solar Install')
StaffTrain = Transition(label='Staff Train')
PilotPlant = Transition(label='Pilot Plant')
DataMonitor = Transition(label='Data Monitor')
CropHarvest = Transition(label='Crop Harvest')
MaintenancePlan = Transition(label='Maintenance Plan')
CommunityMeet = Transition(label='Community Meet')
skip = SilentTransition()

# Define the POWL model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[SiteSurvey, LoadTest, ClimateStudy, PermitCheck])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[SystemDesign, EquipmentBuy, SensorSetup, IrrigationFit, SolarInstall])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[StaffTrain, PilotPlant, DataMonitor, CropHarvest])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[MaintenancePlan, CommunityMeet])
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)