import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities) with exact names
Site_Prep = Transition(label='Site Prep')
Seed_Select = Transition(label='Seed Select')
Nutrient_Mix = Transition(label='Nutrient Mix')
Planting_Rows = Transition(label='Planting Rows')
Env_Monitor = Transition(label='Env Monitor')
Water_Adjust = Transition(label='Water Adjust')
Pest_Control = Transition(label='Pest Control')
Growth_Check = Transition(label='Growth Check')
Light_Calibrate = Transition(label='Light Calibrate')
Energy_Manage = Transition(label='Energy Manage')
Harvest_Crop = Transition(label='Harvest Crop')
Quality_Sort = Transition(label='Quality Sort')
Pack_Goods = Transition(label='Pack Goods')
Cold_Store = Transition(label='Cold Store')
Market_Ship = Transition(label='Market Ship')
Data_Analyze = Transition(label='Data Analyze')

# Define a partial order (StrictPartialOrder) with the defined activities
root = StrictPartialOrder(nodes=[
    Site_Prep, Seed_Select, Nutrient_Mix, Planting_Rows, Env_Monitor, Water_Adjust, Pest_Control, Growth_Check, Light_Calibrate, Energy_Manage, Harvest_Crop, Quality_Sort, Pack_Goods, Cold_Store, Market_Ship, Data_Analyze
])

# Define dependencies (order) between activities
root.order.add_edge(Site_Prep, Seed_Select)
root.order.add_edge(Seed_Select, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, Planting_Rows)
root.order.add_edge(Planting_Rows, Env_Monitor)
root.order.add_edge(Env_Monitor, Water_Adjust)
root.order.add_edge(Water_Adjust, Pest_Control)
root.order.add_edge(Pest_Control, Growth_Check)
root.order.add_edge(Growth_Check, Light_Calibrate)
root.order.add_edge(Light_Calibrate, Energy_Manage)
root.order.add_edge(Energy_Manage, Harvest_Crop)
root.order.add_edge(Harvest_Crop, Quality_Sort)
root.order.add_edge(Quality_Sort, Pack_Goods)
root.order.add_edge(Pack_Goods, Cold_Store)
root.order.add_edge(Cold_Store, Market_Ship)
root.order.add_edge(Market_Ship, Data_Analyze)

print(root)