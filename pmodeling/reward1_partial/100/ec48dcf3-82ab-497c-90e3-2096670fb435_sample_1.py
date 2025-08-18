import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the partial order
root = StrictPartialOrder(nodes=[Site_Survey, Design_Layout, Structure_Build, System_Install, Climate_Setup, Nutrient_Prep, Seed_Germinate, Planting_Phase, Sensor_Deploy, Pest_Control, Water_Monitor, Data_Analyze, Staff_Train, Yield_Forecast, Community_Meet])

# Add edges to represent the dependencies between activities
root.order.add_edge(Site_Survey, Design_Layout)
root.order.add_edge(Design_Layout, Structure_Build)
root.order.add_edge(Structure_Build, System_Install)
root.order.add_edge(System_Install, Climate_Setup)
root.order.add_edge(Climate_Setup, Nutrient_Prep)
root.order.add_edge(Nutrient_Prep, Seed_Germinate)
root.order.add_edge(Seed_Germinate, Planting_Phase)
root.order.add_edge(Planting_Phase, Sensor_Deploy)
root.order.add_edge(Sensor_Deploy, Pest_Control)
root.order.add_edge(Pest_Control, Water_Monitor)
root.order.add_edge(Water_Monitor, Data_Analyze)
root.order.add_edge(Data_Analyze, Staff_Train)
root.order.add_edge(Staff_Train, Yield_Forecast)
root.order.add_edge(Yield_Forecast, Community_Meet)

# Optionally, you can add silent transitions for pauses or interruptions if needed
# For example:
# root.order.add_edge(Site_Survey, Design_Layout, silent=True)
# root.order.add_edge(Design_Layout, Structure_Build, silent=True)
# ...

# Now, 'root' contains the POWL model for the urban vertical farm setup process.