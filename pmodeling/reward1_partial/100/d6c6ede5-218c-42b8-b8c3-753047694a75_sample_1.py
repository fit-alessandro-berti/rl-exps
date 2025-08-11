import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) for the POWL model
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

# Define the partial order structure
root = StrictPartialOrder(nodes=[
    SiteSurvey,
    LoadTest,
    ClimateStudy,
    PermitCheck,
    SystemDesign,
    EquipmentBuy,
    SensorSetup,
    IrrigationFit,
    SolarInstall,
    StaffTrain,
    PilotPlant,
    DataMonitor,
    CropHarvest,
    MaintenancePlan,
    CommunityMeet
])

# Define the dependencies between the transitions
root.order.add_edge(SiteSurvey, LoadTest)
root.order.add_edge(SiteSurvey, ClimateStudy)
root.order.add_edge(SiteSurvey, PermitCheck)
root.order.add_edge(LoadTest, SystemDesign)
root.order.add_edge(ClimateStudy, SystemDesign)
root.order.add_edge(PermitCheck, SystemDesign)
root.order.add_edge(SystemDesign, EquipmentBuy)
root.order.add_edge(SystemDesign, SensorSetup)
root.order.add_edge(SystemDesign, IrrigationFit)
root.order.add_edge(SystemDesign, SolarInstall)
root.order.add_edge(EquipmentBuy, StaffTrain)
root.order.add_edge(SensorSetup, StaffTrain)
root.order.add_edge(IrrigationFit, StaffTrain)
root.order.add_edge(SolarInstall, StaffTrain)
root.order.add_edge(StaffTrain, PilotPlant)
root.order.add_edge(PilotPlant, DataMonitor)
root.order.add_edge(PilotPlant, CropHarvest)
root.order.add_edge(PilotPlant, MaintenancePlan)
root.order.add_edge(PilotPlant, CommunityMeet)

print(root)