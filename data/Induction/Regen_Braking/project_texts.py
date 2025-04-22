project_steps_texts = [
    {
        "title": "Overview",
        "content": """**Turning Motion into Electricity: The Physics of Regenerative Braking**

**Project Objectives:**
- Understand how changing magnetic flux induces currents in regenerative braking systems.
- Analyze energy conversion from mechanical to electrical form using Faraday’s and Lenz’s Laws.
- Apply basic equations to estimate power recovery in electric vehicles.
- Explore the role of magnetic fields in slowing motion and increasing efficiency.
"""
    },
    {
        "title": "Part 1: Basic Concept of Regenerative Braking (20%)",
        "content": """**Task 1:**
- Define regenerative braking and compare it to traditional friction-based braking.
- Describe how it uses electromagnetic induction to slow down a vehicle and recover energy.

**Guiding Questions:**
- How does the vehicle’s motor act as a generator during braking?
- What forces oppose motion in this process, and why?
"""
    },
    {
        "title": "Part 2: Induced EMF from Rotational Motion (25%)",
        "content": """**Task 2:**
- Assume a circular copper coil of radius \( r = 0.15~\\text{m} \), with \( N = 300 \) turns, is rotating at \( \omega = 100~\\text{rad/s} \) in a magnetic field of \( B = 0.5~\\text{T} \).

**Calculations:**
- Determine the area \( A = \\pi r^2 \).
- Find the peak induced EMF:
  \[
  \\mathcal{E}_{\\text{max}} = NBA\\omega
  \]

**Guiding Questions:**
- What factors increase the induced voltage during braking?
- How is energy from this voltage stored or reused in EVs?
"""
    },
    {
        "title": "Part 3: Power Recovery and Energy Estimation (25%)",
        "content": """**Task 3:**
- Assume a car decelerates from 20 m/s to 5 m/s over 8 seconds. Its mass is 1000 kg.

**Tasks:**
- Calculate the mechanical energy lost:
  \[
  \\Delta E = \\frac{1}{2}mv_i^2 - \\frac{1}{2}mv_f^2
  \]
- If regenerative braking captures 70% of this energy, how much is stored?

**Guiding Questions:**
- How much braking energy is “wasted” in a friction-based system?
- How do efficiency and design affect real-world recovery?
"""
    },
    {
        "title": "Part 4: Lenz’s Law and Magnetic Resistance (20%)",
        "content": """**Task 4:**
- Use Lenz’s Law to explain why the magnetic force during braking opposes the vehicle’s motion.
- Sketch the direction of current and induced magnetic field during braking.

**Extension Task:**
- Research one real electric vehicle (e.g., Tesla, Nissan Leaf) and describe how it implements regenerative braking.

**Guiding Questions:**
- Why does the magnetic force grow stronger as the rotation slows down?
- Why do EVs blend regenerative with friction braking?
"""
    },
    {
        "title": "Part 5: Synthesis & Reflection (10%)",
        "content": """**Task 5:**
- Summarize how energy is conserved and transformed during regenerative braking.
- Reflect: How can physics help design cleaner, more efficient transportation?

**Bonus Consideration:**
- Could regenerative braking be applied to bicycles or elevators? What design challenges would arise?
"""
    }
]