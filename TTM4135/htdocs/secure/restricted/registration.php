<?
  set_include_path('../../lib' . PATH_SEPARATOR . '../include');
  include 'user.php';
  include 'user_validations.php';

  if (isset($_POST['submit'])) {
    $given_name      = $_POST['user_given_name'];
    $family_name     = $_POST['user_family_name'];
    $username        = $_POST['username'];
    $email           = $_POST['user_email'];
    $password        = $_POST['user_password'];
    $password_digest = password_hash($password, PASSWORD_DEFAULT);

    $password_confirmation = $_POST['user_password_confirmation'];
    $email_confirmation    = $_POST['user_email_confirmation'];

    $errors = false;

    if (User::get_by_username($username) !== NULL) {
      $username_exists = $errors = true;
    }

    if (User::get_by_email($email) !== NULL) {
      $email_exists = $errors = true;
    }

    if ($password !== $password_confirmation) {
      $password_confirmation_error = $errors = true;
    }

    if ($email !== $email_confirmation) {
      $email_confirmation_error = $errors = true;
    }

    $given_name_error  = !valid_name($given_name);
    $family_name_error = !valid_name($family_name);
    $password_error    = !valid_password($password);
    $email_error       = !valid_email($email);

    if ($given_name_error || $family_name_error || $password_error || $email_error) {
      $errors = true;
    }

    if ($errors) {
      if ($_POST['redirect_to'] == 'register') {
        include 'register.php';
      }
      if ($_POST['redirect_to'] == 'admin') {
        include '../admin/index.php';
      }
    } else {
      $user = new User('', $given_name, $family_name, $username, $email, $password_digest);
      $user->save();

      if ($_POST['redirect_to'] == 'register') {
        header('Location: /restricted/confirmation');
      }
      if ($_POST['redirect_to'] == 'admin') {
        header('Location: /admin?user_created=1');
      }
    }
  }
