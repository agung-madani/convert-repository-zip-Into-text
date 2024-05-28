# Convert Repo Into Text

This application allows users to upload a ZIP file of a repository and displays the content of the files in the repository.

## Getting Started

To get a local copy up and running, follow these steps:

1. Clone the repository.
2. Install the required dependencies.
3. Run the application.

## Usage

1. Navigate to the home page.
2. Click on the upload button to upload a ZIP file.
3. The application will display the content of the files in the repository.

## Code Overview

The application is built with Flask and uses the following routes:

- [`/`](../../../z:/python/convertRepoIntoText/app.py): Renders the home page.
- [`/upload`](../../../z:/python/convertRepoIntoText/app.py): Handles the file upload and processing.

The application uses the [`handle_zip_file`](../../../z:/python/convertRepoIntoText/app.py) function to extract the content of the files from the uploaded ZIP file and pass it to the [`display_files.html`](../../../z:/python/convertRepoIntoText/templates/display_files.html) template.

## Contributing

Contributions are welcome. Please open an issue or submit a pull request.

## License

This project is licensed under the terms of the MIT license.