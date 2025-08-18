from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

artifact_intake = Transition(label='Artifact Intake')
condition_check = Transition(label='Condition Check')
material_sampling = Transition(label='Material Sampling')
radiocarbon_test = Transition(label='Radiocarbon Test')
provenance_review = Transition(label='Provenance Review')
imaging_capture = Transition(label='Imaging Capture')
chemical_analysis = Transition(label='Chemical Analysis')
historical_match = Transition(label='Historical Match')
expert_consult = Transition(label='Expert Consult')
forgery_scan = Transition(label='Forgery Scan')
market_survey = Transition(label='Market Survey')
value_estimate = Transition(label='Value Estimate')
certification = Transition(label='Certification')
digital_archive = Transition(label='Digital Archive')
final_storage = Transition(label='Final Storage')

skip = SilentTransition()

# Radiocarbon Test and Chemical Analysis are sequential, so we use a loop
loop_radiocarbon = OperatorPOWL(operator=Operator.LOOP, children=[radiocarbon_test, chemical_analysis])
loop_radiocarbon.order.add_edge(radiocarbon_test, chemical_analysis)

# Imaging Capture and Chemical Analysis are concurrent, so we use an XOR
xor_imaging = OperatorPOWL(operator=Operator.XOR, children=[imaging_capture, chemical_analysis])

# Market Survey and Historical Match are concurrent, so we use an XOR
xor_market = OperatorPOWL(operator=Operator.XOR, children=[market_survey, historical_match])

# Forgery Scan and Expert Consult are concurrent, so we use an XOR
xor_forgery = OperatorPOWL(operator=Operator.XOR, children=[forgery_scan, expert_consult])

# Value Estimate and Certification are concurrent, so we use an XOR
xor_value = OperatorPOWL(operator=Operator.XOR, children=[value_estimate, certification])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Provenance Review and Historical Match are concurrent, so we use an XOR
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_review, historical_match])

# Expert Consult and Forgery Scan are concurrent, so we use an XOR
xor_expert = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, forgery_scan])

# Market Survey and Historical Match are concurrent, so we use an XOR
xor_market = OperatorPOWL(operator=Operator.XOR, children=[market_survey, historical_match])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor_provenance])

# Final Storage is concurrent with the rest, so we use an XOR
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_storage, xor_value])

# Artifact Intake is concurrent with the rest, so we use an XOR
xor_artifact = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, xor