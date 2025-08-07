import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey     = Transition(label='Site Survey')
design_layout   = Transition(label='Design Layout')
procure_modules = Transition(label='Procure Modules')
install_fw      = Transition(label='Install Framework')
setup_sensors   = Transition(label='Setup Sensors')
configure_iot   = Transition(label='Configure IoT')
calibrate_nut   = Transition(label='Calibrate Nutrients')
plant_seeding   = Transition(label='Plant Seeding')
monitor_growth  = Transition(label='Monitor Growth')
manage_lighting = Transition(label='Manage Lighting')
pest_control    = Transition(label='Pest Control')
recycle_waste   = Transition(label='Recycle Waste')
analyze_data    = Transition(label='Analyze Data')
adjust_env      = Transition(label='Adjust Environment')
harvest_crops   = Transition(label='Harvest Crops')
distribute_pro  = Transition(label='Distribute Produce')

# Loop for repeated monitoring and adjustment
loop_body = StrictPartialOrder(nodes=[monitor_growth, manage_lighting, pest_control, recycle_waste, analyze_data, adjust_env])
loop_body.order.add_edge(monitor_growth, manage_lighting)
loop_body.order.add_edge(manage_lighting, pest_control)
loop_body.order.add_edge(pest_control, recycle_waste)
loop_body.order.add_edge(recycle_waste, analyze_data)
loop_body.order.add_edge(analyze_data, adjust_env)

loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_growth, loop_body])

# Assemble the top-level partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    procure_modules,
    install_fw,
    setup_sensors,
    configure_iot,
    calibrate_nut,
    plant_seeding,
    loop,
    harvest_crops,
    distribute_pro
])

# Define the control-flow edges
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, procure_modules)
root.order.add_edge(procure_modules, install_fw)
root.order.add_edge(install_fw, setup_sensors)
root.order.add_edge(setup_sensors, configure_iot)
root.order.add_edge(configure_iot, calibrate_nut)
root.order.add_edge(calibrate_nut, plant_seeding)
root.order.add_edge(plant_seeding, loop)
root.order.add_edge(loop, harvest_crops)
root.order.add_edge(harvest_crops, distribute_pro)