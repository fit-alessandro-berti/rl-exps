import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Milk_Collection = Transition(label='Milk Collection')
Culture_Prep = Transition(label='Culture Prep')
Curd_Formation = Transition(label='Curd Formation')
Whey_Separation = Transition(label='Whey Separation')
Molding_Cheese = Transition(label='Molding Cheese')
Salting_Process = Transition(label='Salting Process')
Initial_Aging = Transition(label='Initial Aging')
Humidity_Control = Transition(label='Humidity Control')
Temperature_Check = Transition(label='Temperature Check')
Flavor_Testing = Transition(label='Flavor Testing')
Final_Aging = Transition(label='Final Aging')
Packaging_Artisanal = Transition(label='Packaging Artisanal')
Label_Printing = Transition(label='Label Printing')
Inventory_Audit = Transition(label='Inventory Audit')
Order_Fulfillment = Transition(label='Order Fulfillment')
Subscription_Setup = Transition(label='Subscription Setup')
Event_Marketing = Transition(label='Event Marketing')

skip = SilentTransition()

# Define sub-processes
culture_prep_and_curd_form = OperatorPOWL(operator=Operator.XOR, children=[Culture_Prep, Curd_Formation])
molding_and_salting = OperatorPOWL(operator=Operator.XOR, children=[Molding_Cheese, Salting_Process])
initial_aging_and_humidity_control = OperatorPOWL(operator=Operator.XOR, children=[Initial_Aging, Humidity_Control])
temperature_check_and_flavor_testing = OperatorPOWL(operator=Operator.XOR, children=[Temperature_Check, Flavor_Testing])
final_aging = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])
packaging_and_label_printing = OperatorPOWL(operator=Operator.XOR, children=[Packaging_Artisanal, Label_Printing])

# Define loops and exclusive choices
culture_prep_loop = OperatorPOWL(operator=Operator.LOOP, children=[culture_prep_and_curd_form])
molding_and_salting_loop = OperatorPOWL(operator=Operator.LOOP, children=[molding_and_salting])
initial_aging_and_humidity_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[initial_aging_and_humidity_control])
temperature_check_and_flavor_testing_loop = OperatorPOWL(operator=Operator.LOOP, children=[temperature_check_and_flavor_testing])
final_aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[final_aging])
packaging_and_label_printing_loop = OperatorPOWL(operator=Operator.LOOP, children=[packaging_and_label_printing])

# Define the main process
root = StrictPartialOrder(nodes=[
    Milk_Collection,
    culture_prep_loop,
    molding_and_salting_loop,
    initial_aging_and_humidity_control_loop,
    temperature_check_and_flavor_testing_loop,
    final_aging_loop,
    packaging_and_label_printing_loop,
    Inventory_Audit,
    Order_Fulfillment,
    Subscription_Setup,
    Event_Marketing
])

# Add dependencies between nodes
root.order.add_edge(Milk_Collection, culture_prep_loop)
root.order.add_edge(culture_prep_loop, molding_and_salting_loop)
root.order.add_edge(molding_and_salting_loop, initial_aging_and_humidity_control_loop)
root.order.add_edge(initial_aging_and_humidity_control_loop, temperature_check_and_flavor_testing_loop)
root.order.add_edge(temperature_check_and_flavor_testing_loop, final_aging_loop)
root.order.add_edge(final_aging_loop, packaging_and_label_printing_loop)
root.order.add_edge(packaging_and_label_printing_loop, Inventory_Audit)
root.order.add_edge(Inventory_Audit, Order_Fulfillment)
root.order.add_edge(Order_Fulfillment, Subscription_Setup)
root.order.add_edge(Subscription_Setup, Event_Marketing)

print(root)