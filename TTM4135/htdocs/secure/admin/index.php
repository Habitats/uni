<?
  set_include_path("../../lib" . PATH_SEPARATOR . "../include");
  require_once 'helpers.php';
  require_once 'user.php';
?>

<!DOCTYPE html>
<html lang="en">
  <!--
    /secure/admin/index.php
    This file should contain a list of all clients registered to your site and
    a mechanism for adding and removing them. It must also contain links
    pointing to all relevant pages for the staff, in particular it must
    contain a link to your main HTTP and HTTPS pages.
  -->
  <head>
    <? include 'headers.php' ?>
  </head>
  <body>
    <? include 'navbar.php' ?>
    <div class="container">
      <div class="row">
        <div class="col-md-6">
          <h2>Add new user</h2>
          <? if (isset($_GET['user_created'])): ?>
            <? include 'admin/user_success.php' ?>
          <? endif; ?>
          <? $admin_registration = true ?>
          <? include "forms/registration.php"; ?>
        </div>

        <div class="col-md-6">
          <h2>List of users</h2>
          <? if (status_isset()): ?>
            <? if (status_success()): ?>
              <div class="alert alert-success alert-dismissible" role="alert">
                <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span
                    aria-hidden="true">&times;</span></button>
                <strong>Success!</strong> <?= get_username() ?> successfully deleted.
              </div>
            <? endif; ?>
            <? if (!status_success()): ?>
              <div class="alert alert-danger alert-dismissible" role="alert">
                <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span
                    aria-hidden="true">&times;</span></button>
                <strong>Error!</strong> User not deleted.
              </div>
            <? endif; ?>
          <? endif; ?>

          <table style="width:100%">
            <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Username</th>
              <th>Email</th>
              <th>Delete</th>
            </tr>
            </thead>
            <? $users = User::get_all(); ?>
            <? foreach ($users as $user): ?>
              <tr>
                <td> <?= sanify($user->id) ?></td>
                <td> <?= sanify($user->name) ?></td>
                <td> <?= sanify($user->username) ?></td>
                <td> <?= sanify($user->email) ?></td>
                <td>
                  <? include 'forms/delete_user.php' ?>
                </td>
              </tr>
            <? endforeach; ?>
          </table>

        </div>
      </div>
    </div>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>
  </body>
</html>
