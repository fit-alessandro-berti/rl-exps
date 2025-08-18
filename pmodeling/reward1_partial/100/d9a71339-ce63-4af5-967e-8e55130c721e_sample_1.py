import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
site_survey = Transition(label='Site Survey')
structural_check = Transition(label='Structural Check')
modular_install = Transition(label='Modular Install')
hydroponic_setup = Transition(label='Hydroponic Setup')
nutrient_mix = Transition(label='Nutrient Mix')
sensor_setup = Transition(label='Sensor Setup')
ai_training = Transition(label='AI Training')
data_capture = Transition(label='Data Capture')
maintenance_plan = Transition(label='Maintenance Plan')
pest_scan = Transition(label='Pest Scan')
growth_monitor = Transition(label='Growth Monitor')
harvest_sync = Transition(label='Harvest Sync')
quality_test = Transition(label='Quality Test')
package_prep = Transition(label='Package Prep')
logistics_plan = Transition(label='Logistics Plan')

# Define silent transitions for skipped activities
skip = SilentTransition()

# Define the workflow
loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_scan, growth_monitor, harvest_sync, quality_test, package_prep])
xor = OperatorPOWL(operator=Operator.XOR, children=[data_capture, maintenance_plan, logistics_plan])

root = StrictPartialOrder(nodes=[site_survey, structural_check, modular_install, hydroponic_setup, nutrient_mix, sensor_setup, ai_training, loop, xor])
root.order.add_edge(site_survey, structural_check)
root.order.add_edge(structural_check, modular_install)
root.order.add_edge(modular_install, hydroponic_setup)
root.order.add_edge(hydroponic_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, sensor_setup)
root.order.add_edge(sensor_setup, ai_training)
root.order.add_edge(ai_training, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, data_capture)
root.order.add_edge(xor, maintenance_plan)
root.order.add_edge(xor, logistics_plan)

# Save the root in a variable
root