# Data Change Notes

### Modified
---
* values of "-" have been marked as null and not imported.
* `friskflag` and `arrestflag` mapped as booleans with `Y`/`N` translated as `true`/`false`
### Removed
---
No Removals at this time


### Notes
---
* Reported Date/Reported Time do not correlate to the date/time of the stop. For this
  reason, we will not use _Reported Time_ logging metrics. Reported Date is most often within
  1-day of incident. For this reason date based data will not be accurate for pinpointing a
  particular incident
  fields
