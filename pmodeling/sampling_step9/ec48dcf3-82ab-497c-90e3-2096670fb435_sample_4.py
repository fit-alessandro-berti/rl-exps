import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Structure_Build = Transition(label='Structure Build')
System_Install = Transition(label='System Install')
Climate_Setup = Transition(label='Climate Setup')
Nutrient_Prep = Transition(label='Nutrient Prep')
Seed_Germinate = Transition(label='Seed Germinate')
Planting_Phase = Transition(label='Planting Phase')
Sensor_Deploy = Transition(label='Sensor Deploy')
Pest_Control = Transition(label='Pest Control')
Water_Monitor = Transition(label='Water Monitor')
Data_Analyze = Transition(label='Data Analyze')
Staff_Train = Transition(label='Staff Train')
Yield_Forecast = Transition(label='Yield Forecast')
Community_Meet = Transition(label='Community Meet')

# Define silent transitions (tau labels)
skip = SilentTransition()

# Define the loop node for pest control and water monitoring
pest_water_loop = OperatorPOWL(operator=Operator.LOOP, children=[Pest_Control, Water_Monitor])

# Define the exclusive choice for nutrient preparation and seed germination
nutrient_germinate_choice = OperatorPOWL(operator=Operator.XOR, children=[Nutrient_Prep, skip])

# Define the exclusive choice for planting phase and data analysis
planting_data_choice = OperatorPOWL(operator=Operator.XOR, children=[Planting_Phase, Data_Analyze])

# Define the exclusive choice for staff training and community engagement
staff_community_choice = OperatorPOWL(operator=Operator.XOR, children=[Staff_Train, Community_Meet])

# Define the POWL model
root = StrictPartialOrder(nodes=[pest_water_loop, nutrient_germinate_choice, planting_data_choice, staff_community_choice])
root.order.add_edge(pest_water_loop, nutrient_germinate_choice)
root.order.add_edge(nutrient_germinate_choice, planting_data_choice)
root.order.add_edge(planting_data_choice, staff_community_choice)

# Print the POWL model
print(root)