from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_audit = Transition(label='Site Audit')
impact_study = Transition(label='Impact Study')
design_modules = Transition(label='Design Modules')
sensor_setup = Transition(label='Sensor Setup')
hydroponics_install = Transition(label='Hydroponics Install')
nutrient_test = Transition(label='Nutrient Test')
lighting_config = Transition(label='Lighting Config')
staff_training = Transition(label='Staff Training')
data_collection = Transition(label='Data Collection')
yield_analysis = Transition(label='Yield Analysis')
pest_control = Transition(label='Pest Control')
harvest_plan = Transition(label='Harvest Plan')
packaging_prep = Transition(label='Packaging Prep')
market_delivery = Transition(label='Market Delivery')
feedback_loop = Transition(label='Feedback Loop')

# Define the loops and XORs
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[impact_study, site_audit])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[data_collection, yield_analysis, pest_control, staff_training])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[packaging_prep, market_delivery, feedback_loop])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[hydroponics_install, lighting_config])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[design_modules, sensor_setup])

# Create the root node
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, xor1, xor2])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop1, xor2)
root.order.add_edge(loop2, xor1)
root.order.add_edge(loop2, xor2)
root.order.add_edge(loop3, xor1)
root.order.add_edge(loop3, xor2)

# Print the root node
print(root)