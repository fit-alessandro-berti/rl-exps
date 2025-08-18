root = StrictPartialOrder(
    nodes=[
        Transition(label='Asset Intake'),
        Transition(label='Provenance Check'),
        Transition(label='Material Sampling'),
        Transition(label='Radiocarbon Test'),
        Transition(label='Style Compare'),
        Transition(label='Historical Search'),
        Transition(label='Expert Consult'),
        Transition(label='Condition Review'),
        Transition(label='Scientific Analysis'),
        Transition(label='Data Compilation'),
        Transition(label='Peer Review'),
        Transition(label='Report Draft'),
        Transition(label='Certification'),
        Transition(label='Digital Archive'),
        Transition(label='Client Delivery')
    ],
    order={
        Transition(label='Asset Intake'): Transition(label='Provenance Check'),
        Transition(label='Provenance Check'): Transition(label='Material Sampling'),
        Transition(label='Material Sampling'): Transition(label='Radiocarbon Test'),
        Transition(label='Radiocarbon Test'): Transition(label='Style Compare'),
        Transition(label='Style Compare'): Transition(label='Historical Search'),
        Transition(label='Historical Search'): Transition(label='Expert Consult'),
        Transition(label='Expert Consult'): Transition(label='Condition Review'),
        Transition(label='Condition Review'): Transition(label='Scientific Analysis'),
        Transition(label='Scientific Analysis'): Transition(label='Data Compilation'),
        Transition(label='Data Compilation'): Transition(label='Peer Review'),
        Transition(label='Peer Review'): Transition(label='Report Draft'),
        Transition(label='Report Draft'): Transition(label='Certification'),
        Transition(label='Certification'): Transition(label='Digital Archive'),
        Transition(label='Digital Archive'): Transition(label='Client Delivery')
    }
)