## Mars Rover Task

### Prerequisites
1. Navigate to the root of the project

2. Optionally create and source a new virtual environment:
> python -m venv venv
> 
> source venv/bin/activate

3. Install requirements:
> pip install -r requirements.txt

### Run
1. Navigate to the root of the project
2. Run using the command:
> python run.py

Results will be printed to standard out. To change the input, edit the contents of `input.txt` in the root directory.

### Test
A test suite is available under the `test` directory.
In order to run the tests:
1. Navigate to the root of the project
2. Run the tests using the command:
> pytest test
 
### Future Work
- Replace the `move_forward()` function in `robot.py` with something more elegant
- Consolidate State and Position classes
- Replace the `parse_state()` function in `move_executor.py` with something more elegant
- Add error handling (and tests) around invalid initial states
  - e.g. grid instantiated as (2, 2) but the starting position is (3, 3, E)
- Add validation of world state initialisation
- Parameterise the movement tests
- Add robust handling of input
  - e.g. multiple world instantiations in one file
- Add some handling for overlap of robots