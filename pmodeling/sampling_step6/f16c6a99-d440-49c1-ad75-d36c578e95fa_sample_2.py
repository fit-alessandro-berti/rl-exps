import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    sensor_deploy,
    crop_select,
    system_install,
    energy_setup,
    water_cycle,
    pest_control,
    regulatory_check,
    staff_training,
    data_configure,
    supply_plan,
    harvest_schedule,
    quality_audit,
    market_launch,
    feedback_loop
])

# Add dependencies if any (for example, assuming sequential execution)
# For simplicity, we'll just add the dependencies as they appear in the process description
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(site_survey, sensor_deploy)
root.order.add_edge(site_survey, crop_select)
root.order.add_edge(site_survey, system_install)
root.order.add_edge(site_survey, energy_setup)
root.order.add_edge(site_survey, water_cycle)
root.order.add_edge(site_survey, pest_control)
root.order.add_edge(site_survey, regulatory_check)
root.order.add_edge(site_survey, staff_training)
root.order.add_edge(site_survey, data_configure)
root.order.add_edge(site_survey, supply_plan)
root.order.add_edge(site_survey, harvest_schedule)
root.order.add_edge(site_survey, quality_audit)
root.order.add_edge(site_survey, market_launch)
root.order.add_edge(site_survey, feedback_loop)

# Print the root (POWL model) for verification
print(root)