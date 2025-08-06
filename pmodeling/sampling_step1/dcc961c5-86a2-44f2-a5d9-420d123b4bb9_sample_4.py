import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the loop nodes
climate_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup, nutrient_mix])
seed_loop = OperatorPOWL(operator=Operator.LOOP, children=[seed_automation, pest_control])
energy_loop = OperatorPOWL(operator=Operator.LOOP, children=[energy_audit, sensor_install, growth_monitor, waste_process, data_analysis])
staff_loop = OperatorPOWL(operator=Operator.LOOP, children=[staff_train, community_link, yield_report])

# Define the root POWL model
root = StrictPartialOrder(nodes=[site_survey, design_layout, permit_acquire, modular_build, climate_loop, seed_loop, energy_loop, staff_loop])
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, permit_acquire)
root.order.add_edge(permit_acquire, modular_build)
root.order.add_edge(modular_build, climate_loop)
root.order.add_edge(climate_loop, seed_loop)
root.order.add_edge(seed_loop, energy_loop)
root.order.add_edge(energy_loop, staff_loop)
root.order.add_edge(staff_loop, community_link)
root.order.add_edge(community_link, yield_report)

print(root)