import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
flora_mapping = Transition(label='Flora Mapping')
hive_setup = Transition(label='Hive Setup')
sensor_install = Transition(label='Sensor Install')
health_check = Transition(label='Health Check')
pest_control = Transition(label='Pest Control')
data_logging = Transition(label='Data Logging')
community_meet = Transition(label='Community Meet')
workshop_plan = Transition(label='Workshop Plan')
honey_extract = Transition(label='Honey Extract')
quality_test = Transition(label='Quality Test')
packaging = Transition(label='Packaging')
market_setup = Transition(label='Market Setup')
sales_report = Transition(label='Sales Report')
regulation_check = Transition(label='Regulation Check')
waste_manage = Transition(label='Waste Manage')
seasonal_review = Transition(label='Seasonal Review')

# Define the root node with all activities
root = StrictPartialOrder(nodes=[
    site_survey, flora_mapping, hive_setup, sensor_install, health_check, pest_control,
    data_logging, community_meet, workshop_plan, honey_extract, quality_test, packaging,
    market_setup, sales_report, regulation_check, waste_manage, seasonal_review
])
# Since there are no dependencies between activities in this process, the order is not explicitly defined.
# However, if there were dependencies, they would be added to the 'order' attribute of the root node.

# The final POWL model is defined and saved in the variable 'root'.