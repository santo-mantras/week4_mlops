# WEEK4 MLOPS ASSIGNMENT SUBMISSION SEPT 2025 

## Submission by - Roll no - 21f1000243, Name - Santosh Kumar Verma, Mail - 21f1000243@ds.study.iitm.ac.in 

# MLOps Pipeline for Iris Classification with DVC & GitHub Actions

This project demonstrates a complete MLOps workflow for the Iris dataset. The primary goal is to establish a robust system for versioning data and models, automating tests, and implementing Continuous Integration (CI) to ensure code quality and model performance.

## Project Workflow

The project was executed in two main phases:

### Phase 1 - Data & Model Versioning (DVC + Git)

This phase focused on creating two distinct, reproducible versions of the model and its corresponding data.

1. Environment Setup: The project was initialized in Google Cloud Shell, and DVC was configured to use a GCS bucket as remote storage for large files.

```bash
# Configure DVC to point to a GCS bucket
dvc remote add gcs_remote gs://mlops-course-bionic-insight-xxxx-xx-unique/week4
dvc remote default gcs_remote
```
2. Version 1 (v1):

- The initial dataset (v1/data.csv) was split into training (70 rows) and testing (31 rows) sets.
- A Decision Tree classifier was trained on this data, achieving an accuracy of 77.42%.
- All data artifacts and the trained model (v1_model.joblib) were versioned using dvc add and dvc push.This state was locked in with a Git tag: git tag -a "v1".

3. Version 2 (v2):

- A second dataset (v2/data.csv) was introduced and split.
- The training data was augmented by combining the training sets from v1 and v2 (total 104 rows).
- The model was retrained on this richer dataset, significantly improving the accuracy to 100.00% on the v2 test set.
- The new model (v2_model.joblib) and data were versioned, and a v2 Git tag was created.

### Model Performance Comparison

| Model Version | Training Data |Test Accuracy | 
| :--- | :--- | :--- |
| v1_model.joblib | Initial Dataset (70 rows) | 77.42% |
| v2_model.joblib | Augmented Dataset (104 rows) | 100.00% |

### Phase 2 - Continuous Integration (GitHub Actions)

This phase focused on automating quality checks for any new code changes.

 1. Test Development: Using pytest, two critical unit tests were created:

    - test_data_validation: Ensures the input data has the correct columns and no null values.

    - test_model_evaluation: Checks that the v2 model's accuracy is above a minimum threshold of 80%.

 2. CI Workflow: A GitHub Actions workflow (.github/workflows/ci.yml) was built to run on every pull request. The automated job performs the following:

    - Checks out the source code.

    - Sets up Python and installs dependencies from requirements.txt.

    - Authenticates with Google Cloud using a repository secret (GCP_SA_KEY_MLOPS).

    - Pulls the versioned data and models from GCS using dvc pull.

    - Executes the pytest suite.

    - Uses CML (Continuous Machine Learning) to post the test results as a comment directly on the pull request.

# Challenges and Solutions 🐛💡

During the setup, several common MLOps hurdles were encountered. The table below summarizes the problems and their solutions.

| Problem | Solution |
| :--- | :--- |
| **`dvc: command not found`** in the local shell. | The user's `PATH` variable was updated by adding `export PATH="$PATH:/home/user/.local/bin"` to `~/.bashrc`. |
| **`No module named 'dvc_gs'`** during `dvc push`. | The GCS-specific dependency was missing. It was installed directly using `pip install dvc-gs`. |
| **`cml: command not found`** in the CI pipeline. | The CML tool was not installed in the runner. The line `npm install -g @dvcorg/cml` was added to the workflow. |
| **`Resource not accessible by integration`** when CML tried to comment on the PR. | The default `GITHUB_TOKEN` lacked write permissions. This was fixed by adding a `permissions: pull-requests: write` block to the CI job. |
| **`dvc pull` failed in CI** due to `No remote provided`. | The DVC remote configuration file (`.dvc/config`) was not tracked by Git. The solution was to `git add .dvc/config` and commit it. |

# Final CI Sanity Check Report 🧪

The successful CI pipeline automatically generated the following report on the pull request, confirming that all tests passed and the proposed changes are safe to merge.

```bash
Pytest Sanity Check Report
============================= test session starts ==============================
platform linux -- Python 3.10.19, pytest-8.4.2, pluggy-1.6.0 -- /opt/hostedtoolcache/Python/3.10.19/x64/bin/python
cachedir: .pytest_cache
rootdir: /home/runner/work/week4_mlops/week4_mlops
plugins: hydra-core-1.3.2
collecting ... collected 2 items

tests/test_pipeline.py::test_data_validation PASSED                      [ 50%]
tests/test_pipeline.py::test_model_evaluation PASSED                     [100%]

============================== 2 passed in 1.27s ===============================
```
## END