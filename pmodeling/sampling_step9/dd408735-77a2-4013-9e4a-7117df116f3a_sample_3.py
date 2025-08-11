import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
SiteAssess = Transition(label='Site Assess')
StructureCheck = Transition(label='Structure Check')
SoilTest = Transition(label='Soil Test')
ClimateEval = Transition(label='Climate Eval')
PermitObtain = Transition(label='Permit Obtain')
DesignLayout = Transition(label='Design Layout')
SeedSourcing = Transition(label='Seed Sourcing')
IrrigationSet = Transition(label='Irrigation Set')
NutrientMix = Transition(label='Nutrient Mix')
PestControl = Transition(label='Pest Control')
SensorInstall = Transition(label='Sensor Install')
StaffTrain = Transition(label='Staff Train')
CropPlanting = Transition(label='Crop Planting')
YieldMonitor = Transition(label='Yield Monitor')
MarketSetup = Transition(label='Market Setup')
Maintenance = Transition(label='Maintenance')
WasteManage = Transition(label='Waste Manage')

# Define silent transitions for each activity
Skip1 = SilentTransition()
Skip2 = SilentTransition()
Skip3 = SilentTransition()
Skip4 = SilentTransition()
Skip5 = SilentTransition()
Skip6 = SilentTransition()
Skip7 = SilentTransition()
Skip8 = SilentTransition()
Skip9 = SilentTransition()
Skip10 = SilentTransition()
Skip11 = SilentTransition()
Skip12 = SilentTransition()
Skip13 = SilentTransition()
Skip14 = SilentTransition()
Skip15 = SilentTransition()
Skip16 = SilentTransition()
Skip17 = SilentTransition()

# Define the exclusive choice between PermitObtain and Skip1
xor1 = OperatorPOWL(operator=Operator.XOR, children=[PermitObtain, Skip1])

# Define the exclusive choice between DesignLayout and Skip2
xor2 = OperatorPOWL(operator=Operator.XOR, children=[DesignLayout, Skip2])

# Define the exclusive choice between SeedSourcing and Skip3
xor3 = OperatorPOWL(operator=Operator.XOR, children=[SeedSourcing, Skip3])

# Define the exclusive choice between IrrigationSet and Skip4
xor4 = OperatorPOWL(operator=Operator.XOR, children=[IrrigationSet, Skip4])

# Define the exclusive choice between NutrientMix and Skip5
xor5 = OperatorPOWL(operator=Operator.XOR, children=[NutrientMix, Skip5])

# Define the exclusive choice between PestControl and Skip6
xor6 = OperatorPOWL(operator=Operator.XOR, children=[PestControl, Skip6])

# Define the exclusive choice between SensorInstall and Skip7
xor7 = OperatorPOWL(operator=Operator.XOR, children=[SensorInstall, Skip7])

# Define the exclusive choice between StaffTrain and Skip8
xor8 = OperatorPOWL(operator=Operator.XOR, children=[StaffTrain, Skip8])

# Define the exclusive choice between CropPlanting and Skip9
xor9 = OperatorPOWL(operator=Operator.XOR, children=[CropPlanting, Skip9])

# Define the exclusive choice between YieldMonitor and Skip10
xor10 = OperatorPOWL(operator=Operator.XOR, children=[YieldMonitor, Skip10])

# Define the exclusive choice between MarketSetup and Skip11
xor11 = OperatorPOWL(operator=Operator.XOR, children=[MarketSetup, Skip11])

# Define the exclusive choice between Maintenance and Skip12
xor12 = OperatorPOWL(operator=Operator.XOR, children=[Maintenance, Skip12])

# Define the exclusive choice between WasteManage and Skip13
xor13 = OperatorPOWL(operator=Operator.XOR, children=[WasteManage, Skip13])

# Define the loop for the maintenance activities
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Maintenance, WasteManage])

# Define the loop for the crop planting activities
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[CropPlanting, YieldMonitor])

# Define the exclusive choice between loop1 and loop2
xor14 = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2])

# Define the exclusive choice between xor14 and xor13
xor15 = OperatorPOWL(operator=Operator.XOR, children=[xor14, xor13])

# Define the exclusive choice between xor15 and xor12
xor16 = OperatorPOWL(operator=Operator.XOR, children=[xor15, xor12])

# Define the exclusive choice between xor16 and xor11
xor17 = OperatorPOWL(operator=Operator.XOR, children=[xor16, xor11])

# Define the exclusive choice between xor17 and xor10
xor18 = OperatorPOWL(operator=Operator.XOR, children=[xor17, xor10])

# Define the exclusive choice between xor18 and xor9
xor19 = OperatorPOWL(operator=Operator.XOR, children=[xor18, xor9])

# Define the exclusive choice between xor19 and xor8
xor20 = OperatorPOWL(operator=Operator.XOR, children=[xor19, xor8])

# Define the exclusive choice between xor20 and xor7
xor21 = OperatorPOWL(operator=Operator.XOR, children=[xor20, xor7])

# Define the exclusive choice between xor21 and xor6
xor22 = OperatorPOWL(operator=Operator.XOR, children=[xor21, xor6])

# Define the exclusive choice between xor22 and xor5
xor23 = OperatorPOWL(operator=Operator.XOR, children=[xor22, xor5])

# Define the exclusive choice between xor23 and xor4
xor24 = OperatorPOWL(operator=Operator.XOR, children=[xor23, xor4])

# Define the exclusive choice between xor24 and xor3
xor25 = OperatorPOWL(operator=Operator.XOR, children=[xor24, xor3])

# Define the exclusive choice between xor25 and xor2
xor26 = OperatorPOWL(operator=Operator.XOR, children=[xor25, xor2])

# Define the exclusive choice between xor26 and xor1
xor27 = OperatorPOWL(operator=Operator.XOR, children=[xor26, xor1])

# Define the root POWL model
root = StrictPartialOrder(nodes=[SiteAssess, StructureCheck, SoilTest, ClimateEval, xor27])
root.order.add_edge(SiteAssess, StructureCheck)
root.order.add_edge(StructureCheck, SoilTest)
root.order.add_edge(SoilTest, ClimateEval)
root.order.add_edge(ClimateEval, xor27)

# Print the root POWL model
print(root)