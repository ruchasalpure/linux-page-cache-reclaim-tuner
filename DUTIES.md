# Duties and Responsibilities for Linux Page Cache Reclaim Tuner Agent

## Dual-Control Architecture
Maker:
cgroup-reclaim-tuner

Checker:
oom-protection-checker

## Operational Workflow
1. The Maker (cgroup-reclaim-tuner) analyzes incoming telemetry, context, and requirements.
2. The Maker synthesizes a draft operational execution plan with supporting data.
3. The Checker (oom-protection-checker) independently verifies all assumptions and constraints.
4. If validation passes, the plan is signed, logged, and committed.
5. All actions are appended to the immutable governance audit trail.
