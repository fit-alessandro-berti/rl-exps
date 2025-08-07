import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the root of the POWL model
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

# Add dependencies if any are present (as per the process description)
# In this case, the process is sequential and no dependencies are explicitly mentioned
# So, we don't need to add any dependencies here.

print(root)