<?
  set_include_path('../../lib');
  require_once 'user.php';
  require_once 'csrf.php';

  $name  = $_POST['CSRFname'];
  $token = $_POST['CSRFtoken'];

  if (!CSRF::csrfguard_validate_token($name, $token)) {
    header('Location: index');
  } else {
    $id = $_POST['id'];

    $user = User::get_by_id($id);
    $username = '';

    $msg = '';
    $status = 0;

    if (isset($user) && $user->delete()) {
      $username = $user->username;
      $status = 1;
    }

    header('Location: index?status=' . $status . '&username=' . $username);
  }
