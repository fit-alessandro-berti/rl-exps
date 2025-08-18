from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define the loop node
loop = OperatorPOWL(operator=Operator.LOOP, children=[
    site_analysis,
    climate_setup,
    nutrient_mix,
    seed_germinate,
    auto_planting,
    irrigation_setup,
    iot_monitoring,
    pest_detection,
    drone_pollinate,
    pesticide_spray,
    robotic_harvest,
    quality_check,
    package_product,
    waste_recycle,
    energy_optimize,
    data_logging
])

# Define the exclusive choice
xor = OperatorPOWL(operator=Operator.XOR, children=[pest_detection, pesticide_spray])

# Define the root node
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)