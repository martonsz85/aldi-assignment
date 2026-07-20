**1. Broken/missing application code**
The application code was missing from the repo. Before committing, make sure the application starts locally and the endpoints behave as expected. This means that components that build upon this (e.g. Helm chart) don't work, either. Having non-working code in the main branch makes it hard to build on top of your work. Test all changes locally before pushing your commits.

**2. Missing or incomplete documentation**
The Helm chart and Terraform code didn't have a README.md to describe what it is and how it works. Even a small service/component needs a minimal README so others can understand and test it. Without documentation, other engineers can’t test or extend the work.

**3. Commit structure**
Everything landed in one large commit. Try to break changes into smaller, logically grouped commits (e.g., app code, Helm chart, Terraform). This makes reviews easier and helps you reason about your own changes. This is especially useful if there is a larger change that affects multiple modules/components.

**4. Helm chart correctness**
Several chart values were defined but never used, and some ports/selectors didn't match the application. Make sure the chart reflects the actual container configuration so deployments work reliably.

**5. Terraform resource usage**
Terraform variables were defined but unused, and some resources didn't match current provider behavior. Either update the Terraform code to the current provider syntax, or explicitly pin the providers to the major version that matches the syntax you’re using. All-in-all, align the Terraform code with the chart and the application so CI/CD can deploy consistently.
