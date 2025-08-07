import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a Transition
site_prep = Transition(label='Site Prep')
seed_select = Transition(label='Seed Select')
nutrient_mix = Transition(label='Nutrient Mix')
planting_rows = Transition(label='Planting Rows')
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    site_prep,
    seed_select,
    nutrient_mix,
    planting_rows,
    env_monitor,
    water_adjust,
    pest_control,
    growth_check,
    light_calibrate,
    energy_manage,
    harvest_crop,
    quality_sort,
    pack_goods,
    cold_store,
    market_ship,
    data_analyze
])

# Define dependencies if any (in this case, all activities are concurrent)
# No dependencies defined in the problem statement, so we don't need to add any edges.

print(root)