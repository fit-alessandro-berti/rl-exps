import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

site_survey_choice = OperatorPOWL(operator=Operator.XOR, children=[design_modules, skip])
install_sensors_choice = OperatorPOWL(operator=Operator.XOR, children=[calibrate_climate, skip])
select_seeds_choice = OperatorPOWL(operator=Operator.XOR, children=[optimize_nutrients, skip])
deploy_robots_choice = OperatorPOWL(operator=Operator.XOR, children=[monitor_growth, skip])
detect_pests_choice = OperatorPOWL(operator=Operator.XOR, children=[analyze_data, skip])
harvest_crops_choice = OperatorPOWL(operator=Operator.XOR, children=[customize_pack, skip])
recycle_waste_choice = OperatorPOWL(operator=Operator.XOR, children=[audit_energy, skip])
align_demand_choice = OperatorPOWL(operator=Operator.XOR, children=[recycle_waste, skip])

root = StrictPartialOrder(nodes=[
    site_survey, site_survey_choice, install_sensors, install_sensors_choice, select_seeds, select_seeds_choice,
    deploy_robots, deploy_robots_choice, detect_pests, detect_pests_choice, harvest_crops, harvest_crops_choice,
    recycle_waste, recycle_waste_choice, align_demand, align_demand_choice
])
root.order.add_edge(site_survey, site_survey_choice)
root.order.add_edge(site_survey_choice, install_sensors)
root.order.add_edge(install_sensors, install_sensors_choice)
root.order.add_edge(install_sensors_choice, select_seeds)
root.order.add_edge(select_seeds, select_seeds_choice)
root.order.add_edge(select_seeds_choice, deploy_robots)
root.order.add_edge(deploy_robots, deploy_robots_choice)
root.order.add_edge(deploy_robots_choice, detect_pests)
root.order.add_edge(detect_pests, detect_pests_choice)
root.order.add_edge(detect_pests_choice, harvest_crops)
root.order.add_edge(harvest_crops, harvest_crops_choice)
root.order.add_edge(harvest_crops_choice, recycle_waste)
root.order.add_edge(recycle_waste, recycle_waste_choice)
root.order.add_edge(recycle_waste_choice, align_demand)
root.order.add_edge(align_demand, align_demand_choice)