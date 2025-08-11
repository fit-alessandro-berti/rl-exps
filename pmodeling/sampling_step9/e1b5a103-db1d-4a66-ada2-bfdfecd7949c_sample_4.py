import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define silent transitions
Skip = SilentTransition()

# Define loop nodes
Loop_Cycle = OperatorPOWL(operator=Operator.LOOP, children=[Site_Analysis, Structure_Check, Climate_Setup, Hydroponics_Install, Nutrient_Mix, Seed_Select, Light_Schedule, Irrigation_Plan, Health_Monitor, Pest_Control, Robotic_Harvest, Clean_Packaging, Distribution_Plan, Data_Collection, Cycle_Feedback])

# Define XOR nodes
XOR_Harvest = OperatorPOWL(operator=Operator.XOR, children=[Robotic_Harvest, Skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[Loop_Cycle, XOR_Harvest])

# Define the dependencies
root.order.add_edge(Loop_Cycle, XOR_Harvest)

# Print the root POWL model
print(root)