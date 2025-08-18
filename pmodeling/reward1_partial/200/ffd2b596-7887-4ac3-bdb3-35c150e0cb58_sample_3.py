root = StrictPartialOrder(
    nodes=[
        Transition(label='Component Sourcing'),
        Transition(label='Sensor Calibrate'),
        Transition(label='Motor Assembly'),
        Transition(label='Frame Build'),
        Transition(label='Software Install'),
        Transition(label='Algorithm Tune'),
        Transition(label='Battery Integrate'),
        Transition(label='Signal Test'),
        Transition(label='Durability Check'),
        Transition(label='Flight Simulate'),
        Transition(label='Quality Inspect'),
        Transition(label='Compliance Review'),
        Transition(label='Packaging Prep'),
        Transition(label='Logistics Plan'),
        Transition(label='Client Feedback')
    ],
    order={
        Transition(label='Component Sourcing'): Transition(label='Sensor Calibrate'),
        Transition(label='Sensor Calibrate'): Transition(label='Motor Assembly'),
        Transition(label='Motor Assembly'): Transition(label='Frame Build'),
        Transition(label='Frame Build'): Transition(label='Software Install'),
        Transition(label='Software Install'): Transition(label='Algorithm Tune'),
        Transition(label='Algorithm Tune'): Transition(label='Battery Integrate'),
        Transition(label='Battery Integrate'): Transition(label='Signal Test'),
        Transition(label='Signal Test'): Transition(label='Durability Check'),
        Transition(label='Durability Check'): Transition(label='Flight Simulate'),
        Transition(label='Flight Simulate'): Transition(label='Quality Inspect'),
        Transition(label='Quality Inspect'): Transition(label='Compliance Review'),
        Transition(label='Compliance Review'): Transition(label='Packaging Prep'),
        Transition(label='Packaging Prep'): Transition(label='Logistics Plan'),
        Transition(label='Logistics Plan'): Transition(label='Client Feedback')
    }
)