import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
Site_Survey = Transition(label='Site Survey')
Permit_Review = Transition(label='Permit Review')
Design_Layout = Transition(label='Design Layout')
Material_Sourcing = Transition(label='Material Sourcing')
Irrigation_Setup = Transition(label='Irrigation Setup')
Sensor_Install = Transition(label='Sensor Install')
Structural_Test = Transition(label='Structural Test')
Recruit_Farmers = Transition(label='Recruit Farmers')
Trial_Planting = Transition(label='Trial Planting')
Pest_Control = Transition(label='Pest Control')
Soilless_Preparation = Transition(label='Soilless Prep')
System_Calibration = Transition(label='System Calibrate')
Data_Monitoring = Transition(label='Data Monitor')
Harvest_Planning = Transition(label='Harvest Plan')
Community_Outreach = Transition(label='Community Outreach')

# Define the control flow elements
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[Site_Survey, Permit_Review, Design_Layout, Material_Sourcing])
xor_1 = OperatorPOWL(operator=Operator.XOR, children=[Irrigation_Setup, Sensor_Install, Structural_Test])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[Recruit_Farmers, Trial_Planting])
xor_3 = OperatorPOWL(operator=Operator.XOR, children=[Pest_Control, Soilless_Preparation])
xor_4 = OperatorPOWL(operator=Operator.XOR, children=[System_Calibration, Data_Monitoring])
xor_5 = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Planning, Community_Outreach])

# Create the root partial order
root = StrictPartialOrder(nodes=[loop_1, xor_1, xor_2, xor_3, xor_4, xor_5])
root.order.add_edge(loop_1, xor_1)
root.order.add_edge(xor_1, xor_2)
root.order.add_edge(xor_2, xor_3)
root.order.add_edge(xor_3, xor_4)
root.order.add_edge(xor_4, xor_5)

# Print the root model
print(root)