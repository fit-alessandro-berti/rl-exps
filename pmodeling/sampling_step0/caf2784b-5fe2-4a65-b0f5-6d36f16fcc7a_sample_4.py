import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions (if any)
skip = SilentTransition()

# Define operators for choices and loops
xor = OperatorPOWL(operator=Operator.XOR, children=[impact_study, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[design_modules, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[sensor_setup, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[hydroponics_install, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[nutrient_test, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[lighting_config, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[staff_training, skip])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[data_collection, skip])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[yield_analysis, skip])
xor10 = OperatorPOWL(operator=Operator.XOR, children=[pest_control, skip])
xor11 = OperatorPOWL(operator=Operator.XOR, children=[harvest_plan, skip])
xor12 = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, skip])
xor13 = OperatorPOWL(operator=Operator.XOR, children=[market_delivery, skip])

# Define loop for staff training
loop_staff_training = OperatorPOWL(operator=Operator.LOOP, children=[staff_training, feedback_loop])

# Define loop for yield analysis
loop_yield_analysis = OperatorPOWL(operator=Operator.LOOP, children=[yield_analysis, feedback_loop])

# Define the root POWL model
root = StrictPartialOrder(nodes=[site_audit, xor, xor2, xor3, xor4, xor5, xor6, loop_staff_training, xor7, xor8, loop_yield_analysis, xor9, xor10, xor11, xor12, xor13])
root.order.add_edge(site_audit, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, loop_staff_training)
root.order.add_edge(loop_staff_training, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, loop_yield_analysis)
root.order.add_edge(loop_yield_analysis, xor9)
root.order.add_edge(xor9, xor10)
root.order.add_edge(xor10, xor11)
root.order.add_edge(xor11, xor12)
root.order.add_edge(xor12, xor13)

print(root)