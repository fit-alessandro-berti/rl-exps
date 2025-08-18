import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
seed_select = Transition(label='Seed Select')
nutrient_mix = Transition(label='Nutrient Mix')
climate_setup = Transition(label='Climate Setup')
light_adjust = Transition(label='Light Adjust')
co2_control = Transition(label='CO2 Control')
humidity_tune = Transition(label='Humidity Tune')
growth_monitor = Transition(label='Growth Monitor')
pest_detect = Transition(label='Pest Detect')
harvest_plan = Transition(label='Harvest Plan')
produce_sort = Transition(label='Produce Sort')
pack_biodeg = Transition(label='Pack Biodeg')
drone_dispatch = Transition(label='Drone Dispatch')
waste_recycle = Transition(label='Waste Recycle')
compost_create = Transition(label='Compost Create')
cycle_review = Transition(label='Cycle Review')

# Define the control flow
seed_select_to_nutrient_mix = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, nutrient_mix])
nutrient_mix_to_climate_setup = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, nutrient_mix])
climate_setup_to_light_adjust = OperatorPOWL(operator=Operator.XOR, children=[light_adjust, co2_control, humidity_tune])
light_adjust_to_co2_control = OperatorPOWL(operator=Operator.XOR, children=[co2_control, humidity_tune])
co2_control_to_humidity_tune = OperatorPOWL(operator=Operator.XOR, children=[humidity_tune, light_adjust])
humidity_tune_to_growth_monitor = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, pest_detect])
growth_monitor_to_harvest_plan = OperatorPOWL(operator=Operator.XOR, children=[harvest_plan, produce_sort])
pest_detect_to_produce_sort = OperatorPOWL(operator=Operator.XOR, children=[produce_sort, harvest_plan])
harvest_plan_to_drone_dispatch = OperatorPOWL(operator=Operator.XOR, children=[drone_dispatch, waste_recycle])
produce_sort_to_waste_recycle = OperatorPOWL(operator=Operator.XOR, children=[waste_recycle, compost_create])
waste_recycle_to_compost_create = OperatorPOWL(operator=Operator.XOR, children=[compost_create, drone_dispatch])
compost_create_to_cycle_review = OperatorPOWL(operator=Operator.XOR, children=[cycle_review, seed_select])

# Create the root of the POWL model
root = StrictPartialOrder(nodes=[seed_select_to_nutrient_mix, nutrient_mix_to_climate_setup, climate_setup_to_light_adjust, light_adjust_to_co2_control, co2_control_to_humidity_tune, humidity_tune_to_growth_monitor, growth_monitor_to_harvest_plan, pest_detect_to_produce_sort, harvest_plan_to_drone_dispatch, produce_sort_to_waste_recycle, waste_recycle_to_compost_create, compost_create_to_cycle_review])