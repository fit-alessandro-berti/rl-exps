import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) as POWL models
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

# Define the silent transitions
skip = SilentTransition()

# Define the loop nodes
loop_site_survey = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, modular_design])
loop_system_build = OperatorPOWL(operator=Operator.LOOP, children=[system_build, env_control])
loop_nutrient_mix = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, planting_setup])
loop_growth_monitor = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, pest_control])
loop_water_cycle = OperatorPOWL(operator=Operator.LOOP, children=[water_cycle, data_capture])
loop_yield_forecast = OperatorPOWL(operator=Operator.LOOP, children=[yield_forecast, waste_reuse])
loop_compliance_check = OperatorPOWL(operator=Operator.LOOP, children=[compliance_check, supply_sync])

# Define the exclusive choice nodes
xor_site_survey = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_site_survey])
xor_system_build = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_system_build])
xor_nutrient_mix = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_nutrient_mix])
xor_growth_monitor = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_growth_monitor])
xor_water_cycle = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_water_cycle])
xor_yield_forecast = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_yield_forecast])
xor_compliance_check = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_compliance_check])

# Define the root POWL model
root = StrictPartialOrder(nodes=[xor_site_survey, xor_system_build, xor_nutrient_mix, xor_growth_monitor, xor_water_cycle, xor_yield_forecast, xor_compliance_check])
root.order.add_edge(xor_site_survey, xor_system_build)
root.order.add_edge(xor_system_build, xor_nutrient_mix)
root.order.add_edge(xor_nutrient_mix, xor_growth_monitor)
root.order.add_edge(xor_growth_monitor, xor_water_cycle)
root.order.add_edge(xor_water_cycle, xor_yield_forecast)
root.order.add_edge(xor_yield_forecast, xor_compliance_check)