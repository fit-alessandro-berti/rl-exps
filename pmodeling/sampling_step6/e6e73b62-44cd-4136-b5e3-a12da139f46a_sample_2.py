import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
procure_modules = Transition(label='Procure Modules')
install_framework = Transition(label='Install Framework')
setup_sensors = Transition(label='Setup Sensors')
calibrate_nutrients = Transition(label='Calibrate Nutrients')
configure_iot = Transition(label='Configure IoT')
plant_seeding = Transition(label='Plant Seeding')
monitor_growth = Transition(label='Monitor Growth')
manage_lighting = Transition(label='Manage Lighting')
pest_control = Transition(label='Pest Control')
recycle_waste = Transition(label='Recycle Waste')
analyze_data = Transition(label='Analyze Data')
adjust_environment = Transition(label='Adjust Environment')
harvest_crops = Transition(label='Harvest Crops')
distribute_produce = Transition(label='Distribute Produce')

# Define the partial order workflow
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    procure_modules,
    install_framework,
    setup_sensors,
    calibrate_nutrients,
    configure_iot,
    plant_seeding,
    monitor_growth,
    manage_lighting,
    pest_control,
    recycle_waste,
    analyze_data,
    adjust_environment,
    harvest_crops,
    distribute_produce
])

# Add dependencies if any (in this case, there are none explicitly mentioned in the problem statement)
# root.order.add_edge(...)  # Add dependencies here if needed

print(root)