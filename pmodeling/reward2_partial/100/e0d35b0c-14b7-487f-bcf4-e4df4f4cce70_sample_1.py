import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
Site_Survey = Transition(label='Site Survey')
Structural_Check = Transition(label='Structural Check')
Resource_Sourcing = Transition(label='Resource Sourcing')
System_Install = Transition(label='System Install')
Lighting_Setup = Transition(label='Lighting Setup')
Irrigation_Setup = Transition(label='Irrigation Setup')
Stakeholder_Meet = Transition(label='Stakeholder Meet')
Volunteer_Train = Transition(label='Volunteer Train')
Regulation_Review = Transition(label='Regulation Review')
Crop_Selection = Transition(label='Crop Selection')
Planting_Phase = Transition(label='Planting Phase')
Climate_Control = Transition(label='Climate Control')
Growth_Monitor = Transition(label='Growth Monitor')
Data_Logging = Transition(label='Data Logging')
Harvest_Event = Transition(label='Harvest Event')
Waste_Manage = Transition(label='Waste Manage')
Feedback_Collect = Transition(label='Feedback Collect')

# Define the partial order
root = StrictPartialOrder(nodes=[
    Site_Survey, Structural_Check, Resource_Sourcing, System_Install,
    Lighting_Setup, Irrigation_Setup, Stakeholder_Meet, Volunteer_Train,
    Regulation_Review, Crop_Selection, Planting_Phase, Climate_Control,
    Growth_Monitor, Data_Logging, Harvest_Event, Waste_Manage, Feedback_Collect
])

# Define the dependencies
root.order.add_edge(Site_Survey, Structural_Check)
root.order.add_edge(Structural_Check, Resource_Sourcing)
root.order.add_edge(Resource_Sourcing, System_Install)
root.order.add_edge(System_Install, Lighting_Setup)
root.order.add_edge(Lighting_Setup, Irrigation_Setup)
root.order.add_edge(Irrigation_Setup, Stakeholder_Meet)
root.order.add_edge(Stakeholder_Meet, Volunteer_Train)
root.order.add_edge(Volunteer_Train, Regulation_Review)
root.order.add_edge(Regulation_Review, Crop_Selection)
root.order.add_edge(Crop_Selection, Planting_Phase)
root.order.add_edge(Planting_Phase, Climate_Control)
root.order.add_edge(Climate_Control, Growth_Monitor)
root.order.add_edge(Growth_Monitor, Data_Logging)
root.order.add_edge(Data_Logging, Harvest_Event)
root.order.add_edge(Harvest_Event, Waste_Manage)
root.order.add_edge(Waste_Manage, Feedback_Collect)

print(root)