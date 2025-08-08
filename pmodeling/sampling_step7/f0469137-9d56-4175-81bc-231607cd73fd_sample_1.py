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

# Define the POWL model
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

# Define the dependencies
root.order.add_edge(site_analysis, climate_setup)
root.order.add_edge(climate_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, seed_germinate)
root.order.add_edge(seed_germinate, auto_planting)
root.order.add_edge(auto_planting, irrigation_setup)
root.order.add_edge(irrigation_setup, iot_monitoring)
root.order.add_edge(iot_monitoring, pest_detection)
root.order.add_edge(pest_detection, drone_pollinate)
root.order.add_edge(drone_pollinate, pesticide_spray)
root.order.add_edge(pesticide_spray, robotic_harvest)
root.order.add_edge(robotic_harvest, quality_check)
root.order.add_edge(quality_check, package_product)
root.order.add_edge(package_product, waste_recycle)
root.order.add_edge(waste_recycle, energy_optimize)
root.order.add_edge(energy_optimize, data_logging)