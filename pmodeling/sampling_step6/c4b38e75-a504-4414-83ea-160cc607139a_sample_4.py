import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
design_modules = Transition(label='Design Modules')
install_sensors = Transition(label='Install Sensors')
calibrate_climate = Transition(label='Calibrate Climate')
select_seeds = Transition(label='Select Seeds')
optimize_nutrients = Transition(label='Optimize Nutrients')
deploy_robots = Transition(label='Deploy Robots')
monitor_growth = Transition(label='Monitor Growth')
detect_pests = Transition(label='Detect Pests')
analyze_data = Transition(label='Analyze Data')
harvest_crops = Transition(label='Harvest Crops')
customize_pack = Transition(label='Customize Pack')
recycle_waste = Transition(label='Recycle Waste')
audit_energy = Transition(label='Audit Energy')
align_demand = Transition(label='Align Demand')

# Define the root node of the POWL model
root = StrictPartialOrder(nodes=[
    site_survey,
    design_modules,
    install_sensors,
    calibrate_climate,
    select_seeds,
    optimize_nutrients,
    deploy_robots,
    monitor_growth,
    detect_pests,
    analyze_data,
    harvest_crops,
    customize_pack,
    recycle_waste,
    audit_energy,
    align_demand
])

# Add dependencies if any (none in this case)
# root.order.add_edge(site_survey, design_modules)
# root.order.add_edge(site_survey, install_sensors)
# root.order.add_edge(site_survey, calibrate_climate)
# root.order.add_edge(site_survey, select_seeds)
# root.order.add_edge(site_survey, optimize_nutrients)
# root.order.add_edge(site_survey, deploy_robots)
# root.order.add_edge(site_survey, monitor_growth)
# root.order.add_edge(site_survey, detect_pests)
# root.order.add_edge(site_survey, analyze_data)
# root.order.add_edge(site_survey, harvest_crops)
# root.order.add_edge(site_survey, customize_pack)
# root.order.add_edge(site_survey, recycle_waste)
# root.order.add_edge(site_survey, audit_energy)
# root.order.add_edge(site_survey, align_demand)

print(root)