from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the root partial order
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
    monitor_growth,
    manage_pests,
    recycle_waste,
    engage_community,
    ensure_compliance,
    distribute_produce
])

# The process flow is already defined by the sequence of activities.
# No need to explicitly define dependencies as they are already implied by the order of activities.