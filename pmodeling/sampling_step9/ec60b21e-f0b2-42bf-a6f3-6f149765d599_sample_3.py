import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the POWL model
loop_site_survey = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, modular_design])
xor_system_build = OperatorPOWL(operator=Operator.XOR, children=[system_build, SilentTransition()])
loop_env_control = OperatorPOWL(operator=Operator.LOOP, children=[env_control, nutrient_mix])
xor_planting_setup = OperatorPOWL(operator=Operator.XOR, children=[planting_setup, growth_monitor])
loop_growth_monitor = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, pest_control])
xor_water_cycle = OperatorPOWL(operator=Operator.XOR, children=[water_cycle, data_capture])
loop_data_capture = OperatorPOWL(operator=Operator.LOOP, children=[data_capture, yield_forecast])
xor_yield_forecast = OperatorPOWL(operator=Operator.XOR, children=[yield_forecast, waste_reuse])
loop_waste_reuse = OperatorPOWL(operator=Operator.LOOP, children=[waste_reuse, stakeholder_meet])
xor_stakeholder_meet = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_meet, compliance_check])
loop_compliance_check = OperatorPOWL(operator=Operator.LOOP, children=[compliance_check, supply_sync])
xor_supply_sync = OperatorPOWL(operator=Operator.XOR, children=[supply_sync, SilentTransition()])

# Define the partial order
root = StrictPartialOrder(nodes=[loop_site_survey, xor_system_build, loop_env_control, xor_planting_setup, loop_growth_monitor, xor_water_cycle, loop_data_capture, xor_yield_forecast, loop_waste_reuse, xor_stakeholder_meet, loop_compliance_check, xor_supply_sync])
root.order.add_edge(loop_site_survey, xor_system_build)
root.order.add_edge(xor_system_build, loop_env_control)
root.order.add_edge(loop_env_control, xor_planting_setup)
root.order.add_edge(xor_planting_setup, loop_growth_monitor)
root.order.add_edge(loop_growth_monitor, xor_water_cycle)
root.order.add_edge(xor_water_cycle, loop_data_capture)
root.order.add_edge(loop_data_capture, xor_yield_forecast)
root.order.add_edge(xor_yield_forecast, loop_waste_reuse)
root.order.add_edge(loop_waste_reuse, xor_stakeholder_meet)
root.order.add_edge(xor_stakeholder_meet, loop_compliance_check)
root.order.add_edge(loop_compliance_check, xor_supply_sync)
root.order.add_edge(xor_supply_sync, loop_site_survey)

# Print the root
print(root)