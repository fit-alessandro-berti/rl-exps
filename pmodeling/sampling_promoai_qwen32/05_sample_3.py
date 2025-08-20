import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
identify_need = Transition(label='Identify need for new supplier or vendor')
issue_rfp = Transition(label='Issue request for proposals (RFP)')
receive_proposals = Transition(label='Receive supplier proposals')
evaluate_proposal = Transition(label='Evaluate proposal')
conduct_site_visit = Transition(label='Conduct site visit')
conduct_interview = Transition(label='Conduct interview')
select_supplier = Transition(label='Select supplier')
begin_negotiations = Transition(label='Begin contract negotiations')
sign_contract = Transition(label='Sign contract')
execute_contract = Transition(label='Execute contract')
onboard_supplier = Transition(label='Onboard supplier')

# Create a loop for evaluation and selection
loop_evaluation = OperatorPOWL(operator=Operator.LOOP, children=[evaluate_proposal, conduct_site_visit, conduct_interview, select_supplier])

# Create a choice between signing the contract or going back to the loop
choice_sign_contract = OperatorPOWL(operator=Operator.XOR, children=[sign_contract, loop_evaluation])

# Define the overall structure of the process
root = StrictPartialOrder(nodes=[identify_need, issue_rfp, receive_proposals, loop_evaluation, choice_sign_contract, begin_negotiations, execute_contract, onboard_supplier])

# Add edges to represent dependencies
root.order.add_edge(identify_need, issue_rfp)
root.order.add_edge(issue_rfp, receive_proposals)
root.order.add_edge(receive_proposals, loop_evaluation)
root.order.add_edge(loop_evaluation, choice_sign_contract)
root.order.add_edge(choice_sign_contract, begin_negotiations)
root.order.add_edge(begin_negotiations, sign_contract)
root.order.add_edge(sign_contract, execute_contract)
root.order.add_edge(execute_contract, onboard_supplier)