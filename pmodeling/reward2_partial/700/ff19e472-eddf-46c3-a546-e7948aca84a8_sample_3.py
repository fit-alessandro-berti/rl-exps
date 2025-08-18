import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities) for the process
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
install_modules = Transition(label='Install Modules')
calibrate_climate = Transition(label='Calibrate Climate')
prepare_nutrients = Transition(label='Prepare Nutrients')
select_seeds = Transition(label='Select Seeds')
start_germination = Transition(label='Start Germination')
deploy_sensors = Transition(label='Deploy Sensors')
monitor_growth = Transition(label='Monitor Growth')
manage_pests = Transition(label='Manage Pests')
schedule_harvest = Transition(label='Schedule Harvest')
process_waste = Transition(label='Process Waste')
optimize_energy = Transition(label='Optimize Energy')
conduct_training = Transition(label='Conduct Training')
update_records = Transition(label='Update Records')
review_performance = Transition(label='Review Performance')

# Define the partial order model
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    install_modules,
    calibrate_climate,
    prepare_nutrients,
    select_seeds,
    start_germination,
    deploy_sensors,
    monitor_growth,
    manage_pests,
    schedule_harvest,
    process_waste,
    optimize_energy,
    conduct_training,
    update_records,
    review_performance
])

# Define dependencies (edges) between transitions
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, install_modules)
root.order.add_edge(install_modules, calibrate_climate)
root.order.add_edge(calibrate_climate, prepare_nutrients)
root.order.add_edge(prepare_nutrients, select_seeds)
root.order.add_edge(select_seeds, start_germination)
root.order.add_edge(start_germination, deploy_sensors)
root.order.add_edge(deploy_sensors, monitor_growth)
root.order.add_edge(monitor_growth, manage_pests)
root.order.add_edge(manage_pests, schedule_harvest)
root.order.add_edge(schedule_harvest, process_waste)
root.order.add_edge(process_waste, optimize_energy)
root.order.add_edge(optimize_energy, conduct_training)
root.order.add_edge(conduct_training, update_records)
root.order.add_edge(update_records, review_performance)

# Print the partial order model
print(root)