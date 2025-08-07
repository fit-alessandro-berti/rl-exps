import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_survey = Transition(label='Site Survey')
regulation_check = Transition(label='Regulation Check')
design_modules = Transition(label='Design Modules')
install_hydroponics = Transition(label='Install Hydroponics')
integrate_sensors = Transition(label='Integrate Sensors')
calibrate_nutrients = Transition(label='Calibrate Nutrients')
program_climate = Transition(label='Program Climate')
select_crops = Transition(label='Select Crops')
optimize_lighting = Transition(label='Optimize Lighting')
train_staff = Transition(label='Train Staff')
plan_harvest = Transition(label='Plan Harvest')
recycle_waste = Transition(label='Recycle Waste')
analyze_demand = Transition(label='Analyze Demand')
plan_logistics = Transition(label='Plan Logistics')
monitor_systems = Transition(label='Monitor Systems')

root = StrictPartialOrder(nodes=[
    site_survey,
    regulation_check,
    design_modules,
    install_hydroponics,
    integrate_sensors,
    calibrate_nutrients,
    program_climate,
    select_crops,
    optimize_lighting,
    train_staff,
    plan_harvest,
    recycle_waste,
    analyze_demand,
    plan_logistics,
    monitor_systems
])

# Since the process is linear, there are no dependencies defined in the order
# You can add dependencies if needed based on the sequence of activities