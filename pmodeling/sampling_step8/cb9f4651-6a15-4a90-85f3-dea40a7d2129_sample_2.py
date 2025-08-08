from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
milk_sourcing = Transition(label='Milk Sourcing')
culture_prep = Transition(label='Culture Prep')
milk_pasteurize = Transition(label='Milk Pasteurize')
milk_inoculate = Transition(label='Milk Inoculate')
curd_form = Transition(label='Curd Formation')
curd_cut = Transition(label='Curd Cut')
whey_drain = Transition(label='Whey Drain')
mold_inoculate = Transition(label='Mold Inoculate')
press_cheese = Transition(label='Press Cheese')
aging_setup = Transition(label='Aging Setup')
humidity_control = Transition(label='Humidity Control')
temperature_monitor = Transition(label='Temperature Monitor')
quality_test = Transition(label='Quality Test')
packaging = Transition(label='Packaging')
order_fulfill = Transition(label='Order Fulfill')
retail_deliver = Transition(label='Retail Deliver')
feedback_collect = Transition(label='Feedback Collect')

# Define the workflow
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    culture_prep,
    milk_pasteurize,
    milk_inoculate,
    curd_form,
    curd_cut,
    whey_drain,
    mold_inoculate,
    press_cheese,
    aging_setup,
    humidity_control,
    temperature_monitor,
    quality_test,
    packaging,
    order_fulfill,
    retail_deliver,
    feedback_collect
])

# Define the dependencies
root.order.add_edge(milk_sourcing, culture_prep)
root.order.add_edge(culture_prep, milk_pasteurize)
root.order.add_edge(milk_pasteurize, milk_inoculate)
root.order.add_edge(milk_inoculate, curd_form)
root.order.add_edge(curd_form, curd_cut)
root.order.add_edge(curd_cut, whey_drain)
root.order.add_edge(whey_drain, mold_inoculate)
root.order.add_edge(mold_inoculate, press_cheese)
root.order.add_edge(press_cheese, aging_setup)
root.order.add_edge(aging_setup, humidity_control)
root.order.add_edge(humidity_control, temperature_monitor)
root.order.add_edge(temperature_monitor, quality_test)
root.order.add_edge(quality_test, packaging)
root.order.add_edge(packaging, order_fulfill)
root.order.add_edge(order_fulfill, retail_deliver)
root.order.add_edge(retail_deliver, feedback_collect)

print(root)