import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_analysis   = Transition(label='Site Analysis')
climate_setup   = Transition(label='Climate Setup')
nutrient_mix    = Transition(label='Nutrient Mix')
seed_germinate  = Transition(label='Seed Germinate')
auto_planting   = Transition(label='Auto Planting')
irrigation_setup= Transition(label='Irrigation Setup')
iot_monitoring  = Transition(label='IoT Monitoring')
pest_detection  = Transition(label='Pest Detection')
drone_pollinate = Transition(label='Drone Pollinate')
pesticide_spray = Transition(label='Pesticide Spray')
robotic_harvest = Transition(label='Robotic Harvest')
quality_check   = Transition(label='Quality Check')
package_product = Transition(label='Package Product')
waste_recycle   = Transition(label='Waste Recycle')
energy_optimize = Transition(label='Energy Optimize')
data_logging    = Transition(label='Data Logging')

# Build the loop body for continuous monitoring & intervention
monitor_body = StrictPartialOrder(nodes=[
    iot_monitoring,
    pest_detection,
    drone_pollinate,
    pesticide_spray
])
# No explicit order between monitoring & detection; they can run in parallel
# Pest detection triggers either drone pollinate or pesticide spray
monitor_body.order.add_edge(iot_monitoring, pest_detection)
monitor_body.order.add_edge(pest_detection, drone_pollinate)
monitor_body.order.add_edge(pest_detection, pesticide_spray)

# Loop: do the setup, then repeatedly monitor & intervene until exit
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_body, None])

# Assemble the overall process as a strict partial order
root = StrictPartialOrder(nodes=[
    site_analysis,
    climate_setup,
    nutrient_mix,
    seed_germinate,
    auto_planting,
    irrigation_setup,
    monitor_loop,
    robotic_harvest,
    quality_check,
    package_product,
    waste_recycle,
    energy_optimize,
    data_logging
])

# Define the overall control-flow order
root.order.add_edge(site_analysis, climate_setup)
root.order.add_edge(climate_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, seed_germinate)
root.order.add_edge(seed_germinate, auto_planting)
root.order.add_edge(auto_planting, irrigation_setup)
root.order.add_edge(irrigation_setup, monitor_loop)
root.order.add_edge(monitor_loop, robotic_harvest)
root.order.add_edge(ro robotic_harvest, quality_check)
root.order.add_edge(quality_check, package_product)
root.order.add_edge(package_product, waste_recycle)
root.order.add_edge(waste_recycle, energy_optimize)
root.order.add_edge(energy_optimize, data_logging)