import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
milk_sourcing = Transition(label='Milk Sourcing')
culture_selection = Transition(label='Culture Selection')
milk_pasturize = Transition(label='Milk Pasteurize')
curd_formation = Transition(label='Curd Formation')
whey_separation = Transition(label='Whey Separation')
mold_inoculate = Transition(label='Mold Inoculate')
cheese_pressing = Transition(label='Cheese Pressing')
aging_setup = Transition(label='Aging Setup')
humidity_control = Transition(label='Humidity Control')
flavor_testing = Transition(label='Flavor Testing')
packaging_design = Transition(label='Packaging Design')
label_approval = Transition(label='Label Approval')
order_forecast = Transition(label='Order Forecast')
regulation_audit = Transition(label='Regulation Audit')
waste_recycling = Transition(label='Waste Recycling')
market_delivery = Transition(label='Market Delivery')
customer_feedback = Transition(label='Customer Feedback')

# Define the workflow
root = StrictPartialOrder(
    nodes=[
        milk_sourcing,
        culture_selection,
        milk_pasturize,
        curd_formation,
        whey_separation,
        mold_inoculate,
        cheese_pressing,
        aging_setup,
        humidity_control,
        flavor_testing,
        packaging_design,
        label_approval,
        order_forecast,
        regulation_audit,
        waste_recycling,
        market_delivery,
        customer_feedback
    ],
    order={
        milk_sourcing: [culture_selection],
        culture_selection: [milk_pasturize],
        milk_pasturize: [curd_formation],
        curd_formation: [whey_separation],
        whey_separation: [mold_inoculate],
        mold_inoculate: [cheese_pressing],
        cheese_pressing: [aging_setup],
        aging_setup: [humidity_control],
        humidity_control: [flavor_testing],
        flavor_testing: [packaging_design],
        packaging_design: [label_approval],
        label_approval: [order_forecast],
        order_forecast: [regulation_audit],
        regulation_audit: [waste_recycling],
        waste_recycling: [market_delivery],
        market_delivery: [customer_feedback]
    }
)