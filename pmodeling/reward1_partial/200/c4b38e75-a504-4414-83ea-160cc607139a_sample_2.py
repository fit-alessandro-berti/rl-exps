from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the partial order graph
root = StrictPartialOrder(
    nodes=[site_survey, design_modules, install_sensors, calibrate_climate, select_seeds, optimize_nutrients,
           deploy_robots, monitor_growth, detect_pests, analyze_data, harvest_crops, customize_pack, recycle_waste,
           audit_energy, align_demand],
    order={
        (site_survey, design_modules): None,
        (design_modules, install_sensors): None,
        (install_sensors, calibrate_climate): None,
        (calibrate_climate, select_seeds): None,
        (select_seeds, optimize_nutrients): None,
        (optimize_nutrients, deploy_robots): None,
        (deploy_robots, monitor_growth): None,
        (monitor_growth, detect_pests): None,
        (detect_pests, analyze_data): None,
        (analyze_data, harvest_crops): None,
        (harvest_crops, customize_pack): None,
        (customize_pack, recycle_waste): None,
        (recycle_waste, audit_energy): None,
        (audit_energy, align_demand): None
    }
)

print(root)