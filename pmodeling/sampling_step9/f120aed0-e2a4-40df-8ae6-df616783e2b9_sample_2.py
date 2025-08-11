import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
Site_Survey = Transition(label='Site Survey')
Rack_Design = Transition(label='Rack Design')
System_Setup = Transition(label='System Setup')
Climate_Calibrate = Transition(label='Climate Calibrate')
Nutrient_Prep = Transition(label='Nutrient Prep')
Crop_Select = Transition(label='Crop Select')
Seed_Germinate = Transition(label='Seed Germinate')
Sensor_Deploy = Transition(label='Sensor Deploy')
Pest_Control = Transition(label='Pest Control')
Harvest_Automate = Transition(label='Harvest Automate')
Quality_Check = Transition(label='Quality Check')
Pack_Produce = Transition(label='Pack Produce')
Data_Analyze = Transition(label='Data Analyze')
Engage_Community = Transition(label='Engage Community')
Logistics_Plan = Transition(label='Logistics Plan')

# Define the silent transitions
skip = SilentTransition()

# Define the loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Site_Survey, Rack_Design, System_Setup])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Climate_Calibrate, Nutrient_Prep, Crop_Select])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[Seed_Germinate, Sensor_Deploy, Pest_Control])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[Harvest_Automate, Quality_Check, Pack_Produce])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[Data_Analyze, Engage_Community, Logistics_Plan])

# Define the exclusive choice nodes
xor1 = OperatorPOWL(operator=Operator.XOR, children=[skip, loop1])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop2, xor1])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[loop3, xor2])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[loop4, xor3])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[loop5, xor4])

# Define the root
root = StrictPartialOrder(nodes=[xor5])
root.order.add_edge(xor5, xor4)
root.order.add_edge(xor4, xor3)
root.order.add_edge(xor3, xor2)
root.order.add_edge(xor2, xor1)
root.order.add_edge(xor1, loop1)
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop1, xor2)
root.order.add_edge(loop2, xor2)
root.order.add_edge(loop2, xor3)
root.order.add_edge(loop3, xor3)
root.order.add_edge(loop3, xor4)
root.order.add_edge(loop4, xor4)
root.order.add_edge(loop4, xor5)
root.order.add_edge(loop5, xor5)