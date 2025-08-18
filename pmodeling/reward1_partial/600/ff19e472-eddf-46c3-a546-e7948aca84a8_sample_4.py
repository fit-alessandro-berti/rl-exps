import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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