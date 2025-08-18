import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the loop and exclusive choice nodes
trial_cycle = OperatorPOWL(operator=Operator.LOOP, children=[run_trials, analyze_data, optimize_yield])
training_process = OperatorPOWL(operator=Operator.XOR, children=[train_staff, trial_cycle])

root = StrictPartialOrder(nodes=[site_survey, design_layout, select_crops, install_modules, setup_sensors, calibrate_climate, configure_lighting, integrate_iot, training_process, check_compliance, plan_marketing, launch_facility])
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, select_crops)
root.order.add_edge(select_crops, install_modules)
root.order.add_edge(install_modules, setup_sensors)
root.order.add_edge(setup_sensors, calibrate_climate)
root.order.add_edge(calibrate_climate, configure_lighting)
root.order.add_edge(configure_lighting, integrate_iot)
root.order.add_edge(integrate_iot, training_process)
root.order.add_edge(training_process, check_compliance)
root.order.add_edge(check_compliance, plan_marketing)
root.order.add_edge(plan_marketing, launch_facility)