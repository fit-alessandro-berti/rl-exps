import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site_survey      = Transition(label='Site Survey')
design_layout    = Transition(label='Design Layout')
select_crops     = Transition(label='Select Crops')
install_modules  = Transition(label='Install Modules')
setup_sensors    = Transition(label='Setup Sensors')
calibrate_climate= Transition(label='Calibrate Climate')
configure_lighting= Transition(label='Configure Lighting')
integrate_iot    = Transition(label='Integrate IoT')
train_staff      = Transition(label='Train Staff')
run_trials       = Transition(label='Run Trials')
analyze_data     = Transition(label='Analyze Data')
optimize_yield   = Transition(label='Optimize Yield')
check_compliance = Transition(label='Check Compliance')
plan_marketing   = Transition(label='Plan Marketing')
launch_facility  = Transition(label='Launch Facility')

# Define the loop for continuous data-driven yield optimization
# Body A: Analyze Data -> Optimize Yield
body_a = StrictPartialOrder(nodes=[analyze_data, optimize_yield])
body_a.order.add_edge(analyze_data, optimize_yield)

# Body B: Check Compliance -> Plan Marketing
body_b = StrictPartialOrder(nodes=[check_compliance, plan_marketing])
body_b.order.add_edge(check_compliance, plan_marketing)

# Loop: do Body A, then either exit or do Body B and repeat
yield_loop = OperatorPOWL(operator=Operator.LOOP, children=[body_a, body_b])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    select_crops,
    install_modules,
    setup_sensors,
    calibrate_climate,
    configure_lighting,
    integrate_iot,
    train_staff,
    run_trials,
    yield_loop,
    launch_facility
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, select_crops)
root.order.add_edge(select_crops, install_modules)
root.order.add_edge(install_modules, setup_sensors)
root.order.add_edge(setup_sensors, calibrate_climate)
root.order.add_edge(calibrate_climate, configure_lighting)
root.order.add_edge(configure_lighting, integrate_iot)
root.order.add_edge(integrate_iot, train_staff)
root.order.add_edge(train_staff, run_trials)
root.order.add_edge(run_trials, yield_loop)
root.order.add_edge(yield_loop, launch_facility)