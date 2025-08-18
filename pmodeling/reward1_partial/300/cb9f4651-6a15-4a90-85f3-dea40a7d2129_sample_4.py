from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions for each activity
milk_sourcing = Transition(label='Milk Sourcing')
culture_prep = Transition(label='Culture Prep')
milk_pasturize = Transition(label='Milk Pasteurize')
milk_inoculate = Transition(label='Milk Inoculate')
curd_form = Transition(label='Curd Formation')
curd_cut = Transition(label='Curd Cut')
whey_drain = Transition(label='Whey Drain')
mold_inoculate = Transition(label='Mold Inoculate')
press_cheese = Transition(label='Press Cheese')
aging_setup = Transition(label='Aging Setup')
humidity_control = Transition(label='Humidity Control')
temp_monitor = Transition(label='Temperature Monitor')
quality_test = Transition(label='Quality Test')
packaging = Transition(label='Packaging')
order_fulfill = Transition(label='Order Fulfill')
retail_deliver = Transition(label='Retail Deliver')
feedback_collect = Transition(label='Feedback Collect')

# Define loops for aging and quality testing
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_setup, humidity_control, temp_monitor, quality_test])
quality_loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_test])

# Define XOR for packaging and order fulfillment
xor = OperatorPOWL(operator=Operator.XOR, children=[packaging, order_fulfill])

# Define root model with dependencies
root = StrictPartialOrder(nodes=[milk_sourcing, culture_prep, milk_pasturize, milk_inoculate, curd_form, curd_cut, whey_drain, mold_inoculate, press_cheese, aging_loop, quality_loop, xor])
root.order.add_edge(milk_sourcing, culture_prep)
root.order.add_edge(culture_prep, milk_pasturize)
root.order.add_edge(milk_pasturize, milk_inoculate)
root.order.add_edge(milk_inoculate, curd_form)
root.order.add_edge(curd_form, curd_cut)
root.order.add_edge(curd_cut, whey_drain)
root.order.add_edge(whey_drain, mold_inoculate)
root.order.add_edge(mold_inoculate, press_cheese)
root.order.add_edge(press_cheese, aging_loop)
root.order.add_edge(aging_loop, quality_loop)
root.order.add_edge(quality_loop, xor)

# Add dependencies for XOR
root.order.add_edge(aging_loop, packaging)
root.order.add_edge(aging_loop, order_fulfill)
root.order.add_edge(quality_loop, packaging)
root.order.add_edge(quality_loop, order_fulfill)
root.order.add_edge(xor, retail_deliver)
root.order.add_edge(xor, feedback_collect)

print(root)