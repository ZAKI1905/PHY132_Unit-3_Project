project_steps_texts = [
    {
        "title": "Overview",
        "content": """**Magnetic Torque on Satellites: How Spacecraft Change Orientation Without Fuel**

**Project Objectives:**
- Understand how magnetic torque is generated and used for spacecraft attitude control.
- Analyze the interaction between current-carrying coils and Earth’s magnetic field.
- Develop reasoning and diagramming skills to explain magnetic moment and torque.
- Perform numerical calculations to evaluate torque magnitudes and direction.
- Explore real-world engineering strategies for satellite orientation.
"""
    },
    {
        "title": "Part 1: Conceptual Overview of Satellite Attitude Control (20%)",
        "content": """**Task 1:**
- Define *attitude control* and explain why it’s essential for satellites (e.g., for pointing instruments, antennas, or solar panels).
- Describe two main methods of satellite orientation: reaction wheels and magnetorquers.

**Guiding Questions:**
- What is a magnetorquer? What are its advantages over other systems?
- Why is using Earth’s magnetic field for torque generation fuel-free?
"""
    },
    {
        "title": "Part 2: Magnetic Moment of a Current Loop (20%)",
        "content": """**Task 2:**
- Draw and label a rectangular current-carrying loop placed in a magnetic field.
- Define the magnetic moment:
  \[
  \\vec{\\mu} = NIA\\hat{n}
  \]
  where:
  - \( N \): number of turns in the coil
  - \( I \): current in the wire
  - \( A \): area of the loop
  - \( \\hat{n} \): unit vector perpendicular to the loop surface (right-hand rule)

- Explain how changing the current direction changes the direction of the magnetic moment.

**Guiding Questions:**
- What physical features of the loop affect the size of the magnetic moment?
- How is the direction of the magnetic moment determined?
"""
    },
    {
        "title": "Part 3: Torque on a Current Loop in Earth’s Magnetic Field (30%)",
        "content": """**Task 3:**
- Explain how torque is produced by a current loop in an external magnetic field using:
  \[
  \\vec{\\tau} = \\vec{\\mu} \\times \\vec{B}
  \]

- Given a coil of area \( A = 0.1~\\text{m}^2 \), current \( I = 2~\\text{A} \), and \( N = 200 \) turns, and Earth's magnetic field \( B = 3 \\times 10^{-5}~\\text{T} \), calculate:
  - Magnetic moment magnitude \( \\mu \)
  - Torque magnitude when the loop is at 90° to \( \\vec{B} \): \( \\tau = \\mu B \\)

- Draw vectors \( \\vec{\\mu} \), \( \\vec{B} \), and \( \\vec{\\tau} \) in a clear diagram to explain their directions.

**Guiding Questions:**
- Why is the torque zero when the magnetic moment is aligned with the field?
- What orientation causes the greatest torque?
"""
    },
    {
        "title": "Part 4: Time-Dependent Satellite Orientation Strategy (20%)",
        "content": """**Task 4:**
- Describe how turning the current in the magnetorquer coil on and off at different times allows precise control of satellite orientation.
- Imagine you want to rotate the satellite 45° clockwise. What current direction and coil orientation would help accomplish this?

**Extension (optional):**
- Research and report how real missions (e.g., CubeSats) implement magnetorquers.

**Guiding Questions:**
- Why must the onboard computer know Earth’s magnetic field direction at a given location?
- What challenges arise from Earth’s field not being uniform?
"""
    },
    {
        "title": "Part 5: Synthesis & Reflection (10%)",
        "content": """**Task 5:**
- Summarize your understanding of how satellites use current loops to generate torque.
- Reflect: What are the advantages and limitations of magnetorquers compared to other methods like gas thrusters or reaction wheels?

**Bonus Consideration:**
- If Earth’s magnetic field were stronger or weaker, how would that affect the torque?
"""
    }
]