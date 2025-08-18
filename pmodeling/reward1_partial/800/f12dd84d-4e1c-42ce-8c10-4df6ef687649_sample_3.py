import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
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

# Define silent transitions (if any)
skip = SilentTransition()

# Define loops and choices
# For simplicity, we will assume that some activities are executed in a specific order and others are concurrent.
# This is a simplification and may not reflect the exact process flow accurately.

# Example: Quality Testing is a silent transition (if it's not directly connected to other activities)
quality_testing_loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_testing])

# Example: Curd Processing and Salt Application are concurrent activities
curd_and_salt = OperatorPOWL(operator=Operator.XOR, children=[curd_processing, salt_application])

# Example: Mold Inoculation and Press Molding are concurrent activities
mold_and_press = OperatorPOWL(operator=Operator.XOR, children=[mold_inoculation, press_molding])

# Example: Brine Soaking and Aging Setup are concurrent activities
brine_and_aging = OperatorPOWL(operator=Operator.XOR, children=[brine_soaking, aging_setup])

# Example: Humidity Control and Microbial Check are concurrent activities
humidity_and_microbial = OperatorPOWL(operator=Operator.XOR, children=[humidity_control, microbial_check])

# Example: Packaging Design and Label Printing are concurrent activities
packaging_and_label = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, label_printing])

# Example: Trace Logging and Distribution Plan are concurrent activities
trace_and_distribution = OperatorPOWL(operator=Operator.XOR, children=[trace_logging, distribution_plan])

# Example: Customer Review and Inventory Audit are concurrent activities
review_and_audit = OperatorPOWL(operator=Operator.XOR, children=[customer_review, inventory_audit])

# Example: Sustainability Audit is a silent transition (if it's not directly connected to other activities)
sustainability_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[sustainability_audit])

# Root node representing the entire process
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    quality_testing_loop,
    curd_and_salt,
    mold_and_press,
    brine_and_aging,
    humidity_and_microbial,
    packaging_and_label,
    trace_and_distribution,
    review_and_audit,
    sustainability_audit_loop
])

# Define dependencies between nodes
root.order.add_edge(milk_sourcing, quality_testing_loop)
root.order.add_edge(quality_testing_loop, curd_and_salt)
root.order.add_edge(curd_and_salt, mold_and_press)
root.order.add_edge(mold_and_press, brine_and_aging)
root.order.add_edge(brine_and_aging, humidity_and_microbial)
root.order.add_edge(humidity_and_microbial, packaging_and_label)
root.order.add_edge(packaging_and_label, trace_and_distribution)
root.order.add_edge(trace_and_distribution, review_and_audit)
root.order.add_edge(review_and_audit, sustainability_audit_loop)

print(root)