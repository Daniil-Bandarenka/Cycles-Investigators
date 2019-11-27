# Cycles-Investigators


Here we have scripts that can help us investigate when cycles are updated.

### Sites with cycles
- [ ] 001 - temporarily unavailable
- [X] 009
- [X] 018
- [X] 019
- [X] 038
- [X] 074
- [X] 075
- [X] 076
- [ ] 081 - temporarily unavailable
- [ ] 133 - temporarily unavailable

Algorithm is simple, script just gets page source and finds info about current cycle.
This info is printed to terminal, but when it is used by cron job, it is printed to specified (in cron config) file.
So I propose to create a separate cron job for each script. 

### Cron job example

`*/15 * * * * cd <working_dir> && /usr/bin/python3.7 investigators/<script_name>.py >> stats/<script_name>.log 2>&1`

### Output format

`2019-11-27 03:46:03.569194 : Intra Day 2 Cycle 3`

`2019-11-27 04:01:03.746208 : Intra Day 2 Cycle 3`

### Notes

- You have to create `stats` folder, please, pay attention
- Inexplicably, now we can't access sites which we use with Selenium.
