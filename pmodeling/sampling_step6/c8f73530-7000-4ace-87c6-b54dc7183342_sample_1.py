import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) using the exact names provided
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
milk_pasturize = Transition(label='Milk Pasteurize')
culture_inoculate = Transition(label='Culture Inoculate')
coagulation = Transition(label='Coagulation')
curd_cutting = Transition(label='Curd Cutting')
whey_drain = Transition(label='Whey Drain')
pressing = Transition(label='Pressing')
salting = Transition(label='Salting')
aging_control = Transition(label='Aging Control')
sensory_audit = Transition(label='Sensory Audit')
packaging_design = Transition(label='Packaging Design')
label_approval = Transition(label='Label Approval')
order_customization = Transition(label='Order Customization')
logistics_plan = Transition(label='Logistics Plan')
market_delivery = Transition(label='Market Delivery')
customer_feedback = Transition(label='Customer Feedback')
regulatory_check = Transition(label='Regulatory Check')

# Define the partial order model
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    quality_testing,
    milk_pasturize,
    culture_inoculate,
    coagulation,
    curd_cutting,
    whey_drain,
    pressing,
    salting,
    aging_control,
    sensory_audit,
    packaging_design,
    label_approval,
    order_customization,
    logistics_plan,
    market_delivery,
    customer_feedback,
    regulatory_check
])

# Add dependencies between nodes (if any)
# In this example, there are no explicit dependencies mentioned, so we don't add any edges.

# The 'root' variable now contains the POWL model for the process