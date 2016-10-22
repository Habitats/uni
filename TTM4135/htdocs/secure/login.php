<?
  require_once '../lib/user.php';

  $username = $_POST['username'];
  $password = $_POST['password'];

  $user = User::get_by_username($username);
  $status = 0;

  if (isset($user) && password_verify($password, $user->password_digest)) {
    $status = 1;

    $_SESSION['id']       = $user->id;
    $_SESSION['username'] = $user->username;
  }

  header('Location: /?status=' . $status);
