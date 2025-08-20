import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the POWL model
root = StrictPartialOrder(nodes=[identify_need, issue_rfp, receive_proposals, evaluate_proposal, conduct_site_visit, conduct_interview, select_supplier, begin_negotiations, sign_contract, execute_contract, onboard_supplier])
root.order.add_edge(identify_need, issue_rfp)
root.order.add_edge(issue_rfp, receive_proposals)
root.order.add_edge(receive_proposals, evaluate_proposal)
root.order.add_edge(evaluate_proposal, conduct_site_visit)
root.order.add_edge(evaluate_proposal, conduct_interview)
root.order.add_edge(conduct_site_visit, select_supplier)
root.order.add_edge(conduct_interview, select_supplier)
root.order.add_edge(select_supplier, begin_negotiations)
root.order.add_edge(begin_negotiations, sign_contract)
root.order.add_edge(sign_contract, execute_contract)
root.order.add_edge(execute_contract, onboard_supplier)