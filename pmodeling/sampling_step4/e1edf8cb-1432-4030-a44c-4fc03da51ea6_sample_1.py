import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
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

# Define the partial order structure
root = StrictPartialOrder(nodes=[Site_Survey, Structural_Check, Env_Control, Hydro_Setup, Crop_Select, IoT_Install, Sensor_Calibrate, Water_Cycle, Nutrient_Mix, Lighting_Adjust, Staff_Train, Waste_Manage, Energy_Audit, Harvest_Plan, Delivery_Setup, Market_Align])

# Define the order dependencies
root.order.add_edge(Site_Survey, Structural_Check)
root.order.add_edge(Structural_Check, Env_Control)
root.order.add_edge(Env_Control, Hydro_Setup)
root.order.add_edge(Hydro_Setup, Crop_Select)
root.order.add_edge(Crop_Select, IoT_Install)
root.order.add_edge(IoT_Install, Sensor_Calibrate)
root.order.add_edge(Sensor_Calibrate, Water_Cycle)
root.order.add_edge(Water_Cycle, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, Lighting_Adjust)
root.order.add_edge(Lighting_Adjust, Staff_Train)
root.order.add_edge(Staff_Train, Waste_Manage)
root.order.add_edge(Waste_Manage, Energy_Audit)
root.order.add_edge(Energy_Audit, Harvest_Plan)
root.order.add_edge(Harvest_Plan, Delivery_Setup)
root.order.add_edge(Delivery_Setup, Market_Align)

print(root)