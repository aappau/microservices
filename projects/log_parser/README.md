## Log Parser
This program parses a log file and extract IP addresses from the file.

## What it does
- Accepts path to a log file as a user provided argument
- Counts the occurances of an IP address in the log file
- Saves the output of the program in a csv file

## Modules
- re
- csv
- argparse
- collections

## How to Run?
Run the commands below from the root of `log_parser` directory

- Help
```
python run.py -h
```

- Log Parser
```
python run.py <log_file>
```