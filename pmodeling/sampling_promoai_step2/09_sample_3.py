from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
approve = Transition(label='Approve prototype for further development')
build = Transition(label='Build prototype')
collect = Transition(label='Collect feedback from testing phase')
research = Transition(label='Conduct initial research')
feasibility = Transition(label='Conduct feasibility studies')
discard = Transition(label='Discard prototype')
draft = Transition(label='Draft design concepts')
identify = Transition(label='Identify idea for new product or improvement')
refine = Transition(label='Refine prototype')
select = Transition(label='Select promising design')
test_functionality = Transition(label='Test functionality')
test_market = Transition(label='Test market potential')
test_safety = Transition(label='Test safety')

# Define the partial order
root = StrictPartialOrder(nodes=[approve, build, collect, research, feasibility, discard, draft, identify, refine, select, test_functionality, test_market, test_safety])
root.order.add_edge(research, feasibility)
root.order.add_edge(feasibility, identify)
root.order.add_edge(identify, draft)
root.order.add_edge(draft, select)
root.order.add_edge(select, refine)
root.order.add_edge(refine, build)
root.order.add_edge(build, test_functionality)
root.order.add_edge(test_functionality, test_safety)
root.order.add_edge(test_safety, test_market)
root.order.add_edge(test_market, approve)
root.order.add_edge(approve, discard)