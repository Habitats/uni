<? require_once 'csrf.php' ?>
<? $csrf = new CSRF() ?>

<form action="/admin/delete_user" method="post">
  <input type="hidden" name="CSRFname" value="<?= $csrf->name ?>">
  <input type="hidden" name="CSRFtoken" value="<?= $csrf->token ?>">
  <input type="hidden" name="id" id="id" value="<?= $user->id ?>">
  <button type="submit" value="1" name="delete" class="btn btn-default">Delete</button>
</form>
