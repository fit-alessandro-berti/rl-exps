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

# Define the root of the POWL model as a strict partial order
root = StrictPartialOrder(nodes=[site_survey, design_layout, permit_acquire, modular_build, climate_setup, nutrient_mix, seed_automation, pest_control, energy_audit, sensor_install, growth_monitor, waste_process, data_analysis, staff_train, community_link, yield_report])

# Define dependencies between activities (example dependencies for demonstration purposes)
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(site_survey, permit_acquire)
root.order.add_edge(design_layout, modular_build)
root.order.add_edge(design_layout, climate_setup)
root.order.add_edge(design_layout, nutrient_mix)
root.order.add_edge(design_layout, seed_automation)
root.order.add_edge(climate_setup, pest_control)
root.order.add_edge(nutrient_mix, pest_control)
root.order.add_edge(nutrient_mix, energy_audit)
root.order.add_edge(nutrient_mix, sensor_install)
root.order.add_edge(growth_monitor, data_analysis)
root.order.add_edge(data_analysis, staff_train)
root.order.add_edge(data_analysis, community_link)
root.order.add_edge(data_analysis, yield_report)

# Print the root of the POWL model
print(root)