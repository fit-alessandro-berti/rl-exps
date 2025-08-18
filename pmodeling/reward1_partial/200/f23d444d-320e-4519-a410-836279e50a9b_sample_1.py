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

# Define operators
site_survey_node = OperatorPOWL(operator=Operator.SITE_SURVEY, children=[site_survey, system_design])
system_design_node = OperatorPOWL(operator=Operator.SYSTEM_DESIGN, children=[module_build, nutrient_mix, seed_selection, planting_plan, irrigation_setup, climate_control, lighting_adjust, pest_monitor])
module_build_node = OperatorPOWL(operator=Operator.MODULE_BUILD, children=[waste_cycle, data_capture, yield_forecast, regulation_check, community_meet, harvest_prep, market_link])
nutrient_mix_node = OperatorPOWL(operator=Operator.NUTRIENT_MIX, children=[])
seed_selection_node = OperatorPOWL(operator=Operator.SEED_SELECTION, children=[])
planting_plan_node = OperatorPOWL(operator=Operator.PLANTING_PLAN, children=[])
irrigation_setup_node = OperatorPOWL(operator=Operator.IRRIGATION_SETUP, children=[])
climate_control_node = OperatorPOWL(operator=Operator.CLIMATE_CONTROL, children=[])
lighting_adjust_node = OperatorPOWL(operator=Operator.LIGHTING_ADJUST, children=[])
pest_monitor_node = OperatorPOWL(operator=Operator.PEST_MONITOR, children=[])
waste_cycle_node = OperatorPOWL(operator=Operator.WASTE_CYCLE, children=[])
data_capture_node = OperatorPOWL(operator=Operator.DATA_CAPTURE, children=[])
yield_forecast_node = OperatorPOWL(operator=Operator.YIELD_FORECAST, children=[])
regulation_check_node = OperatorPOWL(operator=Operator.REGULATION_CHECK, children=[])
community_meet_node = OperatorPOWL(operator=Operator.COMMUNITY_MEET, children=[])
harvest_prep_node = OperatorPOWL(operator=Operator.HARVEST_PREP, children=[])
market_link_node = OperatorPOWL(operator=Operator.MARKET_LINK, children=[])
silent_transition = SilentTransition()

# Create the partial order
root = StrictPartialOrder(nodes=[
    site_survey_node,
    system_design_node,
    module_build_node,
    nutrient_mix_node,
    seed_selection_node,
    planting_plan_node,
    irrigation_setup_node,
    climate_control_node,
    lighting_adjust_node,
    pest_monitor_node,
    waste_cycle_node,
    data_capture_node,
    yield_forecast_node,
    regulation_check_node,
    community_meet_node,
    harvest_prep_node,
    market_link_node
])

# Define dependencies
root.order.add_edge(site_survey_node, system_design_node)
root.order.add_edge(system_design_node, module_build_node)
root.order.add_edge(module_build_node, waste_cycle_node)
root.order.add_edge(waste_cycle_node, data_capture_node)
root.order.add_edge(data_capture_node, yield_forecast_node)
root.order.add_edge(yield_forecast_node, regulation_check_node)
root.order.add_edge(regulation_check_node, community_meet_node)
root.order.add_edge(community_meet_node, harvest_prep_node)
root.order.add_edge(harvest_prep_node, market_link_node)

print(root)