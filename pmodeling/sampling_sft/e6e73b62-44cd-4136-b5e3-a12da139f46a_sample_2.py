import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
site_survey      = Transition(label='Site Survey')
design_layout    = Transition(label='Design Layout')
procure_modules  = Transition(label='Procure Modules')
install_framework= Transition(label='Install Framework')
setup_sensors    = Transition(label='Setup Sensors')
configure_iot    = Transition(label='Configure IoT')
calibrate_nut    = Transition(label='Calibrate Nutrients')
plant_seeding    = Transition(label='Plant Seeding')
monitor_growth   = Transition(label='Monitor Growth')
manage_lighting  = Transition(label='Manage Lighting')
pest_control     = Transition(label='Pest Control')
recycle_waste    = Transition(label='Recycle Waste')
analyze_data     = Transition(label='Analyze Data')
adjust_env       = Transition(label='Adjust Environment')
harvest_crops    = Transition(label='Harvest Crops')
distribute_produce=Transition(label='Distribute Produce')

# Loop for continuous monitoring and adjustment
loop_monitor = OperatorPOWL(operator=Operator.LOOP, children=[monitor_growth, adjust_env])

# Build the top-level partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    procure_modules,
    install_framework,
    setup_sensors,
    configure_iot,
    calibrate_nut,
    plant_seeding,
    loop_monitor,
    manage_lighting,
    pest_control,
    recycle_waste,
    analyze_data,
    harvest_crops,
    distribute_produce
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, procure_modules)
root.order.add_edge(procure_modules, install_framework)
root.order.add_edge(install_framework, setup_sensors)
root.order.add_edge(setup_sensors, configure_iot)
root.order.add_edge(configure_iot, calibrate_nut)
root.order.add_edge(calibrate_nut, plant_seeding)
root.order.add_edge(plant_seeding, loop_monitor)
root.order.add_edge(loop_monitor, manage_lighting)
root.order.add_edge(loop_monitor, pest_control)
root.order.add_edge(loop_monitor, recycle_waste)
root.order.add_edge(loop_monitor, analyze_data)
root.order.add_edge(loop_monitor, harvest_crops)
root.order.add_edge(harvest_crops, distribute_produce)