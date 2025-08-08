import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the partial order model
root = StrictPartialOrder(nodes=[site_survey, design_layout, select_crops, install_modules, setup_sensors, calibrate_climate, configure_lighting, integrate_iot, train_staff, run_trials, analyze_data, optimize_yield, check_compliance, plan_marketing, launch_facility])

# Define the order edges
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, select_crops)
root.order.add_edge(select_crops, install_modules)
root.order.add_edge(install_modules, setup_sensors)
root.order.add_edge(setup_sensors, calibrate_climate)
root.order.add_edge(calibrate_climate, configure_lighting)
root.order.add_edge(configure_lighting, integrate_iot)
root.order.add_edge(integrate_iot, train_staff)
root.order.add_edge(train_staff, run_trials)
root.order.add_edge(run_trials, analyze_data)
root.order.add_edge(analyze_data, optimize_yield)
root.order.add_edge(optimize_yield, check_compliance)
root.order.add_edge(check_compliance, plan_marketing)
root.order.add_edge(plan_marketing, launch_facility)

print(root)