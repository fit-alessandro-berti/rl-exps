import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey      = Transition(label='Site Survey')
design_layout    = Transition(label='Design Layout')
procure_modules  = Transition(label='Procure Modules')
install_framework= Transition(label='Install Framework')
setup_sensors    = Transition(label='Setup Sensors')
configure_iot    = Transition(label='Configure IoT')
calibrate_nutrients = Transition(label='Calibrate Nutrients')
plant_seeding    = Transition(label='Plant Seeding')
monitor_growth   = Transition(label='Monitor Growth')
manage_lighting  = Transition(label='Manage Lighting')
pest_control     = Transition(label='Pest Control')
recycle_waste    = Transition(label='Recycle Waste')
analyze_data     = Transition(label='Analyze Data')
adjust_environment= Transition(label='Adjust Environment')
harvest_crops    = Transition(label='Harvest Crops')
distribute_produce= Transition(label='Distribute Produce')

# Loop for crop cycle: repeat growth-monitoring-adjustment until exit
crop_cycle_body = StrictPartialOrder(nodes=[monitor_growth, adjust_environment])
crop_cycle_body.order.add_edge(monitor_growth, adjust_environment)
crop_cycle = OperatorPOWL(operator=Operator.LOOP, children=[plant_seeding, crop_cycle_body])

# Build the top-level partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    procure_modules,
    install_framework,
    setup_sensors,
    configure_iot,
    calibrate_nutrients,
    crop_cycle,
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
root.order.add_edge(configure_iot, calibrate_nutrients)
root.order.add_edge(calibrate_nutrients, crop_cycle)
root.order.add_edge(crop_cycle, analyze_data)
root.order.add_edge(analyze_data, harvest_crops)
root.order.add_edge(harvest_crops, distribute_produce)