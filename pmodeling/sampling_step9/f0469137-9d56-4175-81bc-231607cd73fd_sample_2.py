import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define the POWL model
loop_drone_pollinate = OperatorPOWL(operator=Operator.LOOP, children=[pest_detection, drone_pollinate])
loop_pesticide_spray = OperatorPOWL(operator=Operator.LOOP, children=[pest_detection, pesticide_spray])
loop_data_logging = OperatorPOWL(operator=Operator.LOOP, children=[iot_monitoring, data_logging])

xor_irrigation_setup = OperatorPOWL(operator=Operator.XOR, children=[irrigation_setup, skip])
xor_energy_optimize = OperatorPOWL(operator=Operator.XOR, children=[energy_optimize, skip])

xor_quality_check = OperatorPOWL(operator=Operator.XOR, children=[quality_check, skip])
xor_package_product = OperatorPOWL(operator=Operator.XOR, children=[package_product, skip])

xor_waste_recycle = OperatorPOWL(operator=Operator.XOR, children=[waste_recycle, skip])

root = StrictPartialOrder(nodes=[site_analysis, climate_setup, nutrient_mix, seed_germinate, auto_planting,
                                 loop_drone_pollinate, loop_pesticide_spray, loop_data_logging,
                                 xor_irrigation_setup, xor_energy_optimize,
                                 xor_quality_check, xor_package_product,
                                 xor_waste_recycle,
                                 robotic_harvest])
root.order.add_edge(site_analysis, climate_setup)
root.order.add_edge(climate_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, seed_germinate)
root.order.add_edge(seed_germinate, auto_planting)
root.order.add_edge(auto_planting, loop_drone_pollinate)
root.order.add_edge(loop_drone_pollinate, loop_pesticide_spray)
root.order.add_edge(loop_pesticide_spray, loop_data_logging)
root.order.add_edge(loop_data_logging, xor_irrigation_setup)
root.order.add_edge(xor_irrigation_setup, xor_energy_optimize)
root.order.add_edge(xor_energy_optimize, xor_quality_check)
root.order.add_edge(xor_quality_check, xor_package_product)
root.order.add_edge(xor_package_product, xor_waste_recycle)
root.order.add_edge(xor_waste_recycle, robotic_harvest)