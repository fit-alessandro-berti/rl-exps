import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
milk_collection = Transition(label='Milk Collection')
quality_testing = Transition(label='Quality Testing')
milk_blending = Transition(label='Milk Blending')
starter_culture = Transition(label='Starter Culture')
fermentation_check = Transition(label='Fermentation Check')
curd_cutting = Transition(label='Curd Cutting')
whey_separation = Transition(label='Whey Separation')
molding_press = Transition(label='Molding Press')
salting_stage = Transition(label='Salting Stage')
aging_control = Transition(label='Aging Control')
packaging_design = Transition(label='Packaging Design')
cold_shipping = Transition(label='Cold Shipping')
compliance_audit = Transition(label='Compliance Audit')
blockchain_log = Transition(label='Blockchain Log')
market_pricing = Transition(label='Market Pricing')
order_fulfillment = Transition(label='Order Fulfillment')
feedback_review = Transition(label='Feedback Review')

# Define the process
root = StrictPartialOrder(
    nodes=[
        milk_collection, quality_testing, milk_blending, starter_culture,
        fermentation_check, curd_cutting, whey_separation, molding_press,
        salting_stage, aging_control, packaging_design, cold_shipping,
        compliance_audit, blockchain_log, market_pricing, order_fulfillment,
        feedback_review
    ],
    order={
        milk_collection: [quality_testing],
        quality_testing: [milk_blending, starter_culture],
        milk_blending: [fermentation_check],
        starter_culture: [fermentation_check],
        fermentation_check: [curd_cutting, whey_separation],
        curd_cutting: [molding_press],
        whey_separation: [salting_stage],
        molding_press: [aging_control],
        salting_stage: [aging_control],
        aging_control: [packaging_design],
        packaging_design: [cold_shipping],
        cold_shipping: [compliance_audit],
        compliance_audit: [blockchain_log],
        blockchain_log: [market_pricing],
        market_pricing: [order_fulfillment],
        order_fulfillment: [feedback_review]
    }
)

# Add edges to the process
for node in root.nodes:
    if node.label in ['Milk Collection', 'Quality Testing', 'Milk Blending', 'Starter Culture', 'Fermentation Check', 'Curd Cutting', 'Whey Separation', 'Molding Press', 'Salting Stage', 'Aging Control', 'Packaging Design', 'Cold Shipping', 'Compliance Audit', 'Blockchain Log', 'Market Pricing', 'Order Fulfillment', 'Feedback Review']:
        root.order.add_edge(node, node)

print(root)