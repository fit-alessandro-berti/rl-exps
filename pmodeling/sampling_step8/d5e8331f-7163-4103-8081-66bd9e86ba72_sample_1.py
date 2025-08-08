import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_prep = Transition(label='Site Prep')
seed_select = Transition(label='Seed Select')
nutrient_mix = Transition(label='Nutrient Mix')
plant_rows = Transition(label='Planting Rows')
env_monitor = Transition(label='Env Monitor')
water_adjust = Transition(label='Water Adjust')
pest_control = Transition(label='Pest Control')
growth_check = Transition(label='Growth Check')
light_calibrate = Transition(label='Light Calibrate')
energy_manage = Transition(label='Energy Manage')
harvest_crop = Transition(label='Harvest Crop')
quality_sort = Transition(label='Quality Sort')
pack_goods = Transition(label='Pack Goods')
cold_store = Transition(label='Cold Store')
market_ship = Transition(label='Market Ship')
data_analyze = Transition(label='Data Analyze')

# Define a loop for the main production cycle
production_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    site_prep, seed_select, nutrient_mix, plant_rows, env_monitor, water_adjust, pest_control, growth_check, light_calibrate, energy_manage, harvest_crop
])

# Define a partial order for post-harvest activities
post_harvest = OperatorPOWL(operator=Operator.PARTIAL_ORDER, children=[
    quality_sort, pack_goods, cold_store, market_ship
])

# Define a loop for the data feedback loop
data_feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    data_analyze
])

# Define the root POWL model
root = StrictPartialOrder(nodes=[production_loop, post_harvest, data_feedback_loop])
root.order.add_edge(production_loop, post_harvest)
root.order.add_edge(post_harvest, data_feedback_loop)

print(root)