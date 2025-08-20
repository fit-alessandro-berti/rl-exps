import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
identify_idea = Transition(label='Identify idea for new product or improvement')
conduct_research = Transition(label='Conduct initial research')
conduct_feasibility = Transition(label='Conduct feasibility studies')
draft_concepts = Transition(label='Draft design concepts')
select_design = Transition(label='Select promising design')
build_prototype = Transition(label='Build prototype')
test_functionality = Transition(label='Test functionality')
test_safety = Transition(label='Test safety')
test_market_potential = Transition(label='Test market potential')
collect_feedback = Transition(label='Collect feedback from testing phase')
refine_prototype = Transition(label='Refine prototype')
approve_development = Transition(label='Approve prototype for further development')
discard_prototype = Transition(label='Discard prototype')

# Define silent transitions
skip = SilentTransition()

# Define nodes
research_node = OperatorPOWL(operator=Operator.XOR, children=[conduct_research, skip])
feasibility_node = OperatorPOWL(operator=Operator.XOR, children=[conduct_feasibility, skip])
concepts_node = OperatorPOWL(operator=Operator.XOR, children=[draft_concepts, skip])
design_node = OperatorPOWL(operator=Operator.XOR, children=[select_design, skip])
prototype_node = OperatorPOWL(operator=Operator.XOR, children=[build_prototype, skip])
testing_node = OperatorPOWL(operator=Operator.XOR, children=[test_functionality, test_safety, test_market_potential])
feedback_node = OperatorPOWL(operator=Operator.XOR, children=[collect_feedback, skip])
refine_node = OperatorPOWL(operator=Operator.XOR, children=[refine_prototype, skip])
approval_node = OperatorPOWL(operator=Operator.XOR, children=[approve_development, skip])
discarding_node = OperatorPOWL(operator=Operator.XOR, children=[discard_prototype, skip])

# Define root node
root = StrictPartialOrder(nodes=[identify_idea, research_node, feasibility_node, concepts_node, design_node, prototype_node, testing_node, feedback_node, refine_node, approval_node, discarding_node])

# Define dependencies
root.order.add_edge(identify_idea, research_node)
root.order.add_edge(identify_idea, feasibility_node)
root.order.add_edge(research_node, concepts_node)
root.order.add_edge(research_node, feasibility_node)
root.order.add_edge(feasibility_node, concepts_node)
root.order.add_edge(feasibility_node, design_node)
root.order.add_edge(concepts_node, design_node)
root.order.add_edge(design_node, prototype_node)
root.order.add_edge(prototype_node, testing_node)
root.order.add_edge(testing_node, feedback_node)
root.order.add_edge(testing_node, refine_node)
root.order.add_edge(feedback_node, refine_node)
root.order.add_edge(refine_node, testing_node)
root.order.add_edge(refine_node, approval_node)
root.order.add_edge(refine_node, discarding_node)
root.order.add_edge(approval_node, discarding_node)

# Print the root
print(root)