# Cycles-Investigators


Here we have scripts that can help us investigate when cycles are updated.

### Sites with cycles
- [X] [001](http://services.kernrivergas.com/portal/Informational-Postings/Capacity/Operationally-Available)
- [X] [009](https://peplmessenger.energytransfer.com/ipost/PEPL/capacity/operationally-available-by-location)
- [X] [018](https://tgcmessenger.energytransfer.com/ipost/TGC/capacity/operationally-available-by-location)
- [X] [019](https://rovermessenger.energytransfer.com/ipost/ROVER/capacity/operationally-available-by-location)
- [X] [038](http://www.northwest.williams.com/NWP_Portal/CapacityResultsScrollable.action)
- [X] [074](https://sermessenger.energytransfer.com/ipost/SER/capacity/operationally-available-by-location)
- [X] [075](https://swgsmessenger.energytransfer.com/ipost/SWGS/capacity/operationally-available-by-location)
- [X] [076](https://GSTmessenger.energytransfer.com/ipost/GST/capacity/operationally-available-by-location)
- [X] [133](https://transmission.wbienergy.com/informational_postings/capacity/operational_capacity_locations.aspx)

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
