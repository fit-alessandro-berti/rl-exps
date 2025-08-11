import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Site_Survey = Transition(label='Site Survey')
Load_Test = Transition(label='Load Test')
Climate_Study = Transition(label='Climate Study')
Permit_Check = Transition(label='Permit Check')
System_Design = Transition(label='System Design')
Equipment_Buy = Transition(label='Equipment Buy')
Sensor_Setup = Transition(label='Sensor Setup')
Irrigation_Fit = Transition(label='Irrigation Fit')
Solar_Install = Transition(label='Solar Install')
Staff_Train = Transition(label='Staff Train')
Pilot_Plant = Transition(label='Pilot Plant')
Data_Monitor = Transition(label='Data Monitor')
Crop_Harvest = Transition(label='Crop Harvest')
Maintenance_Plan = Transition(label='Maintenance Plan')
Community_Meet = Transition(label='Community Meet')

# Define silent transitions
skip = SilentTransition()

# Define the loop nodes
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[Permit_Check, skip])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[Equipment_Buy, skip])
loop_3 = OperatorPOWL(operator=Operator.LOOP, children=[Solar_Install, skip])
loop_4 = OperatorPOWL(operator=Operator.LOOP, children=[Staff_Train, skip])
loop_5 = OperatorPOWL(operator=Operator.LOOP, children=[Data_Monitor, skip])
loop_6 = OperatorPOWL(operator=Operator.LOOP, children=[Maintenance_Plan, skip])

# Define the exclusive choice nodes
xor_1 = OperatorPOWL(operator=Operator.XOR, children=[loop_1, skip])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[loop_2, skip])
xor_3 = OperatorPOWL(operator=Operator.XOR, children=[loop_3, skip])
xor_4 = OperatorPOWL(operator=Operator.XOR, children=[loop_4, skip])
xor_5 = OperatorPOWL(operator=Operator.XOR, children=[loop_5, skip])
xor_6 = OperatorPOWL(operator=Operator.XOR, children=[loop_6, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[xor_1, xor_2, xor_3, xor_4, xor_5, xor_6])
root.order.add_edge(xor_1, xor_2)
root.order.add_edge(xor_2, xor_3)
root.order.add_edge(xor_3, xor_4)
root.order.add_edge(xor_4, xor_5)
root.order.add_edge(xor_5, xor_6)

# Print the root POWL model
print(root)