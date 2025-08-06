import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_survey = Transition(label='Site Survey')
design_modules = Transition(label='Design Modules')
source_materials = Transition(label='Source Materials')
install_framework = Transition(label='Install Framework')
setup_irrigation = Transition(label='Setup Irrigation')
integrate_sensors = Transition(label='Integrate Sensors')
configure_ai = Transition(label='Configure AI')
select_crops = Transition(label='Select Crops')
calibrate_climate = Transition(label='Calibrate Climate')
plant_seeds = Transition(label='Plant Seeds')
monitor_growth = Transition(label='Monitor Growth')
manage_pests = Transition(label='Manage Pests')
recycle_waste = Transition(label='Recycle Waste')
engage_community = Transition(label='Engage Community')
ensure_compliance = Transition(label='Ensure Compliance')
distribute_produce = Transition(label='Distribute Produce')

# Define the partial order structure
root = StrictPartialOrder(
    nodes=[site_survey, design_modules, source_materials, install_framework, setup_irrigation,
           integrate_sensors, configure_ai, select_crops, calibrate_climate, plant_seeds, monitor_growth,
           manage_pests, recycle_waste, engage_community, ensure_compliance, distribute_produce],
    order=[
        (site_survey, design_modules),
        (design_modules, source_materials),
        (source_materials, install_framework),
        (install_framework, setup_irrigation),
        (setup_irrigation, integrate_sensors),
        (integrate_sensors, configure_ai),
        (configure_ai, select_crops),
        (select_crops, calibrate_climate),
        (calibrate_climate, plant_seeds),
        (plant_seeds, monitor_growth),
        (monitor_growth, manage_pests),
        (manage_pests, recycle_waste),
        (recycle_waste, engage_community),
        (engage_community, ensure_compliance),
        (ensure_compliance, distribute_produce)
    ]
)

print(root)