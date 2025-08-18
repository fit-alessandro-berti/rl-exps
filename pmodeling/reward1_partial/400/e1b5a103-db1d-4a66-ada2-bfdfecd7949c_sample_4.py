import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
Site_Analysis = Transition(label='Site Analysis')
Structure_Check = Transition(label='Structure Check')
Climate_Setup = Transition(label='Climate Setup')
Hydroponics_Install = Transition(label='Hydroponics Install')
Nutrient_Mix = Transition(label='Nutrient Mix')
Seed_Select = Transition(label='Seed Select')
Light_Schedule = Transition(label='Light Schedule')
Irrigation_Plan = Transition(label='Irrigation Plan')
Health_Monitor = Transition(label='Health Monitor')
Pest_Control = Transition(label='Pest Control')
Robotic_Harvest = Transition(label='Robotic Harvest')
Clean_Packaging = Transition(label='Clean Packaging')
Distribution_Plan = Transition(label='Distribution Plan')
Data_Collection = Transition(label='Data Collection')
Cycle_Feedback = Transition(label='Cycle Feedback')

# Define the partial order
root = StrictPartialOrder(nodes=[
    Site_Analysis,
    Structure_Check,
    Climate_Setup,
    Hydroponics_Install,
    Nutrient_Mix,
    Seed_Select,
    Light_Schedule,
    Irrigation_Plan,
    Health_Monitor,
    Pest_Control,
    Robotic_Harvest,
    Clean_Packaging,
    Distribution_Plan,
    Data_Collection,
    Cycle_Feedback
])

# Define the dependencies between nodes
root.order.add_edge(Site_Analysis, Structure_Check)
root.order.add_edge(Structure_Check, Climate_Setup)
root.order.add_edge(Climate_Setup, Hydroponics_Install)
root.order.add_edge(Hydroponics_Install, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, Seed_Select)
root.order.add_edge(Seed_Select, Light_Schedule)
root.order.add_edge(Light_Schedule, Irrigation_Plan)
root.order.add_edge(Irrigation_Plan, Health_Monitor)
root.order.add_edge(Health_Monitor, Pest_Control)
root.order.add_edge(Pest_Control, Robotic_Harvest)
root.order.add_edge(Robotic_Harvest, Clean_Packaging)
root.order.add_edge(Clean_Packaging, Distribution_Plan)
root.order.add_edge(Distribution_Plan, Data_Collection)
root.order.add_edge(Data_Collection, Cycle_Feedback)