import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define silent activities
skip = SilentTransition()

# Define loops
site_evaluation = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, design_modules])
climate_calibration = OperatorPOWL(operator=Operator.LOOP, children=[install_sensors, calibrate_climate])
seed_selection = OperatorPOWL(operator=Operator.LOOP, children=[select_seeds, optimize_nutrients])
robot_deployment = OperatorPOWL(operator=Operator.LOOP, children=[deploy_robots, monitor_growth])
pest_detection = OperatorPOWL(operator=Operator.LOOP, children=[detect_pests, analyze_data])
harvesting = OperatorPOWL(operator=Operator.LOOP, children=[harvest_crops, customize_pack])
waste_recycling = OperatorPOWL(operator=Operator.LOOP, children=[recycle_waste, audit_energy])
demand_alignment = OperatorPOWL(operator=Operator.LOOP, children=[align_demand])

# Define partial order
root = StrictPartialOrder(nodes=[site_evaluation, climate_calibration, seed_selection, robot_deployment, pest_detection, harvesting, waste_recycling, demand_alignment])
root.order.add_edge(site_evaluation, climate_calibration)
root.order.add_edge(site_evaluation, seed_selection)
root.order.add_edge(climate_calibration, seed_selection)
root.order.add_edge(climate_calibration, robot_deployment)
root.order.add_edge(seed_selection, robot_deployment)
root.order.add_edge(robot_deployment, pest_detection)
root.order.add_edge(robot_deployment, harvesting)
root.order.add_edge(pest_detection, harvesting)
root.order.add_edge(harvesting, waste_recycling)
root.order.add_edge(harvesting, demand_alignment)
root.order.add_edge(waste_recycling, demand_alignment)