import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
permit_acquire = Transition(label='Permit Acquire')
modular_build = Transition(label='Modular Build')
climate_setup = Transition(label='Climate Setup')
nutrient_mix = Transition(label='Nutrient Mix')
seed_automation = Transition(label='Seed Automation')
pest_control = Transition(label='Pest Control')
energy_audit = Transition(label='Energy Audit')
sensor_install = Transition(label='Sensor Install')
growth_monitor = Transition(label='Growth Monitor')
waste_process = Transition(label='Waste Process')
data_analysis = Transition(label='Data Analysis')
staff_train = Transition(label='Staff Train')
community_link = Transition(label='Community Link')
yield_report = Transition(label='Yield Report')

skip = SilentTransition()

# Define the workflow
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup, nutrient_mix, seed_automation])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, energy_audit, sensor_install])
loop_3 = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, waste_process, data_analysis])
loop_4 = OperatorPOWL(operator=Operator.LOOP, children=[staff_train, community_link, yield_report])

xor_1 = OperatorPOWL(operator=Operator.XOR, children=[permit_acquire, modular_build])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[site_survey, design_layout])

root = StrictPartialOrder(nodes=[xor_1, xor_2, loop_1, loop_2, loop_3, loop_4])
root.order.add_edge(xor_1, loop_1)
root.order.add_edge(xor_2, loop_2)
root.order.add_edge(loop_1, loop_3)
root.order.add_edge(loop_2, loop_4)

print(root)