from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
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

# Define the operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[pest_detection, drone_pollinate, pesticide_spray])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[quality_check, package_product])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycle, energy_optimize])
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, seed_germinate, auto_planting, irrigation_setup, iot_monitoring, xor1])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[drone_pollinate, pesticide_spray, robotic_harvest, quality_check, package_product])
root = StrictPartialOrder(nodes=[loop1, loop2, xor2, xor3])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop2, xor2)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)

# Print the POWL model
print(root)