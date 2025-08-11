import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the transitions
skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[Site_Analysis, Structural_Check, Rack_Install, System_Setup, Hydroponics_Config, Aeroponics_Tune, Lighting_Setup, Enviro_Control, Sensor_Deploy, Waste_Recycle, Water_Reuse, Staff_Training])
xor = OperatorPOWL(operator=Operator.XOR, children=[Test_Grow, Data_Analytics])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Save the final result in the variable 'root'
root