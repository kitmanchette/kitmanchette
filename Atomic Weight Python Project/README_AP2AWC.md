# ATOMIC PERCENT TO WEIGHT PERCENT CONVERTER
### Video demo: <https://youtu.be/XQ99goJKEck>
## Description:
In my current work as a Reliability and Failure Analysis Engineer, I often complete elemental analysis of failed thermoelectric devices to determine failure root cause. An EDS (energy dispersive x-ray) instrument is used, which determines the percentage of elemental constituents in a sample. Knowing this information is often critical to determine failure mode and root cause.

The image below (a cross-sectioned thermoelectric device, focus on the semiconductor, metallization, and solder interface) is an example of the elemental analysis that can be provided by an EDS instrument:
![Alt text](image.png)

EDS data is usually saved in either atomic percent or weight percent. However, some analysis make more sense with weight percent and some make more sense with atomic percent. Converting between the two uses a formula including Avogadro's number and the elemental weight, and can be time consuming when doing a large analysis of many elemetal spectra.

To save time, I wrote the Atomic Percent to Weight Percent Converter (APWPC) (=since I usually save EDS data in atomic percent for simplicity. The APWPC contains elemental weight data for all non-radioactive elements, and prompts the user for number of elements present, atomic symbols present, and atomic percent of only the present elements. Each step only asks for the information strictly necessary, and contains error handling.

The error handling assumes both malicious and non-malicious intent by the user! For example, when the program prompts the user for the atomic percentages present, if the user inputs atomic percentages that sum to more than 100% it is not assumed that the intent is malicious. It's possible that a typo or mis-enter of this data is the cause, so the user has the option to re-try entering this data without needing to quit the program and start over. This is a great time-saver when inputting a large amount of data, since one typo doesn't break the program flow.
```
atomic_percents = []
    while True:
        try:
            for i in range(len(e)):
                atomic_percents.append(float(input(f"Atomic percentage present of {e[i]}: ")))
            if sum(atomic_percents) <= 100:
                return atomic_percents
            else:
                if input("Atomic percent total must be less than 100. Try again? ").lower() == "y":
                    atomic_percents = []
                    pass
                else:
                    sys.exit()
        except ValueError:
            sys.exit("Must input a valid number for atomic percent.")
```

This section of the code is "friendly" to the user in that it asks them if they made a typo and want to try again, or if they just want to exit the code.

```
if input("Atomic percent total must be less than 100. Try again? ").lower() == "y":
                    atomic_percents = []
                    pass
                else:
                    sys.exit()
```

At the end of the program, the code displays each element present, along with its newly calculated weight percent as a print statement. This allows the user to easily copy this data into their intended application (excel sheet, powerpoint slide, email, etc.)

To facilitate testing the many different user inputs, the test_project.py file uses the `monkeypatch` method via the pytest library to simulate user input:

```
def test_get(monkeypatch):
    #using monkeypatch to mock correct user input
    monkeypatch.setattr('builtins.input', lambda _: "Ni")
    inp = input("Atomic symbol: ")
```

Several decision points happened along the course of writing this code.
1. Which operation should be performed - At% to Wt%, or Wt% to At% (or both)?
    - I chose to onl;y perform the atomic percent to weight percent calculation due to simplicity and by knowing my use case. I rarely have a use case for needed to convert from weight percent to atomic percent.
    - However, a great next step to expand this program would be to allow the user to choose which format they have (At% or Wt%) and allow them to convert either way. This would make the code more useful to more people.
2. How vigilant should the code be at catching errors, and how strict should the code be when encountering an error?
    - I made this code for my use case, and originally assumed I would input things correctly. So, I started out this program with no error handling present.
    - However, I wanted the code to be more robust in case I made a typo or later wanted to expand the program's audience.
    - Some errors are treated harshly, and the code uses `sys.exit()` to close the program (for example, if `cat` is inputted when asked for an atomic percent, I assumed things were too far gone and the program should be restarted).
    - Other errors are treated gently, and the code prompts the user. For example, if the atomic percentages given add to more than 100%, this could be caused by a simple typo in data entry. Or, it could be a mistake the program should be restarted. For best usability, the user is asked if they want to try again from the atomic percent entry step or if they want to start over. This allows flexibility in the code.

```
while True:
        try:
            for i in range(len(e)):
                atomic_percents.append(float(input(f"Atomic percentage present of {e[i]}: ")))
            if 0 < sum(atomic_percents) <= 100:
                return atomic_percents
            else:
                if input("Atomic percent total must be greater than 0 and less than 100. Try again? ").lower() == "y":
                    atomic_percents = []
                    pass
                else:
                    sys.exit()
        except ValueError:
            sys.exit("Must input a valid number for atomic percent.")
```

3. How much data should the program provide to the user?
    - In terms of error handling, most errors are caught and a `sys.exit()` display informs the user and quits the program, or a `print()` statement informs the user and allows them to try the data entry again.
    - All calculations are hidden from the user to limit information overload and to keep the terminal free of extraneous information.
    - This program does not explain atomic percent vs weight percent and assumes the user knows the difference, and knows what format their data is already in.


The following files are included in this project:
- The project.py file contains the full code for the APWPC and displays the final weight percent figures in the terminal.

- The test_project.py file contains the pytest code and tests several edge cases, as well as correct user input.

- The requirements.txt file contains the needed libraries for all files contained herein.
