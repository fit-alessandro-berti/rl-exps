import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
starter_prep = Transition(label='Starter Prep')
curd_cutting = Transition(label='Curd Cutting')
whey_draining = Transition(label='Whey Draining')
molding_press = Transition(label='Molding Press')
fermentation_control = Transition(label='Fermentation Control')
aging_setup = Transition(label='Aging Setup')
humidity_check = Transition(label='Humidity Check')
packaging_design = Transition(label='Packaging Design')
label_approval = Transition(label='Label Approval')
inventory_audit = Transition(label='Inventory Audit')
order_scheduling = Transition(label='Order Scheduling')
market_delivery = Transition(label='Market Delivery')
feedback_review = Transition(label='Feedback Review')
compliance_check = Transition(label='Compliance Check')
marketing_sync = Transition(label='Marketing Sync')

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        milk_sourcing,
        quality_testing,
        starter_prep,
        curd_cutting,
        whey_draining,
        molding_press,
        fermentation_control,
        aging_setup,
        humidity_check,
        packaging_design,
        label_approval,
        inventory_audit,
        order_scheduling,
        market_delivery,
        feedback_review,
        compliance_check,
        marketing_sync
    ],
    order=[
        (milk_sourcing, quality_testing),
        (quality_testing, starter_prep),
        (starter_prep, curd_cutting),
        (curd_cutting, whey_draining),
        (whey_draining, molding_press),
        (molding_press, fermentation_control),
        (fermentation_control, aging_setup),
        (aging_setup, humidity_check),
        (humidity_check, packaging_design),
        (packaging_design, label_approval),
        (label_approval, inventory_audit),
        (inventory_audit, order_scheduling),
        (order_scheduling, market_delivery),
        (market_delivery, feedback_review),
        (feedback_review, compliance_check),
        (compliance_check, marketing_sync)
    ]
)

print(root)