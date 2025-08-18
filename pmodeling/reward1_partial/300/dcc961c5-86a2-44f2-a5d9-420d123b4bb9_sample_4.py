from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the control-flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[site_survey, design_layout])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[permit_acquire, modular_build])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, nutrient_mix])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[seed_automation, pest_control])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[energy_audit, sensor_install])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, waste_process])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[data_analysis, staff_train])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[community_link, yield_report])

# Define the partial order
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)

# Return the root of the POWL model
return root