import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transition
skip = SilentTransition()

# Define loops and XORs
site_survey_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, structural_check])
modular_install_loop = OperatorPOWL(operator=Operator.LOOP, children=[modular_install, hydroponic_setup])
nutrient_mix_loop = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, sensor_setup])
ai_training_loop = OperatorPOWL(operator=Operator.LOOP, children=[ai_training, data_capture])
maintenance_plan_loop = OperatorPOWL(operator=Operator.LOOP, children=[maintenance_plan, pest_scan])
growth_monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, harvest_sync])
quality_test_loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_test, package_prep])
logistics_plan_loop = OperatorPOWL(operator=Operator.LOOP, children=[logistics_plan, logistics_plan])

# Define XORs
xor_site_survey = OperatorPOWL(operator=Operator.XOR, children=[site_survey_loop, skip])
xor_modular_install = OperatorPOWL(operator=Operator.XOR, children=[modular_install_loop, skip])
xor_nutrient_mix = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix_loop, skip])
xor_ai_training = OperatorPOWL(operator=Operator.XOR, children=[ai_training_loop, skip])
xor_maintenance_plan = OperatorPOWL(operator=Operator.XOR, children=[maintenance_plan_loop, skip])
xor_growth_monitor = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor_loop, skip])
xor_quality_test = OperatorPOWL(operator=Operator.XOR, children=[quality_test_loop, skip])
xor_logistics_plan = OperatorPOWL(operator=Operator.XOR, children=[logistics_plan_loop, skip])

# Define the root Partial Order
root = StrictPartialOrder(nodes=[xor_site_survey, xor_modular_install, xor_nutrient_mix, xor_ai_training, xor_maintenance_plan, xor_growth_monitor, xor_quality_test, xor_logistics_plan])

# Define dependencies
root.order.add_edge(xor_site_survey, xor_modular_install)
root.order.add_edge(xor_modular_install, xor_nutrient_mix)
root.order.add_edge(xor_nutrient_mix, xor_ai_training)
root.order.add_edge(xor_ai_training, xor_maintenance_plan)
root.order.add_edge(xor_maintenance_plan, xor_growth_monitor)
root.order.add_edge(xor_growth_monitor, xor_quality_test)
root.order.add_edge(xor_quality_test, xor_logistics_plan)

# Print the result
print(root)