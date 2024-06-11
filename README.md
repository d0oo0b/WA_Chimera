# WA_Chimera
<img src="/Chimera.png" alt="WA Chimera" width="300">
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

**The logic for updating WA notes**: It aims to preserve as much historical log in the notes as possible, with the most recent updates placed at the top. Due to the 2048 character limit, only the latest 2000 characters of the log will be retained.

If you encounter any issues, please report them in the "Issues" section of this repository.


## Supported Custom Lens

The current supported Custom Lens is:
https://gitlab.aws.dev/aws-gcr-sa/gcr-war-key-workload-custom-lens (March 1st version)

When lens.json changes, it needs to be processed by the pjson.py program to generate a new output.csv file. Whether to automatically trigger the update of lens.json based on the updates of gcr-war-key-workload-custom-lens is still under consideration. If necessary, this feature will be supported in future versions.
