import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey      = Transition(label='Site Survey')
design_modules   = Transition(label='Design Modules')
install_sensors  = Transition(label='Install Sensors')
calibrate_climate= Transition(label='Calibrate Climate')
select_seeds     = Transition(label='Select Seeds')
optimize_nutrients= Transition(label='Optimize Nutrients')
deploy_robots    = Transition(label='Deploy Robots')
monitor_growth   = Transition(label='Monitor Growth')
detect_pests     = Transition(label='Detect Pests')
analyze_data     = Transition(label='Analyze Data')
harvest_crops    = Transition(label='Harvest Crops')
customize_pack   = Transition(label='Customize Pack')
recycle_waste    = Transition(label='Recycle Waste')
audit_energy     = Transition(label='Audit Energy')
align_demand     = Transition(label='Align Demand')

# Define the monitoring and analysis loop body (A)
body = StrictPartialOrder(nodes=[detect_pests, analyze_data])

# Define the monitoring and analysis loop (B): do body, then optionally repeat
loop_monitor = OperatorPOWL(operator=Operator.LOOP, children=[body, body])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    design_modules,
    install_sensors,
    calibrate_climate,
    select_seeds,
    optimize_nutrients,
    deploy_robots,
    loop_monitor,
    harvest_crops,
    customize_pack,
    recycle_waste,
    audit_energy,
    align_demand
])

# Define the control-flow dependencies
root.order.add_edge(site_survey,     design_modules)
root.order.add_edge(design_modules,  install_sensors)
root.order.add_edge(install_sensors, calibrate_climate)
root.order.add_edge(calibrate_climate, select_seeds)
root.order.add_edge(select_seeds,    optimize_nutrients)
root.order.add_edge(optimize_nutrients, deploy_robots)
root.order.add_edge(deploy_robots,   loop_monitor)
root.order.add_edge(loop_monitor,    harvest_crops)
root.order.add_edge(harvest_crops,   customize_pack)
root.order.add_edge(customize_pack,  recycle_waste)
root.order.add_edge(recycle_waste,   audit_energy)
root.order.add_edge(audit_energy,    align_demand)