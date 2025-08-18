import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the operators
xor = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[curd_processing, salt_application])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[mold_inoculation, press_molding])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[brine_soaking, aging_setup])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[humidity_control, microbial_check])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, label_printing])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[trace_logging, distribution_plan])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[customer_review, inventory_audit])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[sustainability_audit])

# Define the partial order
root = StrictPartialOrder(nodes=[xor, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9])
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor9)