import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the control flow operators
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[regulation_check, community_meet])
inclusive_choice = OperatorPOWL(operator=Operator.OR, children=[seed_selection, planting_plan])
loop = OperatorPOWL(operator=Operator.LOOP, children=[irrigation_setup, climate_control, lighting_adjust, pest_monitor, waste_cycle])
partial_order = StrictPartialOrder(nodes=[site_survey, system_design, module_build, nutrient_mix, inclusive_choice, data_capture, yield_forecast, exclusive_choice, loop, market_link])

# Define the dependencies between transitions
partial_order.order.add_edge(site_survey, system_design)
partial_order.order.add_edge(system_design, module_build)
partial_order.order.add_edge(module_build, nutrient_mix)
partial_order.order.add_edge(nutrient_mix, inclusive_choice)
partial_order.order.add_edge(inclusive_choice, data_capture)
partial_order.order.add_edge(data_capture, yield_forecast)
partial_order.order.add_edge(yield_forecast, exclusive_choice)
partial_order.order.add_edge(exclusive_choice, market_link)
partial_order.order.add_edge(market_link, loop)
partial_order.order.add_edge(loop, module_build)

# Assign the root node
root = partial_order