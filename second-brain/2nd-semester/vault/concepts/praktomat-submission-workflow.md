---
title: "Praktomat Submission Workflow"
tags: [concept, scaling-database-systems, semester-2, tooling, assessment]
course: "Scaling Database Systems"
source_count: 2
status: current
last_updated: 2026-10-20
prerequisites: ["[[scaling-database-systems]]"]
---

## One-line Summary
Praktomat is the course's only submission channel: an automatically checking, deadline-enforcing platform where the Final Solution is the most recent submission that passed every required test.

## Core Intuition

Praktomat closes a gap that a mailing list cannot. A hand-in directory, an email attachment, or a
Stud.IP post can all receive a file without knowing whether the file is correct. Praktomat does not
merely store what you upload - it *checks* it, immediately, against the tests the exercise defines,
and it tells you why it was rejected.

That feedback is only useful because the acceptance rule is monotone in a specific way. Your Final
Solution is your most recent *passing* submission, and it survives later failures. That turns the
platform into a sandbox for experimentation rather than a one-shot slot machine: you can try a
risky implementation, watch it fail, and still hold the accepted version. A platform where the last
upload always won would make experimentation irrational.

The same design explains the hard cutoff. "Submissions are no longer possible after the deadline.
Submissions by other means, such as email attachments or printed copies, are not accepted." There
is no grace period, but there is also no alternative route: if it is not in Praktomat, it is not
submitted. That single channel is what makes the cutoff enforceable and the Final Solution
well-defined.

One thing the platform does not do is grade. The check is a precondition for acceptance, not an
assessment: "Praktomat automatically checks your submissions but does not assign grades for these
exercises. Therefore, you can ignore the Result Overview section." Reading a passed check as a score
misreads the system.

## Formal Definition / Statement

The mechanics as stated by the Praktomat sheet:

- **Access.** Praktomat is "only accessible from within the University of Passau's network"; from
  outside, a VPN connection is required. URL: `https://praktomat.sdbs.fim.uni-passau.de`.
- **Instance selection.** The home page lists active courses with their instances. Choose
  "Scaling Database Systems" in "Wintersemester 26/27"; it opens that instance's login page.
- **Accounts are per instance and not integrated.** "Praktomat is not integrated with the
  university's authentication system. Therefore, you need a separate Praktomat account. Each
  Praktomat instance has its own user accounts. Even if you already have an account for another
  (e.g., older) instance, you must register again for the instance used in this course."
- **Registration fields.** Username, first name, last name, email address, matriculation number,
  password, and password confirmation - all required. Only email addresses of the form
  `<ZIM-name>@ads.uni-passau.de` are accepted.
- **Activation.** A confirmation email with an activation link is sent to the address provided; if
  it does not arrive, check the spam folder. On first login a disclaimer must be accepted,
  including the declaration of authenticity and the data privacy statement.
- **Exercises.** The overview lists the exercises, with each submission deadline below its title.
  "Submissions are no longer possible after the deadline. Submissions by other means, such as
  email attachments or printed copies, are not accepted."
- **Checking, not grading.** Submissions are checked automatically; no grades are assigned; the
  Result Overview can be ignored.
- **Submission page.** My Solutions on the exercise detail page shows previous submissions and
  accepts a new one. The page shows a Solution History and the current Final Solution on the
  right; the upload panel on the left has *Choose File*, plus `+` and `-` buttons for exercises
  allowing multiple files. "Make sure to use this exact filename when uploading your solution.
  Click Upload to submit your files. Praktomat checks them immediately."
- **Resubmission and the Final Solution rule.** "You can submit new versions as often as you
  like before the deadline. The Final Solution is your most recent submission that passed all
  required tests. If you submit another solution that fails the tests, your previously accepted
  solution remains your Final Solution."
- **Acceptance and rejection.** A submission is accepted if it passes all required tests. If it
  fails at least one, it is rejected and the reason displayed - the sheet's own example is an
  uploaded file that does not match the required filename `submission.pdf`.
- **Scope.** The exercise kickoff sheet states: "We will use Praktomat for all kinds of submissions
  (e.g., Milestones)." It also forbids public disclosure: "Do not make any submission public",
  naming posting milestone code in the Stud.IP forum and uploading a submission to a public GitHub
  repository as examples.

## Key Properties

- **Single channel.** No email attachments, no printed copies, no Stud.IP hand-in. If it is not
  in Praktomat, it is not submitted.
- **Hard cutoff.** After the deadline, submission is impossible. No grace period and no
  late-submission route - because no other route exists.
- **Check ≠ grade.** The automatic check is a precondition for acceptance, not an assessment.
- **History is preserved.** Every submission stays visible in the Solution History, and a
  previously accepted solution survives later failures. The Final Solution advances only when a
  new submission passes.
- **Filename is part of the contract.** A mismatch with the specified filename is a rejection
  reason - a mechanical check that costs nothing to satisfy and is fatal to ignore.
- **Accounts are per instance, and identity is manual.** No SSO. The ZIM-name email form is
  enforced, and a student with an older instance must register again.
- **Activation is a manual step.** No account exists until the emailed link is clicked; the first
  login then requires the disclaimer.

## Worked Example

A concrete milestone submission, walked through the state machine. The states are: *no account* ->
*registered, awaiting activation* -> *active, no submission* -> *has a passing submission (Final
Solution set)* -> *latest submission failing (Final Solution unchanged)* -> *closed*.

**Step 0 - access.** The student is at home. Praktomat is reachable only from inside the Passau
network, so they bring up the university VPN (the eduVPN page is in the sheet's footnote) and open
`https://praktomat.sdbs.fim.uni-passau.de`.

**Step 1 - instance.** The student chooses "Scaling Database Systems" in "Wintersemester 26/27" and
lands on that instance's login page.

**Step 2 - register.** The student has an account from an older instance, so they go to Register:
username, first name, last name, email (`<ZIM-name>@ads.uni-passau.de`), matriculation number,
password, and password confirmation - seven fields, all required. A private address would be
refused.

**Step 3 - activate.** The confirmation email lands in spam; the student finds it and clicks the
link. On first login the disclaimer is accepted. State: *active, no submission*.

**Step 4 - read the description.** The exercise page shows the deadline below the title and
repeats it next to the description. The description specifies the required filename - the student
notes the exact name, `submission.pdf` in the sheet's own example.

**Step 5 - first upload, wrong filename.** The student uploads the file as `submission_final.pdf`
and clicks Upload. Praktomat checks immediately, the submission fails at least one required test,
and it is rejected with the reason displayed: the uploaded file does not match the required
filename. State: *active, no submission, rejection reason shown*. The Solution History now lists
this attempt.

**Step 6 - second upload, correct filename, tests pass.** The student renames the file to the
specified name, uploads again, and Praktomat accepts it because it passes all required tests. The
Final Solution is now this submission. State: *has a passing submission*.

**Step 7 - third upload, later, fails.** Before the deadline the student experiments: a different
implementation fails one required test. Praktomat rejects it and shows the reason. The Final
Solution does **not** change - the sheet is explicit that the previously accepted solution remains
the Final Solution. State: *latest submission failing, Final Solution unchanged*. The final state
depends only on the most recent *passing* submission.

**Step 8 - deadline.** The deadline passes. Submission is impossible. The Final Solution stands as
it was. State: *closed*.

## Common Pitfalls

- **Reading the Result Overview as a grade.** The check does not assign grades; treating a
  passed check as a score misreads the system.
- **Assuming an old Praktomat account still works.** Accounts are per instance; register again.
  Using a non-ZIM email address fails registration outright, and the activation mail never arrives.
- **Not checking the spam folder.** The activation email can land in spam, and an unactivated
  account cannot be used.
- **Renaming the file "improvefully".** A mismatch with the specified filename is a rejection
  reason, and the cheapest way to fail a technically correct submission. Uploading only one file
  when the exercise allows several fails the same way - the `+` and `-` buttons exist for that.
- **Probing the deadline with a last-minute upload.** There is no grace period. Uploading
  something uncertain is safe - the Final Solution rule protects you - but it must happen
  *before* the deadline.
- **Believing a failed later upload destroyed the accepted one.** It does not. This is the safety
  property students fail to exploit: experiment freely before the deadline.
- **Handling a submission outside Praktomat, or posting it publicly.** Email attachments and
  printed copies are not accepted, and milestone code must not be published to the Stud.IP forum
  or a public GitHub repository. A solution handed in any other way was not handed in.

## Connections

- [[scaling-database-systems]] - the course page; this workflow serves its milestones.
- [[minihive-project-structure]] - the artefact that gets submitted, and the milestone series.
- [[rootless-docker-server-access]] - where the submission is tested before upload; also network-bound.
- [[git-commit-hygiene]] - the version history behind the submitted files.
- [[git-branching-and-merging]] - how milestone variants are kept apart while the channel holds one current file.
- [[reproducible-builds]] - why the container-tested artefact is the thing that gets submitted.
- [[containerization-for-builds]] - the packaging practice behind the tested artefact.

## Open Questions

- **The exercises themselves are unknown.** The sheet describes the mechanism, not the content.
  The list of exercises, their deadlines, and their required tests are not in the material.
- **Which artefacts are submitted is unknown.** Source archive, container image, report, or
  single script is not stated; the filename example `submission.pdf` is illustrative.
- **The test suite behind the automatic check is unknown.** What the required tests verify, how
  they run, and whether they are the miniHive container's tests is not stated.
- **The meaning of the Final Solution for grading is unknown.** The sheet is precise about the
  mechanic, but how the Final Solution is used afterwards - graded artefact, gate, or checkpoint -
  is not in the material.
- **The number of allowed files and their naming for multi-file exercises is unknown.** The `+`
  and `-` buttons exist, but the naming rules are not stated. Whether the milestone deadlines align
  with the exercise sheet deadlines is also not stated.
- **The disclaimer's content is unknown.** The sheet names the declaration of authenticity and
  the data privacy statement but does not reproduce them. What happens to a submission after the
  course ends - retention, deletion, later use - is not addressed either.
