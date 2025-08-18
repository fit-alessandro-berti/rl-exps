import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
Site_Survey = Transition(label='Site Survey')
Design_Planning = Transition(label='Design Planning')
Permit_Filing = Transition(label='Permit Filing')
Structural_Reinforce = Transition(label='Structural Reinforce')
Hydroponic_Setup = Transition(label='Hydroponic Setup')
Sensor_Install = Transition(label='Sensor Install')
Energy_Audit = Transition(label='Energy Audit')
Crop_Selection = Transition(label='Crop Selection')
Nutrient_Mix = Transition(label='Nutrient Mix')
Waste_Process = Transition(label='Waste Process')
Climate_Control = Transition(label='Climate Control')
Staff_Training = Transition(label='Staff Training')
Market_Study = Transition(label='Market Study')
Community_Meet = Transition(label='Community Meet')
Launch_Trial = Transition(label='Launch Trial')
Data_Monitor = Transition(label='Data Monitor')

# Define the partial order
root = StrictPartialOrder(nodes=[
    Site_Survey, Design_Planning, Permit_Filing, Structural_Reinforce, Hydroponic_Setup, Sensor_Install,
    Energy_Audit, Crop_Selection, Nutrient_Mix, Waste_Process, Climate_Control, Staff_Training, Market_Study,
    Community_Meet, Launch_Trial, Data_Monitor
])

# Define the order between nodes
root.order.add_edge(Site_Survey, Design_Planning)
root.order.add_edge(Design_Planning, Permit_Filing)
root.order.add_edge(Permit_Filing, Structural_Reinforce)
root.order.add_edge(Structural_Reinforce, Hydroponic_Setup)
root.order.add_edge(Hydroponic_Setup, Sensor_Install)
root.order.add_edge(Sensor_Install, Energy_Audit)
root.order.add_edge(Energy_Audit, Crop_Selection)
root.order.add_edge(Crop_Selection, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, Waste_Process)
root.order.add_edge(Waste_Process, Climate_Control)
root.order.add_edge(Climate_Control, Staff_Training)
root.order.add_edge(Staff_Training, Market_Study)
root.order.add_edge(Market_Study, Community_Meet)
root.order.add_edge(Community_Meet, Launch_Trial)
root.order.add_edge(Launch_Trial, Data_Monitor)

# Print the root POWL model
print(root)