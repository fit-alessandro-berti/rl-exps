from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
sensor_deploy = Transition(label='Sensor Deploy')
crop_select = Transition(label='Crop Select')
system_install = Transition(label='System Install')
energy_setup = Transition(label='Energy Setup')
water_cycle = Transition(label='Water Cycle')
pest_control = Transition(label='Pest Control')
regulatory_check = Transition(label='Regulatory Check')
staff_training = Transition(label='Staff Training')
data_configure = Transition(label='Data Configure')
supply_plan = Transition(label='Supply Plan')
harvest_schedule = Transition(label='Harvest Schedule')
quality_audit = Transition(label='Quality Audit')
market_launch = Transition(label='Market Launch')
feedback_loop = Transition(label='Feedback Loop')

# Create the process tree structure
site_survey_process = StrictPartialOrder(nodes=[site_survey])
design_layout_process = StrictPartialOrder(nodes=[design_layout])
sensor_deploy_process = StrictPartialOrder(nodes=[sensor_deploy])
crop_select_process = StrictPartialOrder(nodes=[crop_select])
system_install_process = StrictPartialOrder(nodes=[system_install])
energy_setup_process = StrictPartialOrder(nodes=[energy_setup])
water_cycle_process = StrictPartialOrder(nodes=[water_cycle])
pest_control_process = StrictPartialOrder(nodes=[pest_control])
regulatory_check_process = StrictPartialOrder(nodes=[regulatory_check])
staff_training_process = StrictPartialOrder(nodes=[staff_training])
data_configure_process = StrictPartialOrder(nodes=[data_configure])
supply_plan_process = StrictPartialOrder(nodes=[supply_plan])
harvest_schedule_process = StrictPartialOrder(nodes=[harvest_schedule])
quality_audit_process = StrictPartialOrder(nodes=[quality_audit])
market_launch_process = StrictPartialOrder(nodes=[market_launch])
feedback_loop_process = StrictPartialOrder(nodes=[feedback_loop])

# Define the dependencies
root = StrictPartialOrder(nodes=[
    site_survey_process, design_layout_process, sensor_deploy_process, crop_select_process, system_install_process,
    energy_setup_process, water_cycle_process, pest_control_process, regulatory_check_process, staff_training_process,
    data_configure_process, supply_plan_process, harvest_schedule_process, quality_audit_process, market_launch_process,
    feedback_loop_process
])
root.order.add_edge(site_survey_process, design_layout_process)
root.order.add_edge(design_layout_process, sensor_deploy_process)
root.order.add_edge(sensor_deploy_process, crop_select_process)
root.order.add_edge(crop_select_process, system_install_process)
root.order.add_edge(system_install_process, energy_setup_process)
root.order.add_edge(energy_setup_process, water_cycle_process)
root.order.add_edge(water_cycle_process, pest_control_process)
root.order.add_edge(pest_control_process, regulatory_check_process)
root.order.add_edge(regulatory_check_process, staff_training_process)
root.order.add_edge(staff_training_process, data_configure_process)
root.order.add_edge(data_configure_process, supply_plan_process)
root.order.add_edge(supply_plan_process, harvest_schedule_process)
root.order.add_edge(harvest_schedule_process, quality_audit_process)
root.order.add_edge(quality_audit_process, market_launch_process)
root.order.add_edge(market_launch_process, feedback_loop_process)