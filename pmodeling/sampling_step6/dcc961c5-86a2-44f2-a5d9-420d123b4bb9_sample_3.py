import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with exact names as given in the description
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

# Define the partial order for the workflow
root = StrictPartialOrder(nodes=[site_survey, design_layout, permit_acquire, modular_build, climate_setup, nutrient_mix, seed_automation, pest_control, energy_audit, sensor_install, growth_monitor, waste_process, data_analysis, staff_train, community_link, yield_report])

# Note: The dependencies between activities are not explicitly defined in the POWL model above.
# In a real-world scenario, you would need to define the order of execution explicitly based on the process flow.
# For example, the order might be as follows:
# root.order.add_edge(site_survey, design_layout)
# root.order.add_edge(site_survey, permit_acquire)
# root.order.add_edge(site_survey, modular_build)
# ...
# This would ensure that the activities are executed in the correct sequence.