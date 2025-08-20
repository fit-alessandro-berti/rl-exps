import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
begin_negotiations = Transition(label='Begin contract negotiations')
conduct_interview = Transition(label='Conduct interview')
conduct_site_visit = Transition(label='Conduct site visit')
evaluate_proposal = Transition(label='Evaluate proposal')
execute_contract = Transition(label='Execute contract')
identify_need = Transition(label='Identify need for new supplier or vendor')
issue_rfp = Transition(label='Issue request for proposals (RFP)')
onboard_supplier = Transition(label='Onboard supplier')
receive_proposals = Transition(label='Receive supplier proposals')
select_supplier = Transition(label='Select supplier')
sign_contract = Transition(label='Sign contract')

# Define silent transitions
skip_interview = SilentTransition()
skip_site_visit = SilentTransition()
skip_proposal_evaluation = SilentTransition()

# Define loops and choices
site_visit_loop = OperatorPOWL(operator=Operator.LOOP, children=[conduct_interview, skip_interview])
proposal_evaluation_loop = OperatorPOWL(operator=Operator.LOOP, children=[conduct_site_visit, skip_site_visit])
proposal_evaluation_choice = OperatorPOWL(operator=Operator.XOR, children=[evaluate_proposal, skip_proposal_evaluation])
contract_negotiation_choice = OperatorPOWL(operator=Operator.XOR, children=[site_visit_loop, proposal_evaluation_loop])
contract_negotiation_choice_loop = OperatorPOWL(operator=Operator.LOOP, children=[contract_negotiation_choice, proposal_evaluation_choice])

# Define root node
root = StrictPartialOrder(nodes=[identify_need, issue_rfp, receive_proposals, select_supplier, contract_negotiation_choice_loop, execute_contract, onboard_supplier])
root.order.add_edge(identify_need, issue_rfp)
root.order.add_edge(issue_rfp, receive_proposals)
root.order.add_edge(receive_proposals, select_supplier)
root.order.add_edge(select_supplier, contract_negotiation_choice_loop)
root.order.add_edge(contract_negotiation_choice_loop, execute_contract)
root.order.add_edge(execute_contract, onboard_supplier)

print(root)