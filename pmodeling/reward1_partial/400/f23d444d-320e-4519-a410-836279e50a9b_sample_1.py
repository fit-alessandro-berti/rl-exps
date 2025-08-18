import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define exclusive choice between nutrient mix and seed selection
nutrient_mix_or_seed_selection = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, seed_selection])

# Define loop for planting plan, irrigation setup, climate control, lighting adjust, pest monitor, and waste cycle
planting_plan_loop = OperatorPOWL(operator=Operator.LOOP, children=[planting_plan, irrigation_setup, climate_control, lighting_adjust, pest_monitor, waste_cycle])

# Define exclusive choice between yield forecast and regulation check
yield_forecast_or_regulation_check = OperatorPOWL(operator=Operator.XOR, children=[yield_forecast, regulation_check])

# Define exclusive choice between community meet and market link
community_meet_or_market_link = OperatorPOWL(operator=Operator.XOR, children=[community_meet, market_link])

# Define root node with all activities
root = StrictPartialOrder(nodes=[site_survey, system_design, module_build, nutrient_mix_or_seed_selection, planting_plan_loop, yield_forecast_or_regulation_check, community_meet_or_market_link])
root.order.add_edge(site_survey, system_design)
root.order.add_edge(system_design, module_build)
root.order.add_edge(module_build, nutrient_mix_or_seed_selection)
root.order.add_edge(nutrient_mix_or_seed_selection, planting_plan_loop)
root.order.add_edge(planting_plan_loop, yield_forecast_or_regulation_check)
root.order.add_edge(yield_forecast_or_regulation_check, community_meet_or_market_link)