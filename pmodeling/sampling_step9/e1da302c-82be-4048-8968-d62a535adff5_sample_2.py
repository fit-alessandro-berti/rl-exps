import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
sourcing = Transition(label='Colony Sourcing')
design = Transition(label='Hive Design')
survey = Transition(label='Site Survey')
prep = Transition(label='Installation Prep')
setup = Transition(label='Hive Setup')
sensor = Transition(label='Sensor Install')
monitor = Transition(label='Health Monitor')
pest = Transition(label='Pest Control')
harvest = Transition(label='Honey Harvest')
wax = Transition(label='Wax Processing')
package = Transition(label='Product Packaging')
dispatch = Transition(label='Order Dispatch')
workshop = Transition(label='Workshop Setup')
outreach = Transition(label='Community Outreach')
regulation = Transition(label='Regulation Check')
data = Transition(label='Data Analysis')
maintenance = Transition(label='Maintenance Plan')

# Define the silent transitions
skip = SilentTransition()

# Define the exclusive choice operators
choice1 = OperatorPOWL(operator=Operator.XOR, children=[pest, harvest])
choice2 = OperatorPOWL(operator=Operator.XOR, children=[wax, package])
choice3 = OperatorPOWL(operator=Operator.XOR, children=[dispatch, workshop])
choice4 = OperatorPOWL(operator=Operator.XOR, children=[outreach, regulation])
choice5 = OperatorPOWL(operator=Operator.XOR, children=[data, maintenance])

# Define the loop operators
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[choice1])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[choice2])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[choice3])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[choice4])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[choice5])

# Define the root partial order
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5])
root.order.add_edge(loop1, choice1)
root.order.add_edge(loop2, choice2)
root.order.add_edge(loop3, choice3)
root.order.add_edge(loop4, choice4)
root.order.add_edge(loop5, choice5)

# Print the root
print(root)