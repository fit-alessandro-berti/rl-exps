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

# Site Assessment
site_assessment = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, design_layout])

# Modular System Design
modular_design = OperatorPOWL(operator=Operator.LOOP, children=[select_crops, install_modules])

# Environmental Calibration
env_calibration = OperatorPOWL(operator=Operator.LOOP, children=[calibrate_climate, configure_lighting])

# IoT Monitoring and Integration
iot_integration = OperatorPOWL(operator=Operator.LOOP, children=[integrate_iot, setup_sensors])

# Staff Training
staff_training = OperatorPOWL(operator=Operator.LOOP, children=[train_staff, skip])

# Trial Cultivation
trial_cultivation = OperatorPOWL(operator=Operator.LOOP, children=[run_trials, analyze_data])

# Yield Optimization
yield_optimization = OperatorPOWL(operator=Operator.LOOP, children=[optimize_yield, skip])

# Regulatory Compliance
compliance_check = OperatorPOWL(operator=Operator.LOOP, children=[check_compliance, skip])

# Marketing Planning
marketing_planning = OperatorPOWL(operator=Operator.LOOP, children=[plan_marketing, skip])

# Facility Launch
facility_launch = OperatorPOWL(operator=Operator.LOOP, children=[launch_facility, skip])

root = StrictPartialOrder(nodes=[site_assessment, modular_design, env_calibration, iot_integration, staff_training, trial_cultivation, yield_optimization, compliance_check, marketing_planning, facility_launch])
root.order.add_edge(site_assessment, modular_design)
root.order.add_edge(modular_design, env_calibration)
root.order.add_edge(env_calibration, iot_integration)
root.order.add_edge(iot_integration, staff_training)
root.order.add_edge(staff_training, trial_cultivation)
root.order.add_edge(trial_cultivation, yield_optimization)
root.order.add_edge(yield_optimization, compliance_check)
root.order.add_edge(compliance_check, marketing_planning)
root.order.add_edge(marketing_planning, facility_launch)