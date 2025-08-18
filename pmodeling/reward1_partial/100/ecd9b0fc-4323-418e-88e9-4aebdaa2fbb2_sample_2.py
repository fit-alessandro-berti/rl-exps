from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions with their labels
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
Packaging_Prepare = Transition(label='Packaging Prep')
Delivery_Route = Transition(label='Delivery Route')
Data_Analysis = Transition(label='Data Analysis')
Yield_Forecast = Transition(label='Yield Forecast')

# Define the silent transitions (tau labels)
skip = SilentTransition()

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        Site_Survey,
        Structure_Check,
        Hydroponic_Install,
        Lighting_Setup,
        Climate_Control,
        Seed_Selection,
        Nutrient_Mix,
        Water_Recycling,
        Sensor_Deploy,
        Pest_Control,
        Growth_Monitor,
        Harvest_Plan,
        Packaging_Prepare,
        Delivery_Route,
        Data_Analysis,
        Yield_Forecast
    ]
)

# Define the edges in the partial order
root.order.add_edge(Site_Survey, Structure_Check)
root.order.add_edge(Structure_Check, Hydroponic_Install)
root.order.add_edge(Hydroponic_Install, Lighting_Setup)
root.order.add_edge(Lighting_Setup, Climate_Control)
root.order.add_edge(Climate_Control, Seed_Selection)
root.order.add_edge(Seed_Selection, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, Water_Recycling)
root.order.add_edge(Water_Recycling, Sensor_Deploy)
root.order.add_edge(Sensor_Deploy, Pest_Control)
root.order.add_edge(Pest_Control, Growth_Monitor)
root.order.add_edge(Growth_Monitor, Harvest_Plan)
root.order.add_edge(Harvest_Plan, Packaging_Prepare)
root.order.add_edge(Packaging_Prepare, Delivery_Route)
root.order.add_edge(Delivery_Route, Data_Analysis)
root.order.add_edge(Data_Analysis, Yield_Forecast)

# Print the root node
print(root)