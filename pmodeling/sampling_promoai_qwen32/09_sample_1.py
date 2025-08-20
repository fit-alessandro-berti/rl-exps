import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Identify_idea = Transition(label='Identify idea for new product or improvement')
Conduct_research = Transition(label='Conduct initial research')
Feasibility_studies = Transition(label='Conduct feasibility studies')
Draft_design = Transition(label='Draft design concepts')
Select_design = Transition(label='Select promising design')
Build_prototype = Transition(label='Build prototype')
Test_functionality = Transition(label='Test functionality')
Test_safety = Transition(label='Test safety')
Test_market = Transition(label='Test market potential')
Collect_feedback = Transition(label='Collect feedback from testing phase')
Refine_prototype = Transition(label='Refine prototype')
Approve_prototype = Transition(label='Approve prototype for further development')
Discard_prototype = Transition(label='Discard prototype')

# Define the process
loop = OperatorPOWL(operator=Operator.LOOP, children=[Refine_prototype, Collect_feedback, Test_functionality, Test_safety, Test_market])
xor = OperatorPOWL(operator=Operator.XOR, children=[Approve_prototype, Discard_prototype])
root = StrictPartialOrder(nodes=[Identify_idea, Conduct_research, Feasibility_studies, Draft_design, Select_design, Build_prototype, Test_functionality, Test_safety, Test_market, Collect_feedback, Refine_prototype, Approve_prototype, Discard_prototype])
root.order.add_edge(Identify_idea, Conduct_research)
root.order.add_edge(Conduct_research, Feasibility_studies)
root.order.add_edge(Feasibility_studies, Draft_design)
root.order.add_edge(Draft_design, Select_design)
root.order.add_edge(Select_design, Build_prototype)
root.order.add_edge(Build_prototype, Test_functionality)
root.order.add_edge(Test_functionality, Test_safety)
root.order.add_edge(Test_safety, Test_market)
root.order.add_edge(Test_market, Collect_feedback)
root.order.add_edge(Collect_feedback, loop)
root.order.add_edge(loop, xor)