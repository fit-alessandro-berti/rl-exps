import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
from pm4py.objects.petri_net.obj import PetriNet, Marking
from pm4py.objects.petri_net.utils import petri_utils
from pm4py.objects.petri_net.utils.petri_utils import create_transition, create_place, create_arc
from pm4py.objects.petri_net.utils.petri_utils import create_loop, create_xor, create_and, create_transition_with_label
from pm4py.objects.petri_net.utils.petri_utils import create_arc_with_label

# Create the activities
approve_prototype = Transition(label='Approve prototype for further development')
build_prototype = Transition(label='Build prototype')
collect_feedback = Transition(label='Collect feedback from testing phase')
conduct_feasibility = Transition(label='Conduct feasibility studies')
conduct_research = Transition(label='Conduct initial research')
discard_prototype = Transition(label='Discard prototype')
draft_concepts = Transition(label='Draft design concepts')
identify_idea = Transition(label='Identify idea for new product or improvement')
refine_prototype = Transition(label='Refine prototype')
select_design = Transition(label='Select promising design')
test_functionality = Transition(label='Test functionality')
test_market = Transition(label='Test market potential')
test_safety = Transition(label='Test safety')

# Create the silent transitions
skip = SilentTransition()

# Create the loop and XOR nodes
loop = OperatorPOWL(operator=Operator.LOOP, children=[test_functionality, test_market, test_safety])
xor = OperatorPOWL(operator=Operator.XOR, children=[refine_prototype, skip])

# Create the root POWL model
root = StrictPartialOrder(nodes=[conduct_research, conduct_feasibility, draft_concepts, select_design, build_prototype, loop, xor, approve_prototype, discard_prototype])
root.order.add_edge(conduct_research, conduct_feasibility)
root.order.add_edge(conduct_feasibility, draft_concepts)
root.order.add_edge(draft_concepts, select_design)
root.order.add_edge(select_design, build_prototype)
root.order.add_edge(build_prototype, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, approve_prototype)
root.order.add_edge(xor, discard_prototype)
root.order.add_edge(approve_prototype, conduct_feasibility)
root.order.add_edge(approve_prototype, draft_concepts)
root.order.add_edge(approve_prototype, select_design)
root.order.add_edge(approve_prototype, build_prototype)
root.order.add_edge(discard_prototype, conduct_feasibility)
root.order.add_edge(discard_prototype, draft_concepts)
root.order.add_edge(discard_prototype, select_design)
root.order.add_edge(discard_prototype, build_prototype)