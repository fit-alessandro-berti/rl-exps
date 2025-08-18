import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

site_survey_choice = OperatorPOWL(operator=Operator.XOR, children=[site_survey, skip])
system_design_choice = OperatorPOWL(operator=Operator.XOR, children=[system_design, skip])
module_build_choice = OperatorPOWL(operator=Operator.XOR, children=[module_build, skip])
nutrient_mix_choice = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, skip])
seed_selection_choice = OperatorPOWL(operator=Operator.XOR, children=[seed_selection, skip])
planting_plan_choice = OperatorPOWL(operator=Operator.XOR, children=[planting_plan, skip])
irrigation_setup_choice = OperatorPOWL(operator=Operator.XOR, children=[irrigation_setup, skip])
climate_control_choice = OperatorPOWL(operator=Operator.XOR, children=[climate_control, skip])
lighting_adjust_choice = OperatorPOWL(operator=Operator.XOR, children=[lighting_adjust, skip])
pest_monitor_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_monitor, skip])
waste_cycle_choice = OperatorPOWL(operator=Operator.XOR, children=[waste_cycle, skip])
data_capture_choice = OperatorPOWL(operator=Operator.XOR, children=[data_capture, skip])
yield_forecast_choice = OperatorPOWL(operator=Operator.XOR, children=[yield_forecast, skip])
regulation_check_choice = OperatorPOWL(operator=Operator.XOR, children=[regulation_check, skip])
community_meet_choice = OperatorPOWL(operator=Operator.XOR, children=[community_meet, skip])
harvest_prep_choice = OperatorPOWL(operator=Operator.XOR, children=[harvest_prep, skip])
market_link_choice = OperatorPOWL(operator=Operator.XOR, children=[market_link, skip])

root = StrictPartialOrder(nodes=[
    site_survey_choice,
    system_design_choice,
    module_build_choice,
    nutrient_mix_choice,
    seed_selection_choice,
    planting_plan_choice,
    irrigation_setup_choice,
    climate_control_choice,
    lighting_adjust_choice,
    pest_monitor_choice,
    waste_cycle_choice,
    data_capture_choice,
    yield_forecast_choice,
    regulation_check_choice,
    community_meet_choice,
    harvest_prep_choice,
    market_link_choice
])
root.order.add_edge(site_survey_choice, system_design_choice)
root.order.add_edge(system_design_choice, module_build_choice)
root.order.add_edge(module_build_choice, nutrient_mix_choice)
root.order.add_edge(nutrient_mix_choice, seed_selection_choice)
root.order.add_edge(seed_selection_choice, planting_plan_choice)
root.order.add_edge(planting_plan_choice, irrigation_setup_choice)
root.order.add_edge(irrigation_setup_choice, climate_control_choice)
root.order.add_edge(climate_control_choice, lighting_adjust_choice)
root.order.add_edge(lighting_adjust_choice, pest_monitor_choice)
root.order.add_edge(pest_monitor_choice, waste_cycle_choice)
root.order.add_edge(waste_cycle_choice, data_capture_choice)
root.order.add_edge(data_capture_choice, yield_forecast_choice)
root.order.add_edge(yield_forecast_choice, regulation_check_choice)
root.order.add_edge(regulation_check_choice, community_meet_choice)
root.order.add_edge(community_meet_choice, harvest_prep_choice)
root.order.add_edge(harvest_prep_choice, market_link_choice)