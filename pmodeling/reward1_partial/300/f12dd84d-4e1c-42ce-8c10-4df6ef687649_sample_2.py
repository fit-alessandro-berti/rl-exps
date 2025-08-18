import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the loop and exclusive choice operators
loop = OperatorPOWL(operator=Operator.LOOP, children=[milk_sourcing, quality_testing, curd_processing, salt_application, mold_inoculation, press_molding, brine_soaking, aging_setup, humidity_control, microbial_check, packaging_design, label_printing, trace_logging, distribution_plan, customer_review, inventory_audit, sustainability_audit])
xor = OperatorPOWL(operator=Operator.XOR, children=[sustainability_audit, inventory_audit, trace_logging, label_printing, packaging_design, distribution_plan, customer_review, microbial_check, aging_setup, humidity_control, press_molding, brine_soaking, mold_inoculation, salt_application, curd_processing, quality_testing, milk_sourcing])

# Define the root node with the defined transitions and operators
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Print the root node
print(root)