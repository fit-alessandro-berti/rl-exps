import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey     = Transition(label='Site Survey')
design_layout   = Transition(label='Design Layout')
permit_acquire  = Transition(label='Permit Acquire')
modular_build   = Transition(label='Modular Build')
climate_setup   = Transition(label='Climate Setup')
nutrient_mix    = Transition(label='Nutrient Mix')
seed_automation = Transition(label='Seed Automation')
pest_control    = Transition(label='Pest Control')
energy_audit    = Transition(label='Energy Audit')
sensor_install  = Transition(label='Sensor Install')
growth_monitor  = Transition(label='Growth Monitor')
waste_process   = Transition(label='Waste Process')
data_analysis   = Transition(label='Data Analysis')
staff_train     = Transition(label='Staff Train')
community_link  = Transition(label='Community Link')
yield_report    = Transition(label='Yield Report')

# Define the main production cycle as a partial order
cycle = StrictPartialOrder(nodes=[
    seed_automation, pest_control, climate_setup, nutrient_mix,
    sensor_install, growth_monitor, data_analysis, waste_process
])
cycle.order.add_edge(seed_automation, pest_control)
cycle.order.add_edge(pest_control, climate_setup)
cycle.order.add_edge(climate_setup, nutrient_mix)
cycle.order.add_edge(nutrient_mix, sensor_install)
cycle.order.add_edge(sensor_install, growth_monitor)
cycle.order.add_edge(growth_monitor, data_analysis)
cycle.order.add_edge(data_analysis, waste_process)

# Define the loop: repeat the production cycle until exit
# (the loop body is the cycle itself, and exit is represented by a silent transition)
skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[cycle, skip])

# Assemble the overall process as a strict partial order
root = StrictPartialOrder(nodes=[
    site_survey, design_layout, permit_acquire, modular_build,
    loop, energy_audit, staff_train, community_link, yield_report
])
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, permit_acquire)
root.order.add_edge(permit_acquire, modular_build)
root.order.add_edge(modular_build, loop)
root.order.add_edge(loop, energy_audit)
root.order.add_edge(energy_audit, staff_train)
root.order.add_edge(staff_train, community_link)
root.order.add_edge(community_link, yield_report)