import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a Transition
site_survey = Transition(label='Site Survey')
climate_study = Transition(label='Climate Study')
design_layout = Transition(label='Design Layout')
system_install = Transition(label='System Install')
crop_select = Transition(label='Crop Select')
nutrient_plan = Transition(label='Nutrient Plan')
sensor_setup = Transition(label='Sensor Setup')
automation_test = Transition(label='Automation Test')
staff_train = Transition(label='Staff Train')
compliance_check = Transition(label='Compliance Check')
marketing_sync = Transition(label='Marketing Sync')
data_monitor = Transition(label='Data Monitor')
yield_analyze = Transition(label='Yield Analyze')
supply_chain = Transition(label='Supply Chain')
customer_engage = Transition(label='Customer Engage')

# Define the root Partial Order with all activities as children
root = StrictPartialOrder(nodes=[
    site_survey, climate_study, design_layout, system_install, crop_select, nutrient_plan, sensor_setup,
    automation_test, staff_train, compliance_check, marketing_sync, data_monitor, yield_analyze, supply_chain,
    customer_engage
])