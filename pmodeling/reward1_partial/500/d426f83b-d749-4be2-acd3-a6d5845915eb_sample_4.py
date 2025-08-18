import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
intake = Transition(label='Asset Intake')
check = Transition(label='Provenance Check')
sampling = Transition(label='Material Sampling')
radiocarbon = Transition(label='Radiocarbon Test')
style_compare = Transition(label='Style Compare')
historical_search = Transition(label='Historical Search')
consult = Transition(label='Expert Consult')
review = Transition(label='Condition Review')
analysis = Transition(label='Scientific Analysis')
compilation = Transition(label='Data Compilation')
peer_review = Transition(label='Peer Review')
report_draft = Transition(label='Report Draft')
certification = Transition(label='Certification')
archive = Transition(label='Digital Archive')
delivery = Transition(label='Client Delivery')

# Define the process
intake_to_check = OperatorPOWL(operator=Operator.SEQUENCE, children=[intake, check])
check_to_sampling = OperatorPOWL(operator=Operator.SEQUENCE, children=[check, sampling])
sampling_to_radiocarbon = OperatorPOWL(operator=Operator.SEQUENCE, children=[sampling, radiocarbon])
radiocarbon_to_style_compare = OperatorPOWL(operator=Operator.SEQUENCE, children=[radiocarbon, style_compare])
style_compare_to_historical_search = OperatorPOWL(operator=Operator.SEQUENCE, children=[style_compare, historical_search])
historical_search_to_consult = OperatorPOWL(operator=Operator.SEQUENCE, children=[historical_search, consult])
consult_to_review = OperatorPOWL(operator=Operator.SEQUENCE, children=[consult, review])
review_to_analysis = OperatorPOWL(operator=Operator.SEQUENCE, children=[review, analysis])
analysis_to_compilation = OperatorPOWL(operator=Operator.SEQUENCE, children=[analysis, compilation])
compilation_to_peer_review = OperatorPOWL(operator=Operator.SEQUENCE, children=[compilation, peer_review])
peer_review_to_report_draft = OperatorPOWL(operator=Operator.SEQUENCE, children=[peer_review, report_draft])
report_draft_to_certification = OperatorPOWL(operator=Operator.SEQUENCE, children=[report_draft, certification])
certification_to_archive = OperatorPOWL(operator=Operator.SEQUENCE, children=[certification, archive])
archive_to_delivery = OperatorPOWL(operator=Operator.SEQUENCE, children=[archive, delivery])

# Create the root node
root = StrictPartialOrder(nodes=[intake_to_check, check_to_sampling, sampling_to_radiocarbon, radiocarbon_to_style_compare, style_compare_to_historical_search, historical_search_to_consult, consult_to_review, review_to_analysis, analysis_to_compilation, compilation_to_peer_review, peer_review_to_report_draft, report_draft_to_certification, certification_to_archive, archive_to_delivery])

# Define the order of nodes
root.order.add_edge(intake_to_check, check_to_sampling)
root.order.add_edge(check_to_sampling, sampling_to_radiocarbon)
root.order.add_edge(sampling_to_radiocarbon, radiocarbon_to_style_compare)
root.order.add_edge(radiocarbon_to_style_compare, style_compare_to_historical_search)
root.order.add_edge(style_compare_to_historical_search, historical_search_to_consult)
root.order.add_edge(historical_search_to_consult, consult_to_review)
root.order.add_edge(consult_to_review, review_to_analysis)
root.order.add_edge(review_to_analysis, analysis_to_compilation)
root.order.add_edge(analysis_to_compilation, compilation_to_peer_review)
root.order.add_edge(compilation_to_peer_review, peer_review_to_report_draft)
root.order.add_edge(peer_review_to_report_draft, report_draft_to_certification)
root.order.add_edge(report_draft_to_certification, certification_to_archive)
root.order.add_edge(certification_to_archive, archive_to_delivery)

# Print the root node
print(root)