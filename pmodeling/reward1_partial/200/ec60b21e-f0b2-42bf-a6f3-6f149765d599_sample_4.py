import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
site_design_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, modular_design])
build_env_loop = OperatorPOWL(operator=Operator.LOOP, children=[system_build, env_control])
planting_loop = OperatorPOWL(operator=Operator.LOOP, children=[seed_selection, nutrient_mix, planting_setup])

# Define choice nodes
env_monitor_choice = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, skip])
pest_control_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, skip])
water_cycle_choice = OperatorPOWL(operator=Operator.XOR, children=[water_cycle, skip])

# Define partial order
root = StrictPartialOrder(nodes=[site_design_loop, build_env_loop, planting_loop, env_monitor_choice, pest_control_choice, water_cycle_choice, data_capture, yield_forecast, waste_reuse, stakeholder_meet, compliance_check, supply_sync])
root.order.add_edge(site_design_loop, build_env_loop)
root.order.add_edge(build_env_loop, planting_loop)
root.order.add_edge(planting_loop, env_monitor_choice)
root.order.add_edge(env_monitor_choice, pest_control_choice)
root.order.add_edge(pest_control_choice, water_cycle_choice)
root.order.add_edge(water_cycle_choice, data_capture)
root.order.add_edge(data_capture, yield_forecast)
root.order.add_edge(yield_forecast, waste_reuse)
root.order.add_edge(waste_reuse, stakeholder_meet)
root.order.add_edge(stakeholder_meet, compliance_check)
root.order.add_edge(compliance_check, supply_sync)