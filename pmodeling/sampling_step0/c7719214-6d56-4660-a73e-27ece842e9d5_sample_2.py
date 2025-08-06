from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
milk_sourcing = Transition(label='Milk Sourcing')
diet_monitoring = Transition(label='Diet Monitoring')
culture_selection = Transition(label='Culture Selection')
milk_pasteurize = Transition(label='Milk Pasteurize')
curd_cutting = Transition(label='Curd Cutting')
whey_draining = Transition(label='Whey Draining')
mold_inoculate = Transition(label='Mold Inoculate')
press_forming = Transition(label='Press Forming')
salt_application = Transition(label='Salt Application')
aging_setup = Transition(label='Aging Setup')
humidity_control = Transition(label='Humidity Control')
flavor_testing = Transition(label='Flavor Testing')
packaging_design = Transition(label='Packaging Design')
order_processing = Transition(label='Order Processing')
retail_delivery = Transition(label='Retail Delivery')
event_coordination = Transition(label='Event Coordination')
feedback_review = Transition(label='Feedback Review')

# Define the workflow model
root = StrictPartialOrder(
    nodes=[
        milk_sourcing,
        diet_monitoring,
        culture_selection,
        milk_pasteurize,
        curd_cutting,
        whey_draining,
        mold_inoculate,
        press_forming,
        salt_application,
        aging_setup,
        humidity_control,
        flavor_testing,
        packaging_design,
        order_processing,
        retail_delivery,
        event_coordination,
        feedback_review
    ],
    order=[
        (milk_sourcing, diet_monitoring),
        (diet_monitoring, culture_selection),
        (culture_selection, milk_pasteurize),
        (milk_pasteurize, curd_cutting),
        (curd_cutting, whey_draining),
        (whey_draining, mold_inoculate),
        (mold_inoculate, press_forming),
        (press_forming, salt_application),
        (salt_application, aging_setup),
        (aging_setup, humidity_control),
        (humidity_control, flavor_testing),
        (flavor_testing, packaging_design),
        (packaging_design, order_processing),
        (order_processing, retail_delivery),
        (retail_delivery, event_coordination),
        (event_coordination, feedback_review)
    ]
)

# Add a loop for feedback review
loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback_review])
root.order.add_edge(root, loop)

# Add a choice for packaging design
xor = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, SilentTransition()])
root.order.add_edge(root, xor)
root.order.add_edge(xor, feedback_review)

# Return the root node
print(root)