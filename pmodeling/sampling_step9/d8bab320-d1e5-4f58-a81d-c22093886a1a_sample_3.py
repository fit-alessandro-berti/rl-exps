import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) in the POWL model
Milk_Sourcing = Transition(label='Milk Sourcing')
Culture_Selection = Transition(label='Culture Selection')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Curd_Formation = Transition(label='Curd Formation')
Whey_Separation = Transition(label='Whey Separation')
Mold_Inoculate = Transition(label='Mold Inoculate')
Cheese_Pressing = Transition(label='Cheese Pressing')
Aging_Setup = Transition(label='Aging Setup')
Humidity_Control = Transition(label='Humidity Control')
Flavor_Testing = Transition(label='Flavor Testing')
Packaging_Design = Transition(label='Packaging Design')
Label_Approval = Transition(label='Label Approval')
Order_Forecast = Transition(label='Order Forecast')
Regulation_Audit = Transition(label='Regulation Audit')
Waste_Recycling = Transition(label='Waste Recycling')
Market_Delivery = Transition(label='Market Delivery')
Customer_Feedback = Transition(label='Customer Feedback')

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[Aging_Setup, Humidity_Control, Flavor_Testing])
waste_loop = OperatorPOWL(operator=Operator.LOOP, children=[Waste_Recycling])

# Define XOR nodes
sensory_analysis = OperatorPOWL(operator=Operator.XOR, children=[Flavor_Testing, skip])
regulatory_check = OperatorPOWL(operator=Operator.XOR, children=[Regulation_Audit, skip])
seasonal_demand = OperatorPOWL(operator=Operator.XOR, children=[Order_Forecast, skip])
custom_order = OperatorPOWL(operator=Operator.XOR, children=[Market_Delivery, skip])
customer_innovation = OperatorPOWL(operator=Operator.XOR, children=[Customer_Feedback, skip])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[aging_loop, waste_loop, sensory_analysis, regulatory_check, seasonal_demand, custom_order, customer_innovation])
root.order.add_edge(aging_loop, sensory_analysis)
root.order.add_edge(aging_loop, regulatory_check)
root.order.add_edge(aging_loop, seasonal_demand)
root.order.add_edge(aging_loop, custom_order)
root.order.add_edge(aging_loop, customer_innovation)
root.order.add_edge(waste_loop, sensory_analysis)
root.order.add_edge(waste_loop, regulatory_check)
root.order.add_edge(waste_loop, seasonal_demand)
root.order.add_edge(waste_loop, custom_order)
root.order.add_edge(waste_loop, customer_innovation)

# Save the final result in the variable 'root'