<? if ($errors): ?>
  <div class="alert alert-danger alert-dismissible" role="alert">
    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
      <span aria-hidden="true">&times;</span>
    </button>
    <strong>Error!</strong> Please fix the errors below, and resubmit.
  </div>
<? endif; ?>

<form action="/restricted/registration" method="POST">
  <? if ($given_name_error): ?>
    <div class="form-group has-error">
  <? else: ?>
    <div class="form-group">
  <? endif; ?>
    <label for="user_given_name">Given name</label>
    <input type="text" name="user_given_name" class="form-control" id="user_given_name"
      placeholder="Enter given name" value="<?= sanify($given_name) ?>">
    <? if ($given_name_error): ?>
      <span id="helpBlock" class="help-block">Given name must be at least 1 character.</span>
    <? endif; ?>
  </div>
  <div class="form-group">
    <label for="user_family_name">Family name</label>
    <input type="text" name="user_family_name" class="form-control" id="user_family_name"
    placeholder="Enter family name" value="<?= sanify($family_name) ?>">
  </div>
  <? if ($username_exists): ?>
    <div class="form-group has-error">
  <? else: ?>
    <div class="form-group">
  <? endif; ?>
    <label for="username">Username</label>
    <input type="text" name="username" class="form-control" id="username" placeholder="Enter username"
      value="<?= sanify($username) ?>">
    <? if ($username_exists): ?>
      <span id="helpBlock" class="help-block">Username already exists.</span>
    <? endif; ?>
  </div>
  <? if ($email_exists): ?>
    <div class="form-group has-error">
  <? else: ?>
    <div class="form-group">
  <? endif; ?>
    <label for="user_email">Email address</label>
    <input type="email" name="user_email" class="form-control" id="user_email" placeholder="Enter email"
      value="<?= sanify($email) ?>">
    <? if ($email_exists): ?>
      <span id="helpBlock" class="help-block">Email already exists.</span>
    <? endif; ?>
  </div>
  <? if ($email_confirmation_error): ?>
    <div class="form-group has-error">
  <? else: ?>
    <div class="form-group">
  <? endif; ?>
    <label for="user_email_confirmation">Confirm email address</label>
    <input type="email" name="user_email_confirmation" class="form-control" id="user_email_confirmation"
      placeholder="Confirm email" value="<?= sanify($email_confirmation) ?>">
    <? if ($email_confirmation_error): ?>
      <span id="helpBlock" class="help-block">Email confirmation did not match.</span>
    <? endif; ?>
  </div>
  <? if ($password_error): ?>
    <div class="form-group has-error">
  <? else: ?>
    <div class="form-group">
  <? endif; ?>
    <label for="user_password">Password</label>
    <input type="password" name="user_password" class="form-control" id="user_password"
      placeholder="Password">
    <? if ($password_error): ?>
      <span id="helpBlock" class="help-block">
        Password should be between 8 and 72 characters.
      </span>
    <? endif; ?>
  </div>
  <? if ($password_confirmation_error): ?>
    <div class="form-group has-error">
  <? else: ?>
    <div class="form-group">
  <? endif; ?>
    <label for="user_password_confirmation">Confirm password</label>
    <input type="password" name="user_password_confirmation" class="form-control"
      id="user_password_confirmation" placeholder="Confirm password">
    <? if ($password_confirmation_error): ?>
      <span id="helpBlock" class="help-block">Password confirmation did not match.</span>
    <? endif; ?>
  </div>
  <? if ($admin_registration): ?>
    <input type="hidden" name="redirect_to" value="admin">
  <? elseif ($user_registration): ?>
    <input type="hidden" name="redirect_to" value="register">
  <? endif; ?>
  <button type="submit" name="submit" class="btn btn-default">Register</button>
</form>
