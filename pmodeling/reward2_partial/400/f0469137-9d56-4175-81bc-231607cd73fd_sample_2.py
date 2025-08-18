import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities) with their labels
Site_Analysis = Transition(label='Site Analysis')
Climate_Setup = Transition(label='Climate Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
Seed_Germinate = Transition(label='Seed Germinate')
Auto_Planting = Transition(label='Auto Planting')
Irrigation_Setup = Transition(label='Irrigation Setup')
IoT_Monitoring = Transition(label='IoT Monitoring')
Pest_Detection = Transition(label='Pest Detection')
Drone_Pollinate = Transition(label='Drone Pollinate')
Pesticide_Spray = Transition(label='Pesticide Spray')
Robotic_Harvest = Transition(label='Robotic Harvest')
Quality_Check = Transition(label='Quality Check')
Package_Product = Transition(label='Package Product')
Waste_Recycle = Transition(label='Waste Recycle')
Energy_Optimize = Transition(label='Energy Optimize')
Data_Logging = Transition(label='Data Logging')

# Define the POWL model as a strict partial order
root = StrictPartialOrder(nodes=[
    Site_Analysis, Climate_Setup, Nutrient_Mix, Seed_Germinate, Auto_Planting, Irrigation_Setup, IoT_Monitoring, Pest_Detection, Drone_Pollinate, Pesticide_Spray, Robotic_Harvest, Quality_Check, Package_Product, Waste_Recycle, Energy_Optimize, Data_Logging
])

# Add edges to define the partial order
root.order.add_edge(Site_Analysis, Climate_Setup)
root.order.add_edge(Climate_Setup, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, Seed_Germinate)
root.order.add_edge(Seed_Germinate, Auto_Planting)
root.order.add_edge(Auto_Planting, Irrigation_Setup)
root.order.add_edge(Irrigation_Setup, IoT_Monitoring)
root.order.add_edge(IoT_Monitoring, Pest_Detection)
root.order.add_edge(Pest_Detection, Drone_Pollinate)
root.order.add_edge(Drone_Pollinate, Pesticide_Spray)
root.order.add_edge(Pesticide_Spray, Robotic_Harvest)
root.order.add_edge(Robotic_Harvest, Quality_Check)
root.order.add_edge(Quality_Check, Package_Product)
root.order.add_edge(Package_Product, Waste_Recycle)
root.order.add_edge(Waste_Recycle, Energy_Optimize)
root.order.add_edge(Energy_Optimize, Data_Logging)

# Print the root of the POWL model
print(root)