import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
identify_idea = Transition(label='Identify idea for new product or improvement')
research = Transition(label='Conduct initial research')
feasibility = Transition(label='Conduct feasibility studies')
draft_designs = Transition(label='Draft design concepts')
select_design = Transition(label='Select promising design')
build_prototype = Transition(label='Build prototype')
test_functionality = Transition(label='Test functionality')
test_safety = Transition(label='Test safety')
test_market = Transition(label='Test market potential')
collect_feedback = Transition(label='Collect feedback from testing phase')
refine_prototype = Transition(label='Refine prototype')
approve_development = Transition(label='Approve prototype for further development')
discard_prototype = Transition(label='Discard prototype')

# Define exclusive choice for testing phase
test_phase = OperatorPOWL(operator=Operator.XOR, children=[test_functionality, test_safety, test_market])

# Define loop for refinement and retesting
refine_loop = OperatorPOWL(operator=Operator.LOOP, children=[refine_prototype, test_phase])

# Define the main process structure
main_process = StrictPartialOrder(nodes=[identify_idea, research, feasibility, draft_designs, select_design, build_prototype, test_phase, refine_loop, OperatorPOWL(operator=Operator.XOR, children=[approve_development, discard_prototype])])

# Define the order of activities
main_process.order.add_edge(identify_idea, research)
main_process.order.add_edge(research, feasibility)
main_process.order.add_edge(feasibility, draft_designs)
main_process.order.add_edge(draft_designs, select_design)
main_process.order.add_edge(select_design, build_prototype)
main_process.order.add_edge(build_prototype, test_phase)
main_process.order.add_edge(test_phase, refine_loop)
main_process.order.add_edge(refine_loop, OperatorPOWL(operator=Operator.XOR, children=[approve_development, discard_prototype]))

# Final result is stored in 'root'
root = main_process