# TallerChallenge

Candidate Assessment – QA Engineer (Manual-Focused with Basic
Automation Skills)

Total time: Approximately 20 minutes
Focus: 70% Manual QA, 30% Basic Automation
Tools: Any programming language and any UI automation framework

Part 1 – Manual QA Analysis (5 minutes)

Using the following page: https://demoqa.com/text-box

Provide concise written answers (bullet points are acceptable) for the
following:
1. Acceptance Criteria
a. List the key acceptance criteria required for this form to be
considered functioning correctly.

2. Essential Test Cases
a. List the minimum set of important test cases, including positive,
negative, and basic validation scenarios.

3. Risks / Edge Cases
a. Identify potential risks, edge cases, or areas where defects
commonly appear.

The expected answer is short and to the point. No formal documentation
format is required.

Part 2 – Light Automation Task (15 minutes)

You may use any programming language and any automation framework
you prefer, such as Selenium, Playwright, Cypress, WebDriverIO, etc. Also you
may also use any HTTP client or library for the API request.

UI Automation Requirements

1. Automate the following flow: Navigate to: https://demoqa.com/text-box
2. Fill the form fields with the following values:
a. Full Name: John Doe
b. Email: john.doe@example.com
c. Current Address: 123 Main St
d. Permanent Address: 456 Secondary St
e. Submit the form.
f. Validate that the displayed output values match exactly the
values submitted.

API Validation Requirements

1. Send a GET request to: https://jsonplaceholder.typicode.com/posts/1
2. Validate the following:
a. The response status code is 200
b. The JSON response contains the keys: userId, id, title, body
c. The value of the id field is equal to 1
d. Final Output
i. If all UI and API validations pass, print the following
message exactly: All tests passed
ii. If any validation fails, return or throw an error with a clear,
descriptive message indicating what failed.

Deliverables
Upload the following to a public GitHub repository:

1. A single script or test file containing your solution (for example:
test_form.js, solution.py, Main.java, etc.)
2. A short README.md including:

a. Prerequisites
b. How to run the script
c. Expected output
d. Evaluation Criteria
e. Manual QA thinking and clarity
f. Ability to write simple and readable automation
g. Correctness of UI validation
h. Correctness of API validation
i. Cleanliness and simplicity of the code
