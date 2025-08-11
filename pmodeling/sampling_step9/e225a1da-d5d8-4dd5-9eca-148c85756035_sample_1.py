import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
select_crops = Transition(label='Select Crops')
install_modules = Transition(label='Install Modules')
setup_sensors = Transition(label='Setup Sensors')
calibrate_climate = Transition(label='Calibrate Climate')
configure_lighting = Transition(label='Configure Lighting')
integrate_iot = Transition(label='Integrate IoT')
train_staff = Transition(label='Train Staff')
run_trials = Transition(label='Run Trials')
analyze_data = Transition(label='Analyze Data')
optimize_yield = Transition(label='Optimize Yield')
check_compliance = Transition(label='Check Compliance')
plan_marketing = Transition(label='Plan Marketing')
launch_facility = Transition(label='Launch Facility')

# Define silent transitions
skip = SilentTransition()

# Define the process tree structure
loop_trial = OperatorPOWL(operator=Operator.LOOP, children=[run_trials, analyze_data, optimize_yield])
loop_crops = OperatorPOWL(operator=Operator.LOOP, children=[select_crops, design_layout, install_modules, setup_sensors, calibrate_climate, configure_lighting, integrate_iot, train_staff, loop_trial])
loop_check = OperatorPOWL(operator=Operator.LOOP, children=[check_compliance, plan_marketing, launch_facility])

# Define the POWL model
root = StrictPartialOrder(nodes=[loop_crops, loop_check])
root.order.add_edge(loop_crops, loop_check)

print(root)