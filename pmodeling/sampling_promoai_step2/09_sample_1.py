import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as POWL transitions
identify_idea = Transition(label='Identify idea for new product or improvement')
conduct_research = Transition(label='Conduct initial research')
conduct_feasibility_studies = Transition(label='Conduct feasibility studies')
draft_design_concepts = Transition(label='Draft design concepts')
select_promising_design = Transition(label='Select promising design')
build_prototype = Transition(label='Build prototype')
test_functionality = Transition(label='Test functionality')
test_safety = Transition(label='Test safety')
test_market_potential = Transition(label='Test market potential')
collect_feedback = Transition(label='Collect feedback from testing phase')
refine_prototype = Transition(label='Refine prototype')
approve_for_development = Transition(label='Approve prototype for further development')
discard_prototype = Transition(label='Discard prototype')

# Define the partial order
root = StrictPartialOrder(nodes=[
    identify_idea,
    conduct_research,
    conduct_feasibility_studies,
    draft_design_concepts,
    select_promising_design,
    build_prototype,
    test_functionality,
    test_safety,
    test_market_potential,
    collect_feedback,
    refine_prototype,
    approve_for_development,
    discard_prototype
])

# Define the dependencies between the activities
root.order.add_edge(identify_idea, conduct_research)
root.order.add_edge(conduct_research, conduct_feasibility_studies)
root.order.add_edge(conduct_feasibility_studies, draft_design_concepts)
root.order.add_edge(draft_design_concepts, select_promising_design)
root.order.add_edge(select_promising_design, build_prototype)
root.order.add_edge(build_prototype, test_functionality)
root.order.add_edge(test_functionality, test_safety)
root.order.add_edge(test_safety, test_market_potential)
root.order.add_edge(test_market_potential, collect_feedback)
root.order.add_edge(collect_feedback, refine_prototype)
root.order.add_edge(refine_prototype, test_functionality)
root.order.add_edge(test_functionality, test_safety)
root.order.add_edge(test_safety, test_market_potential)
root.order.add_edge(test_market_potential, collect_feedback)
root.order.add_edge(collect_feedback, approve_for_development)
root.order.add_edge(collect_feedback, discard_prototype)

# Print the root of the POWL model
print(root)