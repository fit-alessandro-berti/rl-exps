import pm4py
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

# Define the root process
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
# Since the activities are concurrent, no edges are needed between them.
# If there were dependencies, they would be added here, for example:
# root.order.add_edge(site_survey, design_modules)
# root.order.add_edge(source_materials, install_framework)

# Note: In the given process description, there are no explicit dependencies between activities.
# If there were, you would need to add those dependencies using `root.order.add_edge` as shown above.
# For example, if 'Site Survey' must precede 'Design Modules', you would write:
# root.order.add_edge(site_survey, design_modules)

print(root)