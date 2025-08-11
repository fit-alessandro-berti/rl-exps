import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Site_Survey = Transition(label='Site Survey')
System_Design = Transition(label='System Design')
Permit_Filing = Transition(label='Permit Filing')
Modular_Build = Transition(label='Modular Build')
Sensor_Install = Transition(label='Sensor Install')
Climate_Setup = Transition(label='Climate Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
Waste_Setup = Transition(label='Waste Setup')
IoT_Deploy = Transition(label='IoT Deploy')
AI_Scheduling = Transition(label='AI Scheduling')
Energy_Audit = Transition(label='Energy Audit')
Compliance_Check = Transition(label='Compliance Check')
Crop_Planting = Transition(label='Crop Planting')
Yield_Monitor = Transition(label='Yield Monitor')
Data_Analysis = Transition(label='Data Analysis')
System_Upgrade = Transition(label='System Upgrade')

# Define silent activities
skip = SilentTransition()

# Define loops
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Site_Survey, System_Design, Permit_Filing])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Modular_Build, Sensor_Install, Climate_Setup])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[Nutrient_Mix, Waste_Setup, IoT_Deploy])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[AI_Scheduling, Energy_Audit, Compliance_Check])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[Crop_Planting, Yield_Monitor, Data_Analysis])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[System_Upgrade])

# Define XORs
xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop2, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[loop3, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[loop4, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[loop5, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[loop6, skip])

# Define root POWL model
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)