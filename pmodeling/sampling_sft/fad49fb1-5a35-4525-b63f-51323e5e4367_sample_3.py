import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey     = Transition(label='Site Survey')
design_modules  = Transition(label='Design Modules')
source_materials= Transition(label='Source Materials')
install_framework= Transition(label='Install Framework')
setup_irrigation= Transition(label='Setup Irrigation')
integrate_sensors= Transition(label='Integrate Sensors')
configure_ai    = Transition(label='Configure AI')
select_crops    = Transition(label='Select Crops')
calibrate_climate= Transition(label='Calibrate Climate')
plant_seeds     = Transition(label='Plant Seeds')
monitor_growth  = Transition(label='Monitor Growth')
manage_pests    = Transition(label='Manage Pests')
recycle_waste   = Transition(label='Recycle Waste')
engage_community= Transition(label='Engage Community')
ensure_compliance= Transition(label='Ensure Compliance')
distribute_produce= Transition(label='Distribute Produce')

# Loop for iterative growth monitoring: repeat Monitor Growth then Manage Pests or Recycle Waste, until exit
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_growth, manage_pests | recycle_waste])

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    design_modules,
    source_materials,
    install_framework,
    setup_irrigation,
    integrate_sensors,
    configure_ai,
    select_crops,
    calibrate_climate,
    plant_seeds,
    monitor_loop,
    engage_community,
    ensure_compliance,
    distribute_produce
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, design_modules)
root.order.add_edge(design_modules, source_materials)
root.order.add_edge(source_materials, install_framework)
root.order.add_edge(install_framework, setup_irrigation)
root.order.add_edge(setup_irrigation, integrate_sensors)
root.order.add_edge(integrate_sensors, configure_ai)
root.order.add_edge(configure_ai, select_crops)
root.order.add_edge(select_crops, calibrate_climate)
root.order.add_edge(calibrate_climate, plant_seeds)
root.order.add_edge(plant_seeds, monitor_loop)
root.order.add_edge(monitor_loop, engage_community)
root.order.add_edge(engage_community, ensure_compliance)
root.order.add_edge(ensure_compliance, distribute_produce)