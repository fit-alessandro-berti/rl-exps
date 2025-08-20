import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
idea = Transition(label='Identify idea for new product or improvement')
research = Transition(label='Conduct initial research')
feasibility = Transition(label='Conduct feasibility studies')
design = Transition(label='Draft design concepts')
select = Transition(label='Select promising design')
build = Transition(label='Build prototype')
test_functionality = Transition(label='Test functionality')
test_safety = Transition(label='Test safety')
test_market = Transition(label='Test market potential')
feedback = Transition(label='Collect feedback from testing phase')
refine = Transition(label='Refine prototype')
approve = Transition(label='Approve prototype for further development')
discard = Transition(label='Discard prototype')

# Define the loop for the testing and refinement phases
test_loop = OperatorPOWL(operator=Operator.LOOP, children=[test_functionality, test_safety, test_market, feedback, refine])

# Define the choice between approving or discarding the prototype
choice = OperatorPOWL(operator=Operator.XOR, children=[approve, discard])

# Define the overall process structure
root = StrictPartialOrder(nodes=[idea, research, feasibility, design, select, build, test_loop, choice])

# Define the order of activities
root.order.add_edge(idea, research)
root.order.add_edge(research, feasibility)
root.order.add_edge(feasibility, design)
root.order.add_edge(design, select)
root.order.add_edge(select, build)
root.order.add_edge(build, test_loop)
root.order.add_edge(test_loop, choice)