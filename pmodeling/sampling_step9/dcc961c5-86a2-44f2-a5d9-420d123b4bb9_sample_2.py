import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
climate_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup, nutrient_mix])
pest_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, energy_audit])
waste_process_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_process, sensor_install])
growth_monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, data_analysis])
staff_train_loop = OperatorPOWL(operator=Operator.LOOP, children=[staff_train, community_link])

# Define exclusive choices
exclusive_choice_1 = OperatorPOWL(operator=Operator.XOR, children=[yield_report, skip])
exclusive_choice_2 = OperatorPOWL(operator=Operator.XOR, children=[skip, skip])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[site_survey, design_layout, permit_acquire, modular_build, climate_loop, pest_control_loop, waste_process_loop, growth_monitor_loop, staff_train_loop, exclusive_choice_1, exclusive_choice_2])

# Add dependencies
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, permit_acquire)
root.order.add_edge(permit_acquire, modular_build)
root.order.add_edge(modular_build, climate_loop)
root.order.add_edge(climate_loop, pest_control_loop)
root.order.add_edge(pest_control_loop, waste_process_loop)
root.order.add_edge(waste_process_loop, growth_monitor_loop)
root.order.add_edge(growth_monitor_loop, staff_train_loop)
root.order.add_edge(staff_train_loop, exclusive_choice_1)
root.order.add_edge(exclusive_choice_1, exclusive_choice_2)
root.order.add_edge(exclusive_choice_2, yield_report)

# Print the root of the POWL model
print(root)