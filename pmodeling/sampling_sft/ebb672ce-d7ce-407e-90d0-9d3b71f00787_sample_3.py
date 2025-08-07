import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey      = Transition(label='Site Survey')
design_layout    = Transition(label='Design Layout')
modular_build    = Transition(label='Modular Build')
install_pumps    = Transition(label='Install Pumps')
setup_sensors    = Transition(label='Setup Sensors')
calibrate_lights = Transition(label='Calibrate Lights')
nutrient_mix     = Transition(label='Nutrient Mix')
plant_seeding    = Transition(label='Plant Seeding')
water_cycling    = Transition(label='Water Cycling')
energy_audit     = Transition(label='Energy Audit')
pest_control     = Transition(label='Pest Control')
growth_monitor   = Transition(label='Growth Monitor')
data_analysis    = Transition(label='Data Analysis')
yield_forecast   = Transition(label='Yield Forecast')
supply_order     = Transition(label='Supply Order')
waste_recycle    = Transition(label='Waste Recycle')
system_upgrade   = Transition(label='System Upgrade')

# Silent transition for loop exits
skip = SilentTransition()

# Loop for continuous monitoring and adjustment
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_monitor, data_analysis, yield_forecast]
)

# Parallel activities before the loop
build_seq = StrictPartialOrder(nodes=[install_pumps, setup_sensors, calibrate_lights])
build_seq.order.add_edge(install_pumps, setup_sensors)
build_seq.order.add_edge(setup_sensors, calibrate_lights)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    modular_build,
    build_seq,
    nutrient_mix,
    plant_seeding,
    water_cycling,
    energy_audit,
    pest_control,
    monitor_loop,
    supply_order,
    waste_recycle,
    system_upgrade
])

# Add dependencies
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, modular_build)
root.order.add_edge(modular_build, build_seq)
root.order.add_edge(build_seq, nutrient_mix)
root.order.add_edge(nutrient_mix, plant_seeding)
root.order.add_edge(plant_seeding, water_cycling)
root.order.add_edge(water_cycling, energy_audit)
root.order.add_edge(energy_audit, pest_control)
root.order.add_edge(pest_control, monitor_loop)
root.order.add_edge(monitor_loop, supply_order)
root.order.add_edge(supply_order, waste_recycle)
root.order.add_edge(waste_recycle, system_upgrade)

# Final loop exit can be either waste_recycle or system_upgrade
final_choice = OperatorPOWL(operator=Operator.XOR, children=[waste_recycle, system_upgrade])
root.order.add_edge(monitor_loop, final_choice)