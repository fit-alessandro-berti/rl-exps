import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as transitions
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

# Define the loop node for continuous environmental monitoring and pest detection
loop_monitor_pest = OperatorPOWL(operator=Operator.LOOP, children=[monitor_growth, detect_pests])

# Define the exclusive choice for data-driven growth analysis and automated harvesting
xor_growth_harvest = OperatorPOWL(operator=Operator.XOR, children=[analyze_data, harvest_crops])

# Define the partial order
root = StrictPartialOrder(nodes=[site_survey, design_modules, install_sensors, calibrate_climate, select_seeds, optimize_nutrients, deploy_robots, loop_monitor_pest, xor_growth_harvest, customize_pack, recycle_waste, audit_energy, align_demand])
root.order.add_edge(site_survey, design_modules)
root.order.add_edge(site_survey, install_sensors)
root.order.add_edge(site_survey, calibrate_climate)
root.order.add_edge(site_survey, select_seeds)
root.order.add_edge(site_survey, optimize_nutrients)
root.order.add_edge(site_survey, deploy_robots)
root.order.add_edge(design_modules, install_sensors)
root.order.add_edge(design_modules, calibrate_climate)
root.order.add_edge(design_modules, select_seeds)
root.order.add_edge(design_modules, optimize_nutrients)
root.order.add_edge(design_modules, deploy_robots)
root.order.add_edge(install_sensors, calibrate_climate)
root.order.add_edge(install_sensors, select_seeds)
root.order.add_edge(install_sensors, optimize_nutrients)
root.order.add_edge(install_sensors, deploy_robots)
root.order.add_edge(calibrate_climate, select_seeds)
root.order.add_edge(calibrate_climate, optimize_nutrients)
root.order.add_edge(calibrate_climate, deploy_robots)
root.order.add_edge(select_seeds, optimize_nutrients)
root.order.add_edge(select_seeds, deploy_robots)
root.order.add_edge(optimize_nutrients, deploy_robots)
root.order.add_edge(deploy_robots, loop_monitor_pest)
root.order.add_edge(loop_monitor_pest, xor_growth_harvest)
root.order.add_edge(xor_growth_harvest, customize_pack)
root.order.add_edge(xor_growth_harvest, recycle_waste)
root.order.add_edge(xor_growth_harvest, audit_energy)
root.order.add_edge(xor_growth_harvest, align_demand)

# Print the root model
print(root)