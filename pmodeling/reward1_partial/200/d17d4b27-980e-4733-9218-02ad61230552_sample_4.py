import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Site_Analysis = Transition(label='Site Analysis')
Zoning_Review = Transition(label='Zoning Review')
Modular_Design = Transition(label='Modular Design')
Climate_Setup = Transition(label='Climate Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
Seed_Selection = Transition(label='Seed Selection')
AI_Monitoring = Transition(label='AI Monitoring')
Lighting_Control = Transition(label='Lighting Control')
Energy_Audit = Transition(label='Energy Audit')
Water_Reclaim = Transition(label='Water Reclaim')
Waste_Sorting = Transition(label='Waste Sorting')
Community_Meet = Transition(label='Community Meet')
Staff_Training = Transition(label='Staff Training')
Yield_Forecast = Transition(label='Yield Forecast')
Market_Sync = Transition(label='Market Sync')
Supply_Chain = Transition(label='Supply Chain')

# Define silent transitions
skip = SilentTransition()

# Define exclusive choice for AI Monitoring and Lighting Control
xor1 = OperatorPOWL(operator=Operator.XOR, children=[AI_Monitoring, Lighting_Control])

# Define exclusive choice for Energy Audit and Water Reclaim
xor2 = OperatorPOWL(operator=Operator.XOR, children=[Energy_Audit, Water_Reclaim])

# Define exclusive choice for Waste Sorting and Community Meet
xor3 = OperatorPOWL(operator=Operator.XOR, children=[Waste_Sorting, Community_Meet])

# Define exclusive choice for Staff Training and Yield Forecast
xor4 = OperatorPOWL(operator=Operator.XOR, children=[Staff_Training, Yield_Forecast])

# Define exclusive choice for Market Sync and Supply Chain
xor5 = OperatorPOWL(operator=Operator.XOR, children=[Market_Sync, Supply_Chain])

# Define the root process
root = StrictPartialOrder(nodes=[
    Site_Analysis, 
    Zoning_Review, 
    Modular_Design, 
    Climate_Setup, 
    Nutrient_Mix, 
    Seed_Selection, 
    xor1, 
    xor2, 
    xor3, 
    xor4, 
    xor5
])

# Define the order of dependencies
root.order.add_edge(Site_Analysis, Zoning_Review)
root.order.add_edge(Zoning_Review, Modular_Design)
root.order.add_edge(Modular_Design, Climate_Setup)
root.order.add_edge(Climate_Setup, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, Seed_Selection)
root.order.add_edge(Seed_Selection, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)