import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities) with exact names
Site_Analysis = Transition(label='Site Analysis')
Structural_Check = Transition(label='Structural Check')
Rack_Install = Transition(label='Rack Install')
System_Setup = Transition(label='System Setup')
Hydroponics_Config = Transition(label='Hydroponics Config')
Aeroponics_Tune = Transition(label='Aeroponics Tune')
Lighting_Setup = Transition(label='Lighting Setup')
Enviro_Control = Transition(label='Enviro Control')
Sensor_Deploy = Transition(label='Sensor Deploy')
Waste_Recycle = Transition(label='Waste Recycle')
Water_Reuse = Transition(label='Water Reuse')
Staff_Training = Transition(label='Staff Training')
Test_Grow = Transition(label='Test Grow')
Data_Analytics = Transition(label='Data Analytics')
Yield_Optimize = Transition(label='Yield Optimize')

# Define silent transitions (same names as the activities)
skip1 = SilentTransition()
skip2 = SilentTransition()
skip3 = SilentTransition()
skip4 = SilentTransition()
skip5 = SilentTransition()
skip6 = SilentTransition()

# Define exclusive choice (XOR) between System Setup and Hydroponics Config
xor1 = OperatorPOWL(operator=Operator.XOR, children=[System_Setup, skip1])

# Define exclusive choice (XOR) between Aeroponics Tune and skip2
xor2 = OperatorPOWL(operator=Operator.XOR, children=[Aeroponics_Tune, skip2])

# Define exclusive choice (XOR) between Lighting Setup and Enviro_Control
xor3 = OperatorPOWL(operator=Operator.XOR, children=[Lighting_Setup, Enviro_Control])

# Define exclusive choice (XOR) between Sensor_Deploy and Waste_Recycle
xor4 = OperatorPOWL(operator=Operator.XOR, children=[Sensor_Deploy, Waste_Recycle])

# Define exclusive choice (XOR) between Water_Reuse and Staff_Training
xor5 = OperatorPOWL(operator=Operator.XOR, children=[Water_Reuse, Staff_Training])

# Define exclusive choice (XOR) between Test_Grow and Data_Analytics
xor6 = OperatorPOWL(operator=Operator.XOR, children=[Test_Grow, Data_Analytics])

# Define exclusive choice (XOR) between Data_Analytics and Yield_Optimize
xor7 = OperatorPOWL(operator=Operator.XOR, children=[Data_Analytics, Yield_Optimize])

# Define a loop (star) for the entire process
loop = OperatorPOWL(operator=Operator.LOOP, children=[Site_Analysis, Structural_Check, Rack_Install, xor1, xor2, xor3, xor4, xor5, xor6, xor7])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop])
root.order.add_edge(loop, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, loop)