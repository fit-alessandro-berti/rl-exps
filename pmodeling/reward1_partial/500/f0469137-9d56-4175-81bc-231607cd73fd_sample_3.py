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

# Define the process
loop_irrigation = OperatorPOWL(operator=Operator.LOOP, children=[irrigation_setup, skip])
loop_pollinate = OperatorPOWL(operator=Operator.LOOP, children=[drone_pollinate, skip])
loop_pesticide = OperatorPOWL(operator=Operator.LOOP, children=[pesticide_spray, skip])
loop_harvest = OperatorPOWL(operator=Operator.LOOP, children=[robotic_harvest, skip])
loop_quality = OperatorPOWL(operator=Operator.LOOP, children=[quality_check, skip])
loop_package = OperatorPOWL(operator=Operator.LOOP, children=[package_product, skip])
loop_recycle = OperatorPOWL(operator=Operator.LOOP, children=[waste_recycle, skip])
loop_optimize = OperatorPOWL(operator=Operator.LOOP, children=[energy_optimize, skip])
loop_data = OperatorPOWL(operator=Operator.LOOP, children=[data_logging, skip])

root = StrictPartialOrder(nodes=[
    site_analysis,
    climate_setup,
    nutrient_mix,
    seed_germinate,
    auto_planting,
    loop_irrigation,
    loop_pollinate,
    loop_pesticide,
    loop_harvest,
    loop_quality,
    loop_package,
    loop_recycle,
    loop_optimize,
    loop_data
])

# Add dependencies
root.order.add_edge(site_analysis, climate_setup)
root.order.add_edge(climate_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, seed_germinate)
root.order.add_edge(seed_germinate, auto_planting)
root.order.add_edge(auto_planting, loop_irrigation)
root.order.add_edge(loop_irrigation, loop_pollinate)
root.order.add_edge(loop_pollinate, loop_pesticide)
root.order.add_edge(loop_pesticide, loop_harvest)
root.order.add_edge(loop_harvest, loop_quality)
root.order.add_edge(loop_quality, loop_package)
root.order.add_edge(loop_package, loop_recycle)
root.order.add_edge(loop_recycle, loop_optimize)
root.order.add_edge(loop_optimize, loop_data)

# Print the root
print(root)