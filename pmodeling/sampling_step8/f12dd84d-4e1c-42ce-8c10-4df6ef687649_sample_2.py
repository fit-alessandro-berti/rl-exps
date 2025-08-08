from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

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

# Define the exclusive choice operator for microbial testing
microbial_test_choice = OperatorPOWL(operator=Operator.XOR, children=[microbial_check, SilentTransition()])

# Define the loop operator for aging setup
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_setup, humidity_control])

# Define the root node and add the defined transitions and control-flow operators as children
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    quality_testing,
    curd_processing,
    salt_application,
    mold_inoculation,
    press_molding,
    brine_soaking,
    aging_loop,
    microbial_test_choice,
    packaging_design,
    label_printing,
    trace_logging,
    distribution_plan,
    customer_review,
    inventory_audit,
    sustainability_audit
])

# Add the necessary dependencies between the nodes
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, curd_processing)
root.order.add_edge(curd_processing, salt_application)
root.order.add_edge(salt_application, mold_inoculation)
root.order.add_edge(mold_inoculation, press_molding)
root.order.add_edge(press_molding, brine_soaking)
root.order.add_edge(brine_soaking, aging_loop)
root.order.add_edge(aging_loop, microbial_test_choice)
root.order.add_edge(microbial_test_choice, packaging_design)
root.order.add_edge(packaging_design, label_printing)
root.order.add_edge(label_printing, trace_logging)
root.order.add_edge(trace_logging, distribution_plan)
root.order.add_edge(distribution_plan, customer_review)
root.order.add_edge(customer_review, inventory_audit)
root.order.add_edge(inventory_audit, sustainability_audit)

# Print the root node
print(root)