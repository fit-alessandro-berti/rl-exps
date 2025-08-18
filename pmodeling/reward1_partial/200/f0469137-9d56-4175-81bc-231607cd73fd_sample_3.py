from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_analysis = Transition(label='Site Analysis')
climate_setup = Transition(label='Climate Setup')
nutrient_mix = Transition(label='Nutrient Mix')
seed_germinate = Transition(label='Seed Germinate')
auto_planting = Transition(label='Auto Planting')
irrigation_setup = Transition(label='Irrigation Setup')
iot_monitoring = Transition(label='IoT Monitoring')
pest_detection = Transition(label='Pest Detection')
drone_pollinate = Transition(label='Drone Pollinate')
pesticide_spray = Transition(label='Pesticide Spray')
robotic_harvest = Transition(label='Robotic Harvest')
quality_check = Transition(label='Quality Check')
package_product = Transition(label='Package Product')
waste_recycle = Transition(label='Waste Recycle')
energy_optimize = Transition(label='Energy Optimize')
data_logging = Transition(label='Data Logging')

# Define transitions
skip = SilentTransition()

# Define loop nodes
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[pest_detection, pesticide_spray])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[drone_pollinate, pesticide_spray])

# Define partial order
root = StrictPartialOrder(nodes=[site_analysis, climate_setup, nutrient_mix, seed_germinate, auto_planting, irrigation_setup, iot_monitoring, loop_1, loop_2, robotic_harvest, quality_check, package_product, waste_recycle, energy_optimize, data_logging])

# Define dependencies
root.order.add_edge(site_analysis, climate_setup)
root.order.add_edge(site_analysis, nutrient_mix)
root.order.add_edge(site_analysis, seed_germinate)
root.order.add_edge(climate_setup, auto_planting)
root.order.add_edge(nutrient_mix, auto_planting)
root.order.add_edge(auto_planting, irrigation_setup)
root.order.add_edge(auto_planting, iot_monitoring)
root.order.add_edge(iot_monitoring, loop_1)
root.order.add_edge(iot_monitoring, loop_2)
root.order.add_edge(loop_1, robotic_harvest)
root.order.add_edge(loop_2, robotic_harvest)
root.order.add_edge(robotic_harvest, quality_check)
root.order.add_edge(quality_check, package_product)
root.order.add_edge(package_product, waste_recycle)
root.order.add_edge(waste_recycle, energy_optimize)
root.order.add_edge(energy_optimize, data_logging)

# Print the final result
print(root)