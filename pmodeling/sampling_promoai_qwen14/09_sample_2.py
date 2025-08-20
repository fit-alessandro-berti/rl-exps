import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Identify_idea_for_new_product_or_improvement = Transition(label='Identify idea for new product or improvement')
Conduct_initial_research = Transition(label='Conduct initial research')
Conduct_feasibility_studies = Transition(label='Conduct feasibility studies')
Draft_design_concepts = Transition(label='Draft design concepts')
Select_promising_design = Transition(label='Select promising design')
Build_prototype = Transition(label='Build prototype')
Test_functionality = Transition(label='Test functionality')
Test_safety = Transition(label='Test safety')
Test_market_potential = Transition(label='Test market potential')
Collect_feedback_from_testing_phase = Transition(label='Collect feedback from testing phase')
Refine_prototype = Transition(label='Refine prototype')
Approve_prototype_for_further_development = Transition(label='Approve prototype for further development')
Discard_prototype = Transition(label='Discard prototype')

Test_phase = OperatorPOWL(operator=Operator.XOR, children=[Test_functionality, Test_safety, Test_market_potential])
Testing_phase = StrictPartialOrder(nodes=[Build_prototype, Test_phase, Collect_feedback_from_testing_phase, Refine_prototype])

Refinement_loop = OperatorPOWL(operator=Operator.LOOP, children=[Testing_phase])
Prototype_evaluation = OperatorPOWL(operator=Operator.XOR, children=[Approve_prototype_for_further_development, Discard_prototype])

root = StrictPartialOrder(nodes=[Identify_idea_for_new_product_or_improvement, Conduct_initial_research, Conduct_feasibility_studies, Draft_design_concepts, Select_promising_design, Refinement_loop, Prototype_evaluation])
root.order.add_edge(Identify_idea_for_new_product_or_improvement, Conduct_initial_research)
root.order.add_edge(Conduct_initial_research, Conduct_feasibility_studies)
root.order.add_edge(Conduct_feasibility_studies, Draft_design_concepts)
root.order.add_edge(Draft_design_concepts, Select_promising_design)
root.order.add_edge(Select_promising_design, Refinement_loop)
root.order.add_edge(Refinement_loop, Prototype_evaluation)