import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define operators
choice1 = OperatorPOWL(operator=Operator.XOR, children=[flora_mapping, hive_setup])
choice2 = OperatorPOWL(operator=Operator.XOR, children=[pest_control, data_logging])
choice3 = OperatorPOWL(operator=Operator.XOR, children=[workshop_plan, community_meet])
choice4 = OperatorPOWL(operator=Operator.XOR, children=[honey_extract, quality_test])
choice5 = OperatorPOWL(operator=Operator.XOR, children=[packaging, market_setup])
choice6 = OperatorPOWL(operator=Operator.XOR, children=[sales_report, regulation_check])
choice7 = OperatorPOWL(operator=Operator.XOR, children=[waste_manage, seasonal_review])

# Define loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[choice1, choice2, choice3, choice4, choice5, choice6, choice7])

# Define root
root = StrictPartialOrder(nodes=[loop])
root.order.add_edge(loop, choice1)
root.order.add_edge(loop, choice2)
root.order.add_edge(loop, choice3)
root.order.add_edge(loop, choice4)
root.order.add_edge(loop, choice5)
root.order.add_edge(loop, choice6)
root.order.add_edge(loop, choice7)