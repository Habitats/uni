<div class="col-md-6">
  <form action="/login" method="post">
    <div class="form-group">
      <label for="username">Username</label>
      <input type="text" name="username" class="form-control" id="username" placeholder="Enter username" value="<?= $_COOKIE["username"] ?>">
    </div>
    <div class="form-group">
      <label for="password">Password</label>
      <input type="password" name="password" class="form-control" id="user_password" placeholder="Password">
    </div>
    <button type="submit" class="btn btn-default">Log in</button>
  </form>
</div>
