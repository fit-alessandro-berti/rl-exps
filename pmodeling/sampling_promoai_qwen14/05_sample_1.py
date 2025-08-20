import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Identify_need_for_new_supplier_or_vendor = Transition(label='Identify need for new supplier or vendor')
Issue_request_for_proposals_RFP = Transition(label='Issue request for proposals (RFP)')
Receive_supplier_proposals = Transition(label='Receive supplier proposals')
Evaluate_proposal = Transition(label='Evaluate proposal')
Conduct_interview = Transition(label='Conduct interview')
Conduct_site_visit = Transition(label='Conduct site visit')
Select_supplier = Transition(label='Select supplier')
Begin_contract_negotiations = Transition(label='Begin contract negotiations')
Sign_contract = Transition(label='Sign contract')
Execute_contract = Transition(label='Execute contract')
Onboard_supplier = Transition(label='Onboard supplier')

# Define the choice node for conducting interview or site visit
interview_or_site_visit = OperatorPOWL(operator=Operator.XOR, children=[Conduct_interview, Conduct_site_visit])

# Define the loop node for evaluating proposals and conducting interviews or site visits
evaluate_loop = OperatorPOWL(operator=Operator.LOOP, children=[Evaluate_proposal, interview_or_site_visit])

# Define the order of activities
root = StrictPartialOrder(nodes=[Identify_need_for_new_supplier_or_vendor, Issue_request_for_proposals_RFP, Receive_supplier_proposals, evaluate_loop, Select_supplier, Begin_contract_negotiations, Sign_contract, Execute_contract, Onboard_supplier])

# Define the dependencies between activities
root.order.add_edge(Identify_need_for_new_supplier_or_vendor, Issue_request_for_proposals_RFP)
root.order.add_edge(Issue_request_for_proposals_RFP, Receive_supplier_proposals)
root.order.add_edge(Receive_supplier_proposals, evaluate_loop)
root.order.add_edge(evaluate_loop, Select_supplier)
root.order.add_edge(Select_supplier, Begin_contract_negotiations)
root.order.add_edge(Begin_contract_negotiations, Sign_contract)
root.order.add_edge(Sign_contract, Execute_contract)
root.order.add_edge(Execute_contract, Onboard_supplier)