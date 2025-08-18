import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Seed_Select = Transition(label='Seed Select')
Climate_Map = Transition(label='Climate Map')
IoT_Setup = Transition(label='IoT Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
Sensor_Check = Transition(label='Sensor Check')
Light_Adjust = Transition(label='Light Adjust')
Water_Cycle = Transition(label='Water Cycle')
Pest_Scan = Transition(label='Pest Scan')
Growth_Audit = Transition(label='Growth Audit')
Harvest_Plan = Transition(label='Harvest Plan')
Demand_Sync = Transition(label='Demand Sync')
Quality_Grade = Transition(label='Quality Grade')
Pack_Items = Transition(label='Pack Items')
Waste_Compost = Transition(label='Waste Compost')
Data_Review = Transition(label='Data Review')
Cycle_Reset = Transition(label='Cycle Reset')

# Define the partial order graph
root = StrictPartialOrder(
    nodes=[Seed_Select, Climate_Map, IoT_Setup, Nutrient_Mix, Sensor_Check, Light_Adjust, Water_Cycle, Pest_Scan,
           Growth_Audit, Harvest_Plan, Demand_Sync, Quality_Grade, Pack_Items, Waste_Compost, Data_Review, Cycle_Reset]
)

# Define the order edges
root.order.add_edge(Seed_Select, Climate_Map)
root.order.add_edge(Climate_Map, IoT_Setup)
root.order.add_edge(IoT_Setup, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, Sensor_Check)
root.order.add_edge(Sensor_Check, Light_Adjust)
root.order.add_edge(Light_Adjust, Water_Cycle)
root.order.add_edge(Water_Cycle, Pest_Scan)
root.order.add_edge(Pest_Scan, Growth_Audit)
root.order.add_edge(Growth_Audit, Harvest_Plan)
root.order.add_edge(Harvest_Plan, Demand_Sync)
root.order.add_edge(Demand_Sync, Quality_Grade)
root.order.add_edge(Quality_Grade, Pack_Items)
root.order.add_edge(Pack_Items, Waste_Compost)
root.order.add_edge(Waste_Compost, Data_Review)
root.order.add_edge(Data_Review, Cycle_Reset)
root.order.add_edge(Cycle_Reset, Seed_Select)  # Cycle Reset back to Seed Select

# Print the root POWL model
print(root)