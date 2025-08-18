from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the exclusive choice (XOR) for microbial check and customer review
xor = OperatorPOWL(operator=Operator.XOR, children=[microbial_check, customer_review])

# Define the partial order (PO) for the rest of the activities
po = StrictPartialOrder(nodes=[
    milk_sourcing,
    quality_testing,
    curd_processing,
    salt_application,
    mold_inoculation,
    press_molding,
    brine_soaking,
    aging_setup,
    humidity_control,
    xor,
    packaging_design,
    label_printing,
    trace_logging,
    distribution_plan,
    inventory_audit,
    sustainability_audit
])

# Define the order of execution
po.order.add_edge(milk_sourcing, quality_testing)
po.order.add_edge(quality_testing, curd_processing)
po.order.add_edge(curd_processing, salt_application)
po.order.add_edge(salt_application, mold_inoculation)
po.order.add_edge(mold_inoculation, press_molding)
po.order.add_edge(press_molding, brine_soaking)
po.order.add_edge(brine_soaking, aging_setup)
po.order.add_edge(aging_setup, humidity_control)
po.order.add_edge(humidity_control, xor)
po.order.add_edge(xor, packaging_design)
po.order.add_edge(packaging_design, label_printing)
po.order.add_edge(label_printing, trace_logging)
po.order.add_edge(trace_logging, distribution_plan)
po.order.add_edge(distribution_plan, customer_review)
po.order.add_edge(customer_review, inventory_audit)
po.order.add_edge(inventory_audit, sustainability_audit)

# Assign the root
root = po