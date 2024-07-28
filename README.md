# Login reCAPTCHA Prototype

This repository contains a prototype for a login system with Google reCAPTCHA with Instagram Integration. It is designed to provide a secure authentication mechanism by preventing automated bots from logging in.

## Features

- User login form with reCAPTCHA verification
- Integration with Google reCAPTCHA v3
- Basic user authentication system

## Technologies Used

- HTML
- CSS
- JavaScript
- PHP
- MySQL
- Google reCAPTCHA v3

## Setup Instructions

### Prerequisites

- Web server with PHP support (e.g., XAMPP, WAMP, MAMP)
- MySQL database

### Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/xyukii/loginrecaptchaprototype.git
    cd loginrecaptchaprototype
    ```

2. **Create a MySQL database:**
    - Open PHPMyAdmin.
    - Create a new database named `loginrecaptcha`.
    - Import the `database.sql` file provided in the repository.

3. **Configure database connection:**
    - Open `config.php`.
    - Update the database credentials:
    ```php
    <?php
    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "loginrecaptcha";
    ?>
    ```

4. **Set up Google reCAPTCHA:**
    - Go to the [Google reCAPTCHA admin console](https://www.google.com/recaptcha/admin/create).
    - Register a new site and get your Site Key and Secret Key.
    - Update the `config.php` file with your reCAPTCHA keys:
    ```php
    <?php
    $recaptcha_site_key = "your_site_key";
    $recaptcha_secret_key = "your_secret_key";
    ?>
    ```

### Usage

1. **Start your web server:**
    - If using XAMPP, open the XAMPP Control Panel and start Apache and MySQL.

2. **Access the login system:**
    - Open your web browser and navigate to `http://localhost/loginrecaptchaprototype`.

3. **Login:**
    - Use the provided form to login. The reCAPTCHA verification will ensure that only human users can log in.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Google reCAPTCHA](https://www.google.com/recaptcha)
- [XAMPP](https://www.apachefriends.org/index.html)

