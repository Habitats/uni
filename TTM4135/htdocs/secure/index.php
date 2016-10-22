<?
  set_include_path("../lib" . PATH_SEPARATOR . "./include");
  require_once 'helpers.php';

  /**
   * @return mixed
   */

  if (status_isset() && status_success()) {
    set_username_cookie(get_username());
  }
?>
<!DOCTYPE html>
<html lang="en">
  <!--
    /secure/index.php
    This page should be accessible to all clients. The script should display a
    login form allowing the user to sign in with a username and password. On
    successful login, the user should be shown a welcome page including his
    username. The page must also contain a link to the register form
    register.php and a link back to your non-HTTPS- secured page (index.html).
  -->
  <head>
    <? include 'headers.php' ?>
  </head>
  <body>
    <? include 'navbar.php' ?>
    <div class="container">
      <? /**
       * @return mixed
       */

        if (status_isset()): ?>
          <? if (status_success()): ?>
            <div class="alert alert-success alert-dismissible" role="alert">
              <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span
                  aria-hidden="true">&times;</span></button>
              <strong>Success!</strong> User: <?= get_session_username() ?> successfully logged in.
            </div>
          <? endif; ?>
          <? if (!status_success()): ?>
            <div class="alert alert-danger alert-dismissible" role="alert">
              <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span
                  aria-hidden="true">&times;</span></button>
              <strong>Error!</strong> Wrong username or password.
            </div>
          <? endif; ?>
        <? endif; ?>

      <? /**
       * @return bool
       */

        if (session_username_isset()): ?>
          <h1>Welcome <?= get_session_username(); ?></h1>
        <? else: ?>
          <h1>Welcome</h1>

          <h3>Please log in</h3>

          <div class="row">
            <? include "forms/login.php" ?>
            <div class="jumbotron col-md-6">
              <p>Yet to create an account?</p>

              <p><a class="btn btn-lg btn-default" href="/restricted/register">Register here</a></p>
              </p>
            </div>
          </div>
        <? endif; ?>
    </div>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>
  </body>
</html>
