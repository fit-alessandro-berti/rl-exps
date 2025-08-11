import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
Site_Survey = Transition(label='Site Survey')
Climate_Study = Transition(label='Climate Study')
Design_Layout = Transition(label='Design Layout')
System_Install = Transition(label='System Install')
Crop_Select = Transition(label='Crop Select')
Nutrient_Plan = Transition(label='Nutrient Plan')
Sensor_Setup = Transition(label='Sensor Setup')
Automation_Test = Transition(label='Automation Test')
Staff_Train = Transition(label='Staff Train')
Compliance_Check = Transition(label='Compliance Check')
Marketing_Sync = Transition(label='Marketing Sync')
Data_Monitor = Transition(label='Data Monitor')
Yield_Analyze = Transition(label='Yield Analyze')
Supply_Chain = Transition(label='Supply Chain')
Customer_Engage = Transition(label='Customer Engage')

# Define the silent transition (empty label)
skip = SilentTransition()

# Define the loop (Design Layout -> Automation Test -> Staff Train)
loop = OperatorPOWL(operator=Operator.LOOP, children=[Design_Layout, Automation_Test, Staff_Train])

# Define the exclusive choice (Nutrient Plan -> Sensor Setup)
xor = OperatorPOWL(operator=Operator.XOR, children=[Nutrient_Plan, Sensor_Setup])

# Define the exclusive choice (Compliance Check -> Marketing Sync)
xor2 = OperatorPOWL(operator=Operator.XOR, children=[Compliance_Check, Marketing_Sync])

# Define the exclusive choice (Data Monitor -> Yield Analyze)
xor3 = OperatorPOWL(operator=Operator.XOR, children=[Data_Monitor, Yield_Analyze])

# Define the exclusive choice (Supply Chain -> Customer Engage)
xor4 = OperatorPOWL(operator=Operator.XOR, children=[Supply_Chain, Customer_Engage])

# Define the root process
root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3, xor4])
root.order.add_edge(loop, xor)
root.order.add_edge(loop, xor2)
root.order.add_edge(loop, xor3)
root.order.add_edge(loop, xor4)

# Print the root process
print(root)