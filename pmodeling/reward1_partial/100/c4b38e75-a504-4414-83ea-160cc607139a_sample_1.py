import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the workflow model
site_survey_choice = OperatorPOWL(operator=Operator.XOR, children=[site_survey, design_modules])
design_modules_choice = OperatorPOWL(operator=Operator.XOR, children=[install_sensors, calibrate_climate])
install_sensors_choice = OperatorPOWL(operator=Operator.XOR, children=[select_seeds, optimize_nutrients])
select_seeds_choice = OperatorPOWL(operator=Operator.XOR, children=[deploy_robots, monitor_growth])
deploy_robots_choice = OperatorPOWL(operator=Operator.XOR, children=[detect_pests, analyze_data])
monitor_growth_choice = OperatorPOWL(operator=Operator.XOR, children=[harvest_crops, customize_pack])
harvest_crops_choice = OperatorPOWL(operator=Operator.XOR, children=[recycle_waste, audit_energy])
recycle_waste_choice = OperatorPOWL(operator=Operator.XOR, children=[align_demand, audit_energy])

# Create the root node with the choices
root = StrictPartialOrder(nodes=[site_survey_choice, design_modules_choice, install_sensors_choice, select_seeds_choice, deploy_robots_choice, monitor_growth_choice, harvest_crops_choice, recycle_waste_choice])
root.order.add_edge(site_survey_choice, design_modules_choice)
root.order.add_edge(design_modules_choice, install_sensors_choice)
root.order.add_edge(install_sensors_choice, select_seeds_choice)
root.order.add_edge(select_seeds_choice, deploy_robots_choice)
root.order.add_edge(deploy_robots_choice, detect_pests_choice)
root.order.add_edge(detect_pests_choice, analyze_data_choice)
root.order.add_edge(monitor_growth_choice, harvest_crops_choice)
root.order.add_edge(harvest_crops_choice, recycle_waste_choice)
root.order.add_edge(recycle_waste_choice, align_demand_choice)
root.order.add_edge(align_demand_choice, audit_energy_choice)

print(root)