import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

site_survey_choice = OperatorPOWL(operator=Operator.XOR, children=[design_layout, skip])
design_layout_choice = OperatorPOWL(operator=Operator.XOR, children=[select_crops, skip])
select_crops_choice = OperatorPOWL(operator=Operator.XOR, children=[install_modules, skip])
install_modules_choice = OperatorPOWL(operator=Operator.XOR, children=[setup_sensors, skip])
setup_sensors_choice = OperatorPOWL(operator=Operator.XOR, children=[calibrate_climate, skip])
calibrate_climate_choice = OperatorPOWL(operator=Operator.XOR, children=[configure_lighting, skip])
configure_lighting_choice = OperatorPOWL(operator=Operator.XOR, children=[integrate_iot, skip])
integrate_iot_choice = OperatorPOWL(operator=Operator.XOR, children=[train_staff, skip])
train_staff_choice = OperatorPOWL(operator=Operator.XOR, children=[run_trials, skip])
run_trials_choice = OperatorPOWL(operator=Operator.XOR, children=[analyze_data, skip])
analyze_data_choice = OperatorPOWL(operator=Operator.XOR, children=[optimize_yield, skip])
optimize_yield_choice = OperatorPOWL(operator=Operator.XOR, children=[check_compliance, skip])
check_compliance_choice = OperatorPOWL(operator=Operator.XOR, children=[plan_marketing, skip])
plan_marketing_choice = OperatorPOWL(operator=Operator.XOR, children=[launch_facility, skip])

root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout_choice,
    select_crops_choice,
    install_modules_choice,
    setup_sensors_choice,
    calibrate_climate_choice,
    configure_lighting_choice,
    integrate_iot_choice,
    train_staff_choice,
    run_trials_choice,
    analyze_data_choice,
    optimize_yield_choice,
    check_compliance_choice,
    plan_marketing_choice
])
root.order.add_edge(site_survey, design_layout_choice)
root.order.add_edge(design_layout_choice, select_crops_choice)
root.order.add_edge(select_crops_choice, install_modules_choice)
root.order.add_edge(install_modules_choice, setup_sensors_choice)
root.order.add_edge(setup_sensors_choice, calibrate_climate_choice)
root.order.add_edge(calibrate_climate_choice, configure_lighting_choice)
root.order.add_edge(configure_lighting_choice, integrate_iot_choice)
root.order.add_edge(integrate_iot_choice, train_staff_choice)
root.order.add_edge(train_staff_choice, run_trials_choice)
root.order.add_edge(run_trials_choice, analyze_data_choice)
root.order.add_edge(analyze_data_choice, optimize_yield_choice)
root.order.add_edge(optimize_yield_choice, check_compliance_choice)
root.order.add_edge(check_compliance_choice, plan_marketing_choice)
root.order.add_edge(plan_marketing_choice, launch_facility)