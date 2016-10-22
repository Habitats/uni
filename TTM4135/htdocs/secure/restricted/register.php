<?
  set_include_path('../../lib' . PATH_SEPARATOR . '../include');
  include 'helpers.php';
?>
<html>
  <!--
    /secure/register.php
    This script must be programmed to inspect the client certificate of the
    web browser, and display two different pages based on whether the client
    has a valid NTNU-certificate or not. If the client has a valid NTNU
    client certificate (either issued by Student CA or Staff CA), he or
    she should be allowed to register with a username and password. All
    others should be dismissed. When a user has successfully registered a
    valid username/password he should be redirected to the confirmation.php
    page, containing either a link back to the to login page
    (/secure/index.php) or automatically redirect him there. You might also
    take a look at [18].
  -->
  <head>
    <? include 'headers.php' ?>
  </head>
  <body>
    <? include 'navbar.php' ?>
    <div class="container">
      <? if (has_valid_certificate()): ?>
        <div class="row">
          <div class="col-md-6">
            <h3>Registration form</h3>
            <? $user_registration = true ?>
            <? include "forms/registration.php"; ?>
          </div>
        </div>
      <? else: ?>
        <h3>Du har ikke tilgang til registrering</h3>
        <p>Sorry</p>
      <? endif; ?>
    </div>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>
  </body>
</html>
