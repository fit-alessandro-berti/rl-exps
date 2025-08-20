import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
identify_idea = Transition(label='Identify idea for new product or improvement')
conduct_research = Transition(label='Conduct initial research')
conduct_studies = Transition(label='Conduct feasibility studies')
draft_concepts = Transition(label='Draft design concepts')
select_design = Transition(label='Select promising design')
build_prototype = Transition(label='Build prototype')
test_functionality = Transition(label='Test functionality')
test_safety = Transition(label='Test safety')
test_market_potential = Transition(label='Test market potential')
collect_feedback = Transition(label='Collect feedback from testing phase')
refine_prototype = Transition(label='Refine prototype')
approve_prototype = Transition(label='Approve prototype for further development')
discard_prototype = Transition(label='Discard prototype')

# Define loops and XORs
testing_loop = OperatorPOWL(operator=Operator.LOOP, children=[test_functionality, test_safety, test_market_potential, collect_feedback, refine_prototype])
approval_xor = OperatorPOWL(operator=Operator.XOR, children=[approve_prototype, discard_prototype])

# Define the root POWL model
root = StrictPartialOrder(nodes=[identify_idea, conduct_research, conduct_studies, draft_concepts, select_design, build_prototype, testing_loop, approval_xor])

# Define the order of the nodes
root.order.add_edge(identify_idea, conduct_research)
root.order.add_edge(conduct_research, conduct_studies)
root.order.add_edge(conduct_studies, draft_concepts)
root.order.add_edge(draft_concepts, select_design)
root.order.add_edge(select_design, build_prototype)
root.order.add_edge(build_prototype, testing_loop)
root.order.add_edge(testing_loop, approval_xor)