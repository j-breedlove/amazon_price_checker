# Amazon Price Alert

This tool allows you to monitor the price of a product on Amazon and sends an email alert if the price falls below a certain threshold.

## Features
- Fetches the current price of a specific Amazon product.
- Sends an email if the price drops below a set threshold.
- Uses environment variables for email and password to ensure security.

## Setup and Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/j-breedlove/amazon_price_checker.git
    cd amazon_price_checker
    ```

2. **Install the required packages:**
    ```bash
    pip install requests beautifulsoup4 python-decouple
    ```

3. **Setup environment variables:**
    - Create a `.env` file in the root directory of the project.
    - Add the following lines to the `.env` file:
      ```
      MY_EMAIL=your_email@gmail.com
      PASSWORD=your_email_password
      ```

## Usage

1. Set the desired product URL and price threshold in the `refactored_code.py`.
2. Run the script:
    ```bash
    python main.py
    ```

## Important Note
- Ensure you have less secure apps access enabled for the Gmail account used for sending emails. [Click here](https://myaccount.google.com/lesssecureapps) to manage this setting. 
- Be cautious about sharing any code or files that contain your `.env` or any sensitive information.
- Consider using application-specific passwords if you're using 2-factor authentication for your Gmail account.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)

---
