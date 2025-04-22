project_steps_texts = [
    {
        "title": "Overview",
        "content": """**No Wires, No Problem: Magnetic Induction for Wireless Power**

**Project Objectives:**
- Understand the principles of electromagnetic induction and mutual inductance.
- Analyze how two coils transfer energy without direct contact.
- Evaluate system parameters like coil distance, alignment, and efficiency.
- Explore real-world uses in toothbrushes, smartphones, and EV chargers.
"""
    },
    {
        "title": "Part 1: Inductive Coupling – The Basic Idea (20%)",
        "content": """**Task 1:**
- Define electromagnetic induction and describe how a time-varying current in a coil produces a magnetic field.
- Explain how this changing field can induce voltage in a nearby coil.

**Diagram Task:**
- Draw a transmitter coil (connected to AC source) and a receiver coil. Label the directions of current and induced magnetic field.

**Guiding Questions:**
- Why is alternating current required for wireless power?
- What factors affect how much voltage is induced in the receiver coil?
"""
    },
    {
        "title": "Part 2: Mutual Inductance and Coil Design (25%)",
        "content": """**Task 2:**
- Use the formula for induced EMF:
  \[
  \\mathcal{E} = -M \\frac{dI}{dt}
  \]
  where \( M \) is the mutual inductance between coils.

- Assume:
  - Primary coil current varies as \( I(t) = I_0 \\sin(\\omega t) \)
  - \( M = 1.2 \\times 10^{-6}~\\text{H} \), \( I_0 = 2~\\text{A} \), \( \\omega = 1000~\\text{rad/s} \)

- Calculate peak induced EMF in the secondary coil.

**Guiding Questions:**
- How does coil alignment and distance affect mutual inductance?
- Why must coils be carefully positioned in practical systems?
"""
    },
    {
        "title": "Part 3: System Efficiency and Energy Loss (25%)",
        "content": """**Task 3:**
- Define efficiency as:
  \[
  \\text{Efficiency} = \\frac{P_{\\text{received}}}{P_{\\text{input}}} \\times 100\\%
  \]

- Consider a case where input power is 5 W and only 3.2 W is received by the device.
- Calculate system efficiency and identify sources of loss (e.g., heat, misalignment, eddy currents).

**Guiding Questions:**
- Why is wireless power transfer typically less efficient than wired?
- How do high-frequency AC signals affect performance?
"""
    },
    {
        "title": "Part 4: Real-World Use Cases and Challenges (20%)",
        "content": """**Task 4:**
- Choose a wireless charging example (e.g., electric toothbrush, phone pad, induction stove).
- Explain how magnetic induction is used in the design.
- Identify safety and efficiency features used in that system.

**Optional Extension:**
- Propose a new device or application that could benefit from wireless power.

**Guiding Questions:**
- What limits the range and power levels of current systems?
- How do commercial devices balance efficiency, size, and safety?
"""
    },
    {
        "title": "Part 5: Synthesis & Reflection (10%)",
        "content": """**Task 5:**
- Summarize how wireless power transfer systems apply Faraday’s Law in practice.
- Reflect: How do you think this technology will evolve in the next 10–20 years?

**Bonus Consideration:**
- Could this concept be scaled up to power moving vehicles or homes?
"""
    }
]