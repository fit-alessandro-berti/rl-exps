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

# Define the root process
root = StrictPartialOrder(nodes=[
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

# Define the order of execution
# This is a simplified representation and actual order would depend on specific dependencies
# For this example, we assume no specific order, as it's not specified in the description
# If there are dependencies, they should be added here
# For instance, if Site Analysis must precede Climate Setup, it would be:
# root.order.add_edge(site_analysis, climate_setup)

print(root)