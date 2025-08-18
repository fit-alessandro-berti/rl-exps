from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_survey = Transition(label='Site Survey')
modular_design = Transition(label='Modular Design')
system_build = Transition(label='System Build')
env_control = Transition(label='Env Control')
seed_selection = Transition(label='Seed Selection')
nutrient_mix = Transition(label='Nutrient Mix')
planting_setup = Transition(label='Planting Setup')
growth_monitor = Transition(label='Growth Monitor')
pest_control = Transition(label='Pest Control')
water_cycle = Transition(label='Water Cycle')
data_capture = Transition(label='Data Capture')
yield_forecast = Transition(label='Yield Forecast')
waste_reuse = Transition(label='Waste Reuse')
stakeholder_meet = Transition(label='Stakeholder Meet')
compliance_check = Transition(label='Compliance Check')
supply_sync = Transition(label='Supply Sync')

site_survey_node = OperatorPOWL(operator=Operator.SITE, children=[site_survey])
modular_design_node = OperatorPOWL(operator=Operator.MODULAR, children=[modular_design])
system_build_node = OperatorPOWL(operator=Operator.BUILD, children=[system_build])
env_control_node = OperatorPOWL(operator=Operator.CONTROL, children=[env_control])
seed_selection_node = OperatorPOWL(operator=Operator.SEED, children=[seed_selection])
nutrient_mix_node = OperatorPOWL(operator=Operator.MIX, children=[nutrient_mix])
planting_setup_node = OperatorPOWL(operator=Operator.SETUP, children=[planting_setup])
growth_monitor_node = OperatorPOWL(operator=Operator.MONITOR, children=[growth_monitor])
pest_control_node = OperatorPOWL(operator=Operator.CONTROL, children=[pest_control])
water_cycle_node = OperatorPOWL(operator=Operator.CYCLE, children=[water_cycle])
data_capture_node = OperatorPOWL(operator=Operator.DATA, children=[data_capture])
yield_forecast_node = OperatorPOWL(operator=Operator.FORECAST, children=[yield_forecast])
waste_reuse_node = OperatorPOWL(operator=Operator.REUSE, children=[waste_reuse])
stakeholder_meet_node = OperatorPOWL(operator=Operator.MEET, children=[stakeholder_meet])
compliance_check_node = OperatorPOWL(operator=Operator.CHECK, children=[compliance_check])
supply_sync_node = OperatorPOWL(operator=Operator.SYNC, children=[supply_sync])

root = StrictPartialOrder(nodes=[
    site_survey_node,
    modular_design_node,
    system_build_node,
    env_control_node,
    seed_selection_node,
    nutrient_mix_node,
    planting_setup_node,
    growth_monitor_node,
    pest_control_node,
    water_cycle_node,
    data_capture_node,
    yield_forecast_node,
    waste_reuse_node,
    stakeholder_meet_node,
    compliance_check_node,
    supply_sync_node
])

root.order.add_edge(site_survey_node, modular_design_node)
root.order.add_edge(modular_design_node, system_build_node)
root.order.add_edge(system_build_node, env_control_node)
root.order.add_edge(env_control_node, seed_selection_node)
root.order.add_edge(seed_selection_node, nutrient_mix_node)
root.order.add_edge(nutrient_mix_node, planting_setup_node)
root.order.add_edge(planting_setup_node, growth_monitor_node)
root.order.add_edge(growth_monitor_node, pest_control_node)
root.order.add_edge(pest_control_node, water_cycle_node)
root.order.add_edge(water_cycle_node, data_capture_node)
root.order.add_edge(data_capture_node, yield_forecast_node)
root.order.add_edge(yield_forecast_node, waste_reuse_node)
root.order.add_edge(waste_reuse_node, stakeholder_meet_node)
root.order.add_edge(stakeholder_meet_node, compliance_check_node)
root.order.add_edge(compliance_check_node, supply_sync_node)