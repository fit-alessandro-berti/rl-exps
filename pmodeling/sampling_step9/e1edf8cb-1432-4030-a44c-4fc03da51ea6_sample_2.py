import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
Site_Survey = Transition(label='Site Survey')
Structural_Check = Transition(label='Structural Check')
Env_Control = Transition(label='Env Control')
Hydro_Setup = Transition(label='Hydro Setup')
Crop_Select = Transition(label='Crop Select')
IoT_Install = Transition(label='IoT Install')
Sensor_Calibrate = Transition(label='Sensor Calibrate')
Water_Cycle = Transition(label='Water Cycle')
Nutrient_Mix = Transition(label='Nutrient Mix')
Lighting_Adjust = Transition(label='Lighting Adjust')
Staff_Train = Transition(label='Staff Train')
Waste_Manage = Transition(label='Waste Manage')
Energy_Audit = Transition(label='Energy Audit')
Harvest_Plan = Transition(label='Harvest Plan')
Delivery_Setup = Transition(label='Delivery Setup')
Market_Align = Transition(label='Market Align')
skip = SilentTransition()

# Define the partial order
loop = OperatorPOWL(operator=Operator.LOOP, children=[Site_Survey, Structural_Check, Env_Control, Hydro_Setup, Crop_Select, IoT_Install, Sensor_Calibrate, Water_Cycle, Nutrient_Mix, Lighting_Adjust, Staff_Train, Waste_Manage, Energy_Audit, Harvest_Plan, Delivery_Setup, Market_Align])
xor = OperatorPOWL(operator=Operator.XOR, children=[skip])

# Define the root
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

print(root)