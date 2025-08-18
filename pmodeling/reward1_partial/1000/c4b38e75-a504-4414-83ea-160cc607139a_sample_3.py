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

site_survey_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, design_modules, install_sensors, calibrate_climate, select_seeds, optimize_nutrients, deploy_robots, monitor_growth, detect_pests, analyze_data])
monitor_growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_growth, detect_pests, analyze_data, harvest_crops, customize_pack, recycle_waste, audit_energy, align_demand])
root = StrictPartialOrder(nodes=[site_survey_loop, monitor_growth_loop])
root.order.add_edge(site_survey_loop, monitor_growth_loop)