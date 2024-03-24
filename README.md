# WA_Chimera

This program is designed to facilitate the process of reading exported XLSX files from the AWS Trusted Adviser service and registering the identified risks into a workload created through a specified Custom Lens. This helps identify and track high-risk P0 and P1 issues for improvement.

## Usage

1. Ensure you have a Python 3 environment with a version not lower than Python 3.12.2.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Execute the program by running `python3 WA.py`.
4. Import the XLSX file exported from the AWS Trusted Adviser service.
5. Upon successful execution, the analysis results will be output to the `TA-check.xlsx` file in the current directory.
6. Refer to the `TA-check.xlsx` file and manually create/modify the workload in the WA Tool accordingly.

### New Feature in V2: Update to AWS WA Tool

In the V2 version, a new feature has been added to update the NOTES of questions in AWS WA Tool. Before using this feature, you need to set up your AWS Access Key and Secret Access Key. Please refer to the documentation for setting up your AK/SK (set them in your system environment variables, following the AWS CLI installation and setup documentation: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html).

After setting up your AK/SK, you can click on the "Setting" option in this application to configure the Region, Workload, and Lens. Once you have successfully imported the exported XLSX files from the AWS Trusted Adviser service, you can perform the "Update Workload" operation.

**Note:** In the Settings, there is an option to determine whether to overwrite or append to the existing notes when updating the workload. If you choose not to overwrite, the new notes will be appended to the existing ones. However, each note in the AWS WA Tool has a length limit, and appending may cause errors due to exceeding this limit. Error messages can be found in the `output.log` file.

If you encounter any issues, please report them in the "Issues" section of this repository.


## Supported Custom Lens

The current supported Custom Lens is:
https://gitlab.aws.dev/aws-gcr-sa/gcr-war-key-workload-custom-lens (March 1st version)

