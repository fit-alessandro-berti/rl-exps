from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

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

site_survey_to_design = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[site_survey, design_layout])
design_layout_to_select = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[design_layout, select_crops])
select_crops_to_install = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[select_crops, install_modules])
install_modules_to_setup = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[install_modules, setup_sensors])
setup_sensors_to_calibrate = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[setup_sensors, calibrate_climate])
calibrate_climate_to_light = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[calibrate_climate, configure_lighting])
configure_lighting_to_integrate = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[configure_lighting, integrate_iot])
integrate_iot_to_train = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[integrate_iot, train_staff])
train_staff_to_trials = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[train_staff, run_trials])
run_trials_to_analyze = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[run_trials, analyze_data])
analyze_data_to_optimize = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[analyze_data, optimize_yield])
optimize_yield_to_compliance = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[optimize_yield, check_compliance])
check_compliance_to_marketing = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[check_compliance, plan_marketing])
plan_marketing_to_launch = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[plan_marketing, launch_facility])

root = StrictPartialOrder(nodes=[
    site_survey_to_design,
    design_layout_to_select,
    select_crops_to_install,
    install_modules_to_setup,
    setup_sensors_to_calibrate,
    calibrate_climate_to_light,
    configure_lighting_to_integrate,
    integrate_iot_to_train,
    train_staff_to_trials,
    run_trials_to_analyze,
    analyze_data_to_optimize,
    optimize_yield_to_compliance,
    check_compliance_to_marketing,
    plan_marketing_to_launch
])

root.order.add_edge(site_survey_to_design, design_layout_to_select)
root.order.add_edge(design_layout_to_select, select_crops_to_install)
root.order.add_edge(select_crops_to_install, install_modules_to_setup)
root.order.add_edge(install_modules_to_setup, setup_sensors_to_calibrate)
root.order.add_edge(setup_sensors_to_calibrate, calibrate_climate_to_light)
root.order.add_edge(calibrate_climate_to_light, configure_lighting_to_integrate)
root.order.add_edge(configure_lighting_to_integrate, integrate_iot_to_train)
root.order.add_edge(integrate_iot_to_train, train_staff_to_trials)
root.order.add_edge(train_staff_to_trials, run_trials_to_analyze)
root.order.add_edge(run_trials_to_analyze, analyze_data_to_optimize)
root.order.add_edge(analyze_data_to_optimize, optimize_yield_to_compliance)
root.order.add_edge(optimize_yield_to_compliance, check_compliance_to_marketing)
root.order.add_edge(check_compliance_to_marketing, plan_marketing_to_launch)