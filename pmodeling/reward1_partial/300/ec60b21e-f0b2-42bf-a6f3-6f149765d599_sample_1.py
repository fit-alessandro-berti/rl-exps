import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define loop nodes
env_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[env_control, nutrient_mix])
planting_loop = OperatorPOWL(operator=Operator.LOOP, children=[planting_setup, growth_monitor, pest_control])
water_cycle_loop = OperatorPOWL(operator=Operator.LOOP, children=[water_cycle, data_capture])

# Define XOR nodes
env_control_xor = OperatorPOWL(operator=Operator.XOR, children=[env_control_loop, nutrient_mix])
planting_xor = OperatorPOWL(operator=Operator.XOR, children=[planting_loop, growth_monitor, pest_control])
water_cycle_xor = OperatorPOWL(operator=Operator.XOR, children=[water_cycle_loop, data_capture])

# Define root
root = StrictPartialOrder(nodes=[site_survey, modular_design, system_build, env_control_xor, planting_xor, water_cycle_xor, yield_forecast, waste_reuse, stakeholder_meet, compliance_check, supply_sync])

# Define dependencies
root.order.add_edge(site_survey, modular_design)
root.order.add_edge(modular_design, system_build)
root.order.add_edge(system_build, env_control_xor)
root.order.add_edge(env_control_xor, planting_xor)
root.order.add_edge(planting_xor, water_cycle_xor)
root.order.add_edge(water_cycle_xor, yield_forecast)
root.order.add_edge(yield_forecast, waste_reuse)
root.order.add_edge(waste_reuse, stakeholder_meet)
root.order.add_edge(stakeholder_meet, compliance_check)
root.order.add_edge(compliance_check, supply_sync)

print(root)