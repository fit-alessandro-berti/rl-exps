import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their names
activities = {
    'Milk Sourcing': Transition(label='Milk Sourcing'),
    'Culture Selection': Transition(label='Culture Selection'),
    'Milk Pasteurize': Transition(label='Milk Pasteurize'),
    'Curd Formation': Transition(label='Curd Formation'),
    'Whey Separation': Transition(label='Whey Separation'),
    'Mold Inoculate': Transition(label='Mold Inoculate'),
    'Cheese Pressing': Transition(label='Cheese Pressing'),
    'Aging Setup': Transition(label='Aging Setup'),
    'Humidity Control': Transition(label='Humidity Control'),
    'Flavor Testing': Transition(label='Flavor Testing'),
    'Packaging Design': Transition(label='Packaging Design'),
    'Label Approval': Transition(label='Label Approval'),
    'Order Forecast': Transition(label='Order Forecast'),
    'Regulation Audit': Transition(label='Regulation Audit'),
    'Waste Recycling': Transition(label='Waste Recycling'),
    'Market Delivery': Transition(label='Market Delivery'),
    'Customer Feedback': Transition(label='Customer Feedback')
}

# Define the partial order (POWL model)
root = StrictPartialOrder(
    nodes=[
        activities['Milk Sourcing'],
        activities['Culture Selection'],
        activities['Milk Pasteurize'],
        activities['Curd Formation'],
        activities['Whey Separation'],
        activities['Mold Inoculate'],
        activities['Cheese Pressing'],
        activities['Aging Setup'],
        activities['Humidity Control'],
        activities['Flavor Testing'],
        activities['Packaging Design'],
        activities['Label Approval'],
        activities['Order Forecast'],
        activities['Regulation Audit'],
        activities['Waste Recycling'],
        activities['Market Delivery'],
        activities['Customer Feedback']
    ],
    order={
        activities['Milk Sourcing']: [activities['Culture Selection']],
        activities['Culture Selection']: [activities['Milk Pasteurize']],
        activities['Milk Pasteurize']: [activities['Curd Formation']],
        activities['Curd Formation']: [activities['Whey Separation']],
        activities['Whey Separation']: [activities['Mold Inoculate']],
        activities['Mold Inoculate']: [activities['Cheese Pressing']],
        activities['Cheese Pressing']: [activities['Aging Setup']],
        activities['Aging Setup']: [activities['Humidity Control']],
        activities['Humidity Control']: [activities['Flavor Testing']],
        activities['Flavor Testing']: [activities['Packaging Design']],
        activities['Packaging Design']: [activities['Label Approval']],
        activities['Label Approval']: [activities['Order Forecast']],
        activities['Order Forecast']: [activities['Regulation Audit']],
        activities['Regulation Audit']: [activities['Waste Recycling']],
        activities['Waste Recycling']: [activities['Market Delivery']],
        activities['Market Delivery']: [activities['Customer Feedback']]
    }
)