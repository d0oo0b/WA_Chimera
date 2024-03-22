# WA_Chimera

This program is designed to facilitate the process of reading exported XLSX files from the AWS Trusted Adviser service and registering the identified risks into a workload created through a specified Custom Lens. This helps identify and track high-risk P0 and P1 issues for improvement.

## Usage

1. Ensure you have a Python 3 environment with a version not lower than Python 3.12.2.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Execute the program by running `python3 WA.py`.
4. Import the XLSX file exported from the AWS Trusted Adviser service.
5. Upon successful execution, the analysis results will be output to the `TA-check.xlsx` file in the current directory.
6. Refer to the `TA-check.xlsx` file and manually create/modify the workload in the WA Tool accordingly.

## Supported Custom Lens

The current supported Custom Lens is:
https://gitlab.aws.dev/aws-gcr-sa/gcr-war-key-workload-custom-lens (March 1st version)
