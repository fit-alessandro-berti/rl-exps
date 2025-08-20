import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
identify_idea = Transition(label='Identify idea for new product or improvement')
conduct_initial_research = Transition(label='Conduct initial research')
conduct_feasibility_studies = Transition(label='Conduct feasibility studies')
draft_design_concepts = Transition(label='Draft design concepts')
select_promising_design = Transition(label='Select promising design')
build_prototype = Transition(label='Build prototype')
test_functionality = Transition(label='Test functionality')
test_safety = Transition(label='Test safety')
test_market_potential = Transition(label='Test market potential')
collect_feedback = Transition(label='Collect feedback from testing phase')
refine_prototype = Transition(label='Refine prototype')
approve_prototype = Transition(label='Approve prototype for further development')
discard_prototype = Transition(label='Discard prototype')

# Define control-flow operators
loop = OperatorPOWL(operator=Operator.LOOP, children=[build_prototype, test_functionality, test_safety, test_market_potential, collect_feedback, refine_prototype])
choice = OperatorPOWL(operator=Operator.XOR, children=[approve_prototype, discard_prototype])

# Define partial order
root = StrictPartialOrder(nodes=[identify_idea, conduct_initial_research, conduct_feasibility_studies, draft_design_concepts, select_promising_design, loop, choice])
root.order.add_edge(identify_idea, conduct_initial_research)
root.order.add_edge(conduct_initial_research, conduct_feasibility_studies)
root.order.add_edge(conduct_feasibility_studies, draft_design_concepts)
root.order.add_edge(draft_design_concepts, select_promising_design)
root.order.add_edge(select_promising_design, loop)
root.order.add_edge(loop, choice)
root.order.add_edge(choice, approve_prototype)
root.order.add_edge(choice, discard_prototype)