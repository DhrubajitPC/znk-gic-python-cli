# GIC Python Car Simulation

## How to Run the App

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone <repo-url>
   cd gic-python
   ```

2. **Set up a virtual environment (recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   This project uses only the Python standard library, so the requirements.txt may be empty, but this ensures future compatibility.

4. **Run the simulation:**
   ```bash
   python main.py
   ```
   or, if you want to use the CLI directly:
   ```bash
   python src/cli.py
   ```

5. **Run the tests:**
   ```bash
   python -m unittest discover tests
   ```
   or, if you use pytest:
   ```bash
   pytest
   ```

---

## Future Improvements

- **Optimize Field Storage:**
  - Store cars in a dictionary with positions as keys for faster access and lookup.
- **Enhanced Collision Reporting:**
  - Return all cars at a collision point instead of just one, allowing for more detailed collision handling and reporting.
- **Enhanced CLI/UX:**
  - Add input validation and error handling for user commands in the CLI.
  - Provide more informative messages and help options for users.
- **Simulation Features:**
  - Support for step-by-step simulation and the ability to pause/resume.
  - Add the ability to save and load simulation states.
- **Field and Car Logic:**
  - Allow for obstacles or different terrain types on the field.
  - Support for different car types with varying movement rules or speeds.
- **Testing and Quality:**
  - Increase test coverage, especially for edge cases and error handling.
- **Performance and Scalability:**
  - Optimize simulation for large numbers of cars or larger fields.
  - Consider parallelizing simulation steps if appropriate.
- **Extensibility:**
  - Make it easy to add new commands or car behaviors via plugins or configuration.
- **Visualization:**
  - Add a simple graphical or web-based visualization of the field and cars.

---

Feel free to contribute or suggest more improvements!
