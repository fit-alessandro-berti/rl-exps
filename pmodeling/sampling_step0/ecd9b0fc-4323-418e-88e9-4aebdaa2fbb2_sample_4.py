import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
Site_Survey = Transition(label='Site Survey')
Structure_Check = Transition(label='Structure Check')
Hydroponic_Install = Transition(label='Hydroponic Install')
Lighting_Setup = Transition(label='Lighting Setup')
Climate_Control = Transition(label='Climate Control')
Seed_Selection = Transition(label='Seed Selection')
Nutrient_Mix = Transition(label='Nutrient Mix')
Water_Recycling = Transition(label='Water Recycling')
Sensor_Deploy = Transition(label='Sensor Deploy')
Pest_Control = Transition(label='Pest Control')
Growth_Monitor = Transition(label='Growth Monitor')
Harvest_Plan = Transition(label='Harvest Plan')
Packaging_Prep = Transition(label='Packaging Prep')
Delivery_Route = Transition(label='Delivery Route')
Data_Analysis = Transition(label='Data Analysis')
Yield_Forecast = Transition(label='Yield Forecast')

# Define silent transitions
skip = SilentTransition()

# Define the process structure
# Site Survey --> Structure Check --> Hydroponic Install --> Lighting Setup --> Climate Control
# Seed Selection --> Nutrient Mix --> Water Recycling --> Sensor Deploy
# Pest Control --> Growth Monitor
# Harvest Plan --> Packaging Prep --> Delivery Route
# Data Analysis --> Yield Forecast

# Create the POWL model
root = StrictPartialOrder()
root.add_transition(Site_Survey)
root.add_transition(Structure_Check)
root.add_transition(Hydroponic_Install)
root.add_transition(Lighting_Setup)
root.add_transition(Climate_Control)
root.add_transition(Seed_Selection)
root.add_transition(Nutrient_Mix)
root.add_transition(Water_Recycling)
root.add_transition(Sensor_Deploy)
root.add_transition(Pest_Control)
root.add_transition(Growth_Monitor)
root.add_transition(Harvest_Plan)
root.add_transition(Packaging_Prep)
root.add_transition(Delivery_Route)
root.add_transition(Data_Analysis)
root.add_transition(Yield_Forecast)

# Define the order of execution
root.add_edge(Site_Survey, Structure_Check)
root.add_edge(Structure_Check, Hydroponic_Install)
root.add_edge(Hydroponic_Install, Lighting_Setup)
root.add_edge(Lighting_Setup, Climate_Control)
root.add_edge(Seed_Selection, Nutrient_Mix)
root.add_edge(Nutrient_Mix, Water_Recycling)
root.add_edge(Water_Recycling, Sensor_Deploy)
root.add_edge(Pest_Control, Growth_Monitor)
root.add_edge(Harvest_Plan, Packaging_Prep)
root.add_edge(Packaging_Prep, Delivery_Route)
root.add_edge(Data_Analysis, Yield_Forecast)

# Define the loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[Pest_Control, Growth_Monitor])
root.add_transition(loop)
root.add_edge(Site_Survey, loop)
root.add_edge(Structure_Check, loop)
root.add_edge(Hydroponic_Install, loop)
root.add_edge(Lighting_Setup, loop)
root.add_edge(Climate_Control, loop)
root.add_edge(Seed_Selection, loop)
root.add_edge(Nutrient_Mix, loop)
root.add_edge(Water_Recycling, loop)
root.add_edge(Sensor_Deploy, loop)
root.add_edge(Pest_Control, loop)
root.add_edge(Growth_Monitor, loop)

# Define the exclusive choice
xor = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor)
root.add_edge(Delivery_Route, xor)
root.add_edge(Packaging_Prep, xor)

# Define the loop for the exclusive choice
loop_xor = OperatorPOWL(operator=Operator.LOOP, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(loop_xor)
root.add_edge(Delivery_Route, loop_xor)
root.add_edge(Packaging_Prep, loop_xor)

# Define the exclusive choice for the delivery route
xor_delivery = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_delivery)
root.add_edge(Delivery_Route, xor_delivery)
root.add_edge(Packaging_Prep, xor_delivery)

# Define the exclusive choice for the packaging prep
xor_packaging = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_packaging)
root.add_edge(Delivery_Route, xor_packaging)
root.add_edge(Packaging_Prep, xor_packaging)

# Define the exclusive choice for the yield forecast
xor_yield = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_yield)
root.add_edge(Delivery_Route, xor_yield)
root.add_edge(Packaging_Prep, xor_yield)

# Define the exclusive choice for the data analysis
xor_data = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_data)
root.add_edge(Delivery_Route, xor_data)
root.add_edge(Packaging_Prep, xor_data)

# Define the exclusive choice for the delivery route
xor_delivery = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_delivery)
root.add_edge(Delivery_Route, xor_delivery)
root.add_edge(Packaging_Prep, xor_delivery)

# Define the exclusive choice for the packaging prep
xor_packaging = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_packaging)
root.add_edge(Delivery_Route, xor_packaging)
root.add_edge(Packaging_Prep, xor_packaging)

# Define the exclusive choice for the yield forecast
xor_yield = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_yield)
root.add_edge(Delivery_Route, xor_yield)
root.add_edge(Packaging_Prep, xor_yield)

# Define the exclusive choice for the data analysis
xor_data = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_data)
root.add_edge(Delivery_Route, xor_data)
root.add_edge(Packaging_Prep, xor_data)

# Define the exclusive choice for the delivery route
xor_delivery = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_delivery)
root.add_edge(Delivery_Route, xor_delivery)
root.add_edge(Packaging_Prep, xor_delivery)

# Define the exclusive choice for the packaging prep
xor_packaging = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_packaging)
root.add_edge(Delivery_Route, xor_packaging)
root.add_edge(Packaging_Prep, xor_packaging)

# Define the exclusive choice for the yield forecast
xor_yield = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_yield)
root.add_edge(Delivery_Route, xor_yield)
root.add_edge(Packaging_Prep, xor_yield)

# Define the exclusive choice for the data analysis
xor_data = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_data)
root.add_edge(Delivery_Route, xor_data)
root.add_edge(Packaging_Prep, xor_data)

# Define the exclusive choice for the delivery route
xor_delivery = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_delivery)
root.add_edge(Delivery_Route, xor_delivery)
root.add_edge(Packaging_Prep, xor_delivery)

# Define the exclusive choice for the packaging prep
xor_packaging = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_packaging)
root.add_edge(Delivery_Route, xor_packaging)
root.add_edge(Packaging_Prep, xor_packaging)

# Define the exclusive choice for the yield forecast
xor_yield = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_yield)
root.add_edge(Delivery_Route, xor_yield)
root.add_edge(Packaging_Prep, xor_yield)

# Define the exclusive choice for the data analysis
xor_data = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_data)
root.add_edge(Delivery_Route, xor_data)
root.add_edge(Packaging_Prep, xor_data)

# Define the exclusive choice for the delivery route
xor_delivery = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_delivery)
root.add_edge(Delivery_Route, xor_delivery)
root.add_edge(Packaging_Prep, xor_packaging)

# Define the exclusive choice for the packaging prep
xor_packaging = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_packaging)
root.add_edge(Delivery_Route, xor_packaging)
root.add_edge(Packaging_Prep, xor_packaging)

# Define the exclusive choice for the yield forecast
xor_yield = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_yield)
root.add_edge(Delivery_Route, xor_yield)
root.add_edge(Packaging_Prep, xor_yield)

# Define the exclusive choice for the data analysis
xor_data = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_data)
root.add_edge(Delivery_Route, xor_data)
root.add_edge(Packaging_Prep, xor_data)

# Define the exclusive choice for the delivery route
xor_delivery = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_delivery)
root.add_edge(Delivery_Route, xor_delivery)
root.add_edge(Packaging_Prep, xor_packaging)

# Define the exclusive choice for the packaging prep
xor_packaging = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_packaging)
root.add_edge(Delivery_Route, xor_packaging)
root.add_edge(Packaging_Prep, xor_packaging)

# Define the exclusive choice for the yield forecast
xor_yield = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_yield)
root.add_edge(Delivery_Route, xor_yield)
root.add_edge(Packaging_Prep, xor_yield)

# Define the exclusive choice for the data analysis
xor_data = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_data)
root.add_edge(Delivery_Route, xor_data)
root.add_edge(Packaging_Prep, xor_data)

# Define the exclusive choice for the delivery route
xor_delivery = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_delivery)
root.add_edge(Delivery_Route, xor_delivery)
root.add_edge(Packaging_Prep, xor_packaging)

# Define the exclusive choice for the packaging prep
xor_packaging = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_packaging)
root.add_edge(Delivery_Route, xor_packaging)
root.add_edge(Packaging_Prep, xor_packaging)

# Define the exclusive choice for the yield forecast
xor_yield = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_yield)
root.add_edge(Delivery_Route, xor_yield)
root.add_edge(Packaging_Prep, xor_yield)

# Define the exclusive choice for the data analysis
xor_data = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_data)
root.add_edge(Delivery_Route, xor_data)
root.add_edge(Packaging_Prep, xor_data)

# Define the exclusive choice for the delivery route
xor_delivery = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_delivery)
root.add_edge(Delivery_Route, xor_delivery)
root.add_edge(Packaging_Prep, xor_packaging)

# Define the exclusive choice for the packaging prep
xor_packaging = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_packaging)
root.add_edge(Delivery_Route, xor_packaging)
root.add_edge(Packaging_Prep, xor_packaging)

# Define the exclusive choice for the yield forecast
xor_yield = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_yield)
root.add_edge(Delivery_Route, xor_yield)
root.add_edge(Packaging_Prep, xor_yield)

# Define the exclusive choice for the data analysis
xor_data = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_data)
root.add_edge(Delivery_Route, xor_data)
root.add_edge(Packaging_Prep, xor_data)

# Define the exclusive choice for the delivery route
xor_delivery = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_delivery)
root.add_edge(Delivery_Route, xor_delivery)
root.add_edge(Packaging_Prep, xor_packaging)

# Define the exclusive choice for the packaging prep
xor_packaging = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_packaging)
root.add_edge(Delivery_Route, xor_packaging)
root.add_edge(Packaging_Prep, xor_packaging)

# Define the exclusive choice for the yield forecast
xor_yield = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_yield)
root.add_edge(Delivery_Route, xor_yield)
root.add_edge(Packaging_Prep, xor_yield)

# Define the exclusive choice for the data analysis
xor_data = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_data)
root.add_edge(Delivery_Route, xor_data)
root.add_edge(Packaging_Prep, xor_data)

# Define the exclusive choice for the delivery route
xor_delivery = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_delivery)
root.add_edge(Delivery_Route, xor_delivery)
root.add_edge(Packaging_Prep, xor_packaging)

# Define the exclusive choice for the packaging prep
xor_packaging = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_packaging)
root.add_edge(Delivery_Route, xor_packaging)
root.add_edge(Packaging_Prep, xor_packaging)

# Define the exclusive choice for the yield forecast
xor_yield = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_yield)
root.add_edge(Delivery_Route, xor_yield)
root.add_edge(Packaging_Prep, xor_yield)

# Define the exclusive choice for the data analysis
xor_data = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_data)
root.add_edge(Delivery_Route, xor_data)
root.add_edge(Packaging_Prep, xor_data)

# Define the exclusive choice for the delivery route
xor_delivery = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_delivery)
root.add_edge(Delivery_Route, xor_delivery)
root.add_edge(Packaging_Prep, xor_packaging)

# Define the exclusive choice for the packaging prep
xor_packaging = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_packaging)
root.add_edge(Delivery_Route, xor_packaging)
root.add_edge(Packaging_Prep, xor_packaging)

# Define the exclusive choice for the yield forecast
xor_yield = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_yield)
root.add_edge(Delivery_Route, xor_yield)
root.add_edge(Packaging_Prep, xor_yield)

# Define the exclusive choice for the data analysis
xor_data = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_data)
root.add_edge(Delivery_Route, xor_data)
root.add_edge(Packaging_Prep, xor_data)

# Define the exclusive choice for the delivery route
xor_delivery = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_delivery)
root.add_edge(Delivery_Route, xor_delivery)
root.add_edge(Packaging_Prep, xor_packaging)

# Define the exclusive choice for the packaging prep
xor_packaging = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_packaging)
root.add_edge(Delivery_Route, xor_packaging)
root.add_edge(Packaging_Prep, xor_packaging)

# Define the exclusive choice for the yield forecast
xor_yield = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_yield)
root.add_edge(Delivery_Route, xor_yield)
root.add_edge(Packaging_Prep, xor_yield)

# Define the exclusive choice for the data analysis
xor_data = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_data)
root.add_edge(Delivery_Route, xor_data)
root.add_edge(Packaging_Prep, xor_data)

# Define the exclusive choice for the delivery route
xor_delivery = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_delivery)
root.add_edge(Delivery_Route, xor_delivery)
root.add_edge(Packaging_Prep, xor_packaging)

# Define the exclusive choice for the packaging prep
xor_packaging = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_packaging)
root.add_edge(Delivery_Route, xor_packaging)
root.add_edge(Packaging_Prep, xor_packaging)

# Define the exclusive choice for the yield forecast
xor_yield = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, Packaging_Prep])
root.add_transition(xor_yield)