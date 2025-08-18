import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

# Site Analysis -> Climate Setup
site_analysis_to_climate = OperatorPOWL(operator=Operator.XOR, children=[site_analysis, climate_setup])

# Climate Setup -> Nutrient Mix
climate_setup_to_nutrient = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, nutrient_mix])

# Nutrient Mix -> Seed Germinate
nutrient_mix_to_germinate = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, seed_germinate])

# Seed Germinate -> Auto Planting
seed_germinate_to_plant = OperatorPOWL(operator=Operator.XOR, children=[seed_germinate, auto_planting])

# Auto Planting -> Irrigation Setup
auto_planting_to_irrigation = OperatorPOWL(operator=Operator.XOR, children=[auto_planting, irrigation_setup])

# Irrigation Setup -> IoT Monitoring
irrigation_setup_to_iot = OperatorPOWL(operator=Operator.XOR, children=[irrigation_setup, iot_monitoring])

# IoT Monitoring -> Pest Detection
iot_monitoring_to_pest = OperatorPOWL(operator=Operator.XOR, children=[iot_monitoring, pest_detection])

# Pest Detection -> Drone Pollinate
pest_detection_to_pollinate = OperatorPOWL(operator=Operator.XOR, children=[pest_detection, drone_pollinate])

# Drone Pollinate -> Pesticide Spray
drone_pollinate_to_spray = OperatorPOWL(operator=Operator.XOR, children=[drone_pollinate, pesticide_spray])

# Pesticide Spray -> Robotic Harvest
pesticide_spray_to_harvest = OperatorPOWL(operator=Operator.XOR, children=[pesticide_spray, robotic_harvest])

# Robotic Harvest -> Quality Check
robotic_harvest_to_quality = OperatorPOWL(operator=Operator.XOR, children=[robotic_harvest, quality_check])

# Quality Check -> Package Product
quality_check_to_package = OperatorPOWL(operator=Operator.XOR, children=[quality_check, package_product])

# Package Product -> Waste Recycle
package_product_to_waste = OperatorPOWL(operator=Operator.XOR, children=[package_product, waste_recycle])

# Waste Recycle -> Energy Optimize
waste_recycle_to_energy = OperatorPOWL(operator=Operator.XOR, children=[waste_recycle, energy_optimize])

# Energy Optimize -> Data Logging
energy_optimize_to_data = OperatorPOWL(operator=Operator.XOR, children=[energy_optimize, data_logging])

# Define the root partial order
root = StrictPartialOrder(nodes=[
    site_analysis_to_climate,
    climate_setup_to_nutrient,
    nutrient_mix_to_germinate,
    seed_germinate_to_plant,
    auto_planting_to_irrigation,
    irrigation_setup_to_iot,
    iot_monitoring_to_pest,
    pest_detection_to_pollinate,
    drone_pollinate_to_spray,
    pesticide_spray_to_harvest,
    robotic_harvest_to_quality,
    quality_check_to_package,
    package_product_to_waste,
    waste_recycle_to_energy,
    energy_optimize_to_data
])

# Define the order dependencies
root.order.add_edge(site_analysis_to_climate, climate_setup_to_nutrient)
root.order.add_edge(climate_setup_to_nutrient, nutrient_mix_to_germinate)
root.order.add_edge(nutrient_mix_to_germinate, seed_germinate_to_plant)
root.order.add_edge(seed_germinate_to_plant, auto_planting_to_irrigation)
root.order.add_edge(auto_planting_to_irrigation, irrigation_setup_to_iot)
root.order.add_edge(irrigation_setup_to_iot, iot_monitoring_to_pest)
root.order.add_edge(iot_monitoring_to_pest, pest_detection_to_pollinate)
root.order.add_edge(pest_detection_to_pollinate, drone_pollinate_to_spray)
root.order.add_edge(drone_pollinate_to_spray, pesticide_spray_to_harvest)
root.order.add_edge(pesticide_spray_to_harvest, robotic_harvest_to_quality)
root.order.add_edge(robotic_harvest_to_quality, quality_check_to_package)
root.order.add_edge(quality_check_to_package, package_product_to_waste)
root.order.add_edge(package_product_to_waste, waste_recycle_to_energy)
root.order.add_edge(waste_recycle_to_energy, energy_optimize_to_data)