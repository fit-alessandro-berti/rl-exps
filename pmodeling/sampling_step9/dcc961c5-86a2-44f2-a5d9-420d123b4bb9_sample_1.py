import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
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

# Define silent transitions (no label)
skip = SilentTransition()

# Define POWL model
loop_site_survey = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, permit_acquire])
loop_design = OperatorPOWL(operator=Operator.LOOP, children=[design_layout, modular_build])
loop_climate = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup, nutrient_mix])
loop_seed = OperatorPOWL(operator=Operator.LOOP, children=[seed_automation, pest_control])
loop_energy = OperatorPOWL(operator=Operator.LOOP, children=[energy_audit, sensor_install])
loop_monitor = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, waste_process])
loop_data = OperatorPOWL(operator=Operator.LOOP, children=[data_analysis, staff_train])
loop_community = OperatorPOWL(operator=Operator.LOOP, children=[community_link, yield_report])

root = StrictPartialOrder(nodes=[loop_site_survey, loop_design, loop_climate, loop_seed, loop_energy, loop_monitor, loop_data, loop_community])
root.order.add_edge(loop_site_survey, loop_design)
root.order.add_edge(loop_design, loop_climate)
root.order.add_edge(loop_climate, loop_seed)
root.order.add_edge(loop_seed, loop_energy)
root.order.add_edge(loop_energy, loop_monitor)
root.order.add_edge(loop_monitor, loop_data)
root.order.add_edge(loop_data, loop_community)