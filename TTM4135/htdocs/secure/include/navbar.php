<nav class="navbar navbar-inverse navbar-fixed-top">
  <div class="container">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar"
              aria-expanded="false" aria-controls="navbar">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="http://ttm4135.item.ntnu.no:8126">Group 06 HTTP</a>
    </div>
    <div id="navbar" class="collapse navbar-collapse">
      <ul class="nav navbar-nav">
        <li<?= nav_class('') ?>><a href="/">Home</a></li>
        <li<?= nav_class('/admin') ?>><a href="/admin">Admin</a></li>
        <li<?= nav_class('/restricted/register') ?>><a href="/restricted/register">Register</a></li>
      </ul>
      <? if (isset($_SESSION['username'])): ?>
        <? include 'forms/logout.php' ?>
        <p class="navbar-text navbar-right">
          Signed in as
          <a href="#" class="navbar-link">
            <?= $_SESSION['username'] ?>
          </a>
        </p>
      <? endif; ?>
    </div>
    <!--/.nav-collapse -->
  </div>
</nav>
