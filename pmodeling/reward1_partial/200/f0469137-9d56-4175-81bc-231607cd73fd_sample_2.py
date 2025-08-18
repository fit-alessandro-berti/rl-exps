from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their exact names
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

# Define silent transitions (if any, here none)
skip = SilentTransition()

# Define the workflow model
root = StrictPartialOrder(
    nodes=[
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
    ],
    order=[
        (site_analysis, climate_setup),
        (site_analysis, nutrient_mix),
        (site_analysis, seed_germinate),
        (climate_setup, nutrient_mix),
        (climate_setup, seed_germinate),
        (nutrient_mix, auto_planting),
        (nutrient_mix, irrigation_setup),
        (seed_germinate, irrigation_setup),
        (auto_planting, iot_monitoring),
        (auto_planting, pest_detection),
        (auto_planting, drone_pollinate),
        (auto_planting, pesticide_spray),
        (irrigation_setup, robotic_harvest),
        (irrigation_setup, quality_check),
        (irrigation_setup, package_product),
        (iot_monitoring, pest_detection),
        (pest_detection, drone_pollinate),
        (pest_detection, pesticide_spray),
        (drone_pollinate, pesticide_spray),
        (pesticide_spray, robotic_harvest),
        (pesticide_spray, quality_check),
        (pesticide_spray, package_product),
        (robotic_harvest, quality_check),
        (robotic_harvest, package_product),
        (quality_check, package_product),
        (package_product, waste_recycle),
        (package_product, energy_optimize),
        (package_product, data_logging),
        (waste_recycle, energy_optimize),
        (waste_recycle, data_logging),
        (energy_optimize, data_logging)
    ]
)

print(root)