import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL nodes
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
curd_processing = Transition(label='Curd Processing')
salt_application = Transition(label='Salt Application')
mold_inoculation = Transition(label='Mold Inoculation')
press_molding = Transition(label='Press Molding')
brine_soaking = Transition(label='Brine Soaking')
aging_setup = Transition(label='Aging Setup')
humidity_control = Transition(label='Humidity Control')
microbial_check = Transition(label='Microbial Check')
packaging_design = Transition(label='Packaging Design')
label_printing = Transition(label='Label Printing')
trace_logging = Transition(label='Trace Logging')
distribution_plan = Transition(label='Distribution Plan')
customer_review = Transition(label='Customer Review')
inventory_audit = Transition(label='Inventory Audit')
sustainability_audit = Transition(label='Sustainability Audit')

# Define the POWL operators
choice_1 = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])
choice_2 = OperatorPOWL(operator=Operator.XOR, children=[curd_processing, salt_application])
choice_3 = OperatorPOWL(operator=Operator.XOR, children=[mold_inoculation, press_molding])
choice_4 = OperatorPOWL(operator=Operator.XOR, children=[brine_soaking, aging_setup])
choice_5 = OperatorPOWL(operator=Operator.XOR, children=[humidity_control, microbial_check])
choice_6 = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, label_printing])
choice_7 = OperatorPOWL(operator=Operator.XOR, children=[trace_logging, distribution_plan])
choice_8 = OperatorPOWL(operator=Operator.XOR, children=[customer_review, inventory_audit])
choice_9 = OperatorPOWL(operator=Operator.XOR, children=[sustainability_audit, None])

# Define the root POWL
root = StrictPartialOrder(nodes=[choice_1, choice_2, choice_3, choice_4, choice_5, choice_6, choice_7, choice_8, choice_9])
root.order.add_edge(choice_1, choice_2)
root.order.add_edge(choice_2, choice_3)
root.order.add_edge(choice_3, choice_4)
root.order.add_edge(choice_4, choice_5)
root.order.add_edge(choice_5, choice_6)
root.order.add_edge(choice_6, choice_7)
root.order.add_edge(choice_7, choice_8)
root.order.add_edge(choice_8, choice_9)

print(root)