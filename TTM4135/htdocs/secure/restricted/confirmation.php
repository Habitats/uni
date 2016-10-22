<?
  set_include_path("../../lib" . PATH_SEPARATOR . "../include");
  include 'helpers.php';
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
      <div class="alert alert-success alert-dismissible" role="alert">
        <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span
          aria-hidden="true">&times;</span></button>
        <strong>Success!</strong> Your account was created.
      </div>

      <h1>Thank you for registering</h1>

      <div class="row">
        <div class="col-md-12">
          <p>
            You are registered, you can now go back to
            <a href="/">the start.</a>
          </p>
        </div>
      </div>
    </div>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>
  </body>
</html>
