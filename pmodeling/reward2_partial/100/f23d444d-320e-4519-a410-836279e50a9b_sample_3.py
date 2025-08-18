import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
Site_Survey = Transition(label='Site Survey')
System_Design = Transition(label='System Design')
Module_Build = Transition(label='Module Build')
Nutrient_Mix = Transition(label='Nutrient Mix')
Seed_Selection = Transition(label='Seed Selection')
Planting_Plan = Transition(label='Planting Plan')
Irrigation_Setup = Transition(label='Irrigation Setup')
Climate_Control = Transition(label='Climate Control')
Lighting_Adjust = Transition(label='Lighting Adjust')
Pest_Monitor = Transition(label='Pest Monitor')
Waste_Cycle = Transition(label='Waste Cycle')
Data_Capture = Transition(label='Data Capture')
Yield_Forecast = Transition(label='Yield Forecast')
Regulation_Check = Transition(label='Regulation Check')
Community_Meet = Transition(label='Community Meet')
Harvest_Prep = Transition(label='Harvest Prep')
Market_Link = Transition(label='Market Link')

# Define the POWL model
root = StrictPartialOrder(nodes=[
    Site_Survey,
    System_Design,
    Module_Build,
    Nutrient_Mix,
    Seed_Selection,
    Planting_Plan,
    Irrigation_Setup,
    Climate_Control,
    Lighting_Adjust,
    Pest_Monitor,
    Waste_Cycle,
    Data_Capture,
    Yield_Forecast,
    Regulation_Check,
    Community_Meet,
    Harvest_Prep,
    Market_Link
])

# Define the dependencies
root.order.add_edge(Site_Survey, System_Design)
root.order.add_edge(System_Design, Module_Build)
root.order.add_edge(Module_Build, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, Seed_Selection)
root.order.add_edge(Seed_Selection, Planting_Plan)
root.order.add_edge(Planting_Plan, Irrigation_Setup)
root.order.add_edge(Irrigation_Setup, Climate_Control)
root.order.add_edge(Climate_Control, Lighting_Adjust)
root.order.add_edge(Lighting_Adjust, Pest_Monitor)
root.order.add_edge(Pest_Monitor, Waste_Cycle)
root.order.add_edge(Waste_Cycle, Data_Capture)
root.order.add_edge(Data_Capture, Yield_Forecast)
root.order.add_edge(Yield_Forecast, Regulation_Check)
root.order.add_edge(Regulation_Check, Community_Meet)
root.order.add_edge(Community_Meet, Harvest_Prep)
root.order.add_edge(Harvest_Prep, Market_Link)

# Print the root of the POWL model
print(root)