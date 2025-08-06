import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey = Transition(label='Site Survey')
system_design = Transition(label='System Design')
module_build = Transition(label='Module Build')
nutrient_mix = Transition(label='Nutrient Mix')
seed_selection = Transition(label='Seed Selection')
planting_plan = Transition(label='Planting Plan')
irrigation_setup = Transition(label='Irrigation Setup')
climate_control = Transition(label='Climate Control')
lighting_adjust = Transition(label='Lighting Adjust')
pest_monitor = Transition(label='Pest Monitor')
waste_cycle = Transition(label='Waste Cycle')
data_capture = Transition(label='Data Capture')
yield_forecast = Transition(label='Yield Forecast')
regulation_check = Transition(label='Regulation Check')
community_meet = Transition(label='Community Meet')
harvest_prep = Transition(label='Harvest Prep')
market_link = Transition(label='Market Link')

# Define choices and loops
site_evaluation = OperatorPOWL(operator=Operator.XOR, children=[site_survey, system_design])
module_build_loop = OperatorPOWL(operator=Operator.LOOP, children=[module_build, nutrient_mix])
seed_selection_loop = OperatorPOWL(operator=Operator.LOOP, children=[seed_selection, planting_plan])
irrigation_setup_loop = OperatorPOWL(operator=Operator.LOOP, children=[irrigation_setup, climate_control])
lighting_adjust_loop = OperatorPOWL(operator=Operator.LOOP, children=[lighting_adjust, pest_monitor])
waste_cycle_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_cycle, data_capture])
yield_forecast_loop = OperatorPOWL(operator=Operator.LOOP, children=[yield_forecast, regulation_check])
community_meet_loop = OperatorPOWL(operator=Operator.LOOP, children=[community_meet, market_link])

# Define partial order
root = StrictPartialOrder(nodes=[site_evaluation, module_build_loop, seed_selection_loop, irrigation_setup_loop, lighting_adjust_loop, waste_cycle_loop, yield_forecast_loop, community_meet_loop])
root.order.add_edge(site_evaluation, module_build_loop)
root.order.add_edge(site_evaluation, seed_selection_loop)
root.order.add_edge(module_build_loop, irrigation_setup_loop)
root.order.add_edge(module_build_loop, lighting_adjust_loop)
root.order.add_edge(seed_selection_loop, waste_cycle_loop)
root.order.add_edge(seed_selection_loop, yield_forecast_loop)
root.order.add_edge(irrigation_setup_loop, community_meet_loop)