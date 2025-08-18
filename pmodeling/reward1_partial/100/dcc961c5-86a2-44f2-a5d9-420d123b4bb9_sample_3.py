import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions for end nodes
yield_report_end = SilentTransition()
community_link_end = SilentTransition()

# Define loop for nutrient mix and seed automation
nutrient_mix_loop = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, seed_automation])

# Define XOR for pest control and energy audit
pest_control_xor = OperatorPOWL(operator=Operator.XOR, children=[pest_control, energy_audit])

# Define partial order for the entire process
root = StrictPartialOrder(nodes=[site_survey, design_layout, permit_acquire, modular_build, climate_setup, nutrient_mix_loop, pest_control_xor, sensor_install, growth_monitor, waste_process, data_analysis, staff_train, community_link_end, yield_report_end])

# Define the order between transitions
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, permit_acquire)
root.order.add_edge(permit_acquire, modular_build)
root.order.add_edge(modular_build, climate_setup)
root.order.add_edge(climate_setup, nutrient_mix_loop)
root.order.add_edge(nutrient_mix_loop, pest_control_xor)
root.order.add_edge(pest_control_xor, sensor_install)
root.order.add_edge(sensor_install, growth_monitor)
root.order.add_edge(growth_monitor, waste_process)
root.order.add_edge(waste_process, data_analysis)
root.order.add_edge(data_analysis, staff_train)
root.order.add_edge(staff_train, community_link_end)
root.order.add_edge(community_link_end, yield_report_end)