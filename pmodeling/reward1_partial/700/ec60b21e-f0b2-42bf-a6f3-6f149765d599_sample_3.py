import pm4py
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

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[env_control, nutrient_mix, planting_setup, growth_monitor, pest_control, water_cycle, data_capture])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[yield_forecast, waste_reuse])
xor = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_meet, compliance_check, supply_sync])

root = StrictPartialOrder(nodes=[site_survey, modular_design, system_build, loop1, loop2, xor])
root.order.add_edge(site_survey, modular_design)
root.order.add_edge(modular_design, system_build)
root.order.add_edge(system_build, loop1)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, xor)