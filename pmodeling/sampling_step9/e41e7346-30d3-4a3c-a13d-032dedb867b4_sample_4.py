import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
Seed_Select = Transition(label='Seed Select')
Nutrient_Mix = Transition(label='Nutrient Mix')
Climate_Setup = Transition(label='Climate Setup')
Light_Adjust = Transition(label='Light Adjust')
CO2_Control = Transition(label='CO2 Control')
Humidity_Tune = Transition(label='Humidity Tune')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Detect = Transition(label='Pest Detect')
Harvest_Plan = Transition(label='Harvest Plan')
Produce_Sort = Transition(label='Produce Sort')
Pack_Biodeg = Transition(label='Pack Biodeg')
Drone_Dispatch = Transition(label='Drone Dispatch')
Waste_Recycle = Transition(label='Waste Recycle')
Compost_Create = Transition(label='Compost Create')
Cycle_Review = Transition(label='Cycle Review')

# Define silent transitions
skip = SilentTransition()

# Define loops and choices
climate_loop = OperatorPOWL(operator=Operator.LOOP, children=[Climate_Setup, Light_Adjust, CO2_Control, Humidity_Tune])
light_loop = OperatorPOWL(operator=Operator.LOOP, children=[Light_Adjust, CO2_Control, Humidity_Tune])
pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[Pest_Detect])
growth_monitor = OperatorPOWL(operator=Operator.XOR, children=[Growth_Monitor, pest_loop])
harvest_plan = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, growth_monitor])
produce_sort = OperatorPOWL(operator=Operator.XOR, children=[Produce_Sort, skip])
pack_biodeg = OperatorPOWL(operator=Operator.XOR, children=[Pack_Biodeg, skip])
drone_dispatch = OperatorPOWL(operator=Operator.XOR, children=[Drone_Dispatch, skip])
waste_recycle = OperatorPOWL(operator=Operator.XOR, children=[Waste_Recycle, skip])
compost_create = OperatorPOWL(operator=Operator.XOR, children=[Compost_Create, skip])
cycle_review = OperatorPOWL(operator=Operator.XOR, children=[Cycle_Review, skip])

# Define the root model
root = StrictPartialOrder(nodes=[Seed_Select, Nutrient_Mix, climate_loop, light_loop, pest_loop, growth_monitor, harvest_plan, produce_sort, pack_biodeg, drone_dispatch, waste_recycle, compost_create, cycle_review])
root.order.add_edge(Seed_Select, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, climate_loop)
root.order.add_edge(climate_loop, light_loop)
root.order.add_edge(light_loop, pest_loop)
root.order.add_edge(pest_loop, growth_monitor)
root.order.add_edge(growth_monitor, harvest_plan)
root.order.add_edge(harvest_plan, produce_sort)
root.order.add_edge(produce_sort, pack_biodeg)
root.order.add_edge(pack_biodeg, drone_dispatch)
root.order.add_edge(drone_dispatch, waste_recycle)
root.order.add_edge(waste_recycle, compost_create)
root.order.add_edge(compost_create, cycle_review)
root.order.add_edge(cycle_review, Seed_Select)