import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) for the process
Load_Assess = Transition(label='Load Assess')
Permit_Review = Transition(label='Permit Review')
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Soil_Mix = Transition(label='Soil Mix')
Install_Beds = Transition(label='Install Beds')
Irrigation_Set = Transition(label='Irrigation Set')
Climate_Test = Transition(label='Climate Test')
Sensor_Deploy = Transition(label='Sensor Deploy')
Energy_Setup = Transition(label='Energy Setup')
Crop_Select = Transition(label='Crop Select')
Plant_Seeding = Transition(label='Plant Seeding')
Community_Meet = Transition(label='Community Meet')
Compliance_Check = Transition(label='Compliance Check')
Growth_Monitor = Transition(label='Growth Monitor')
Harvest_Plan = Transition(label='Harvest Plan')
Waste_Recycle = Transition(label='Waste Recycle')

# Define the partial order graph
root = StrictPartialOrder(nodes=[
    Load_Assess, Permit_Review, Site_Survey, Design_Layout, Soil_Mix, Install_Beds, Irrigation_Set, Climate_Test, Sensor_Deploy, Energy_Setup, Crop_Select, Plant_Seeding, Community_Meet, Compliance_Check, Growth_Monitor, Harvest_Plan, Waste_Recycle
])

# Define the partial order dependencies
root.order.add_edge(Load_Assess, Permit_Review)
root.order.add_edge(Permit_Review, Site_Survey)
root.order.add_edge(Site_Survey, Design_Layout)
root.order.add_edge(Design_Layout, Soil_Mix)
root.order.add_edge(Soil_Mix, Install_Beds)
root.order.add_edge(Install_Beds, Irrigation_Set)
root.order.add_edge(Irrigation_Set, Climate_Test)
root.order.add_edge(Climate_Test, Sensor_Deploy)
root.order.add_edge(Sensor_Deploy, Energy_Setup)
root.order.add_edge(Energy_Setup, Crop_Select)
root.order.add_edge(Crop_Select, Plant_Seeding)
root.order.add_edge(Plant_Seeding, Community_Meet)
root.order.add_edge(Community_Meet, Compliance_Check)
root.order.add_edge(Compliance_Check, Growth_Monitor)
root.order.add_edge(Growth_Monitor, Harvest_Plan)
root.order.add_edge(Harvest_Plan, Waste_Recycle)

# Print the root POWL model
print(root)