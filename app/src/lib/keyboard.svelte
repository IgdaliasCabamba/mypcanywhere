<script>
  let count = 0;
  const increment = () => {
    count += 1;
  };
</script>

<body data-flex-splitter-vertical style="height: 100vh; margin: 0;">
  <button on:click={increment}>
    count is {count}
  </button>
  <header style="max-height: 100px;">header (max-height: 100px)</header>

  <div role="separator" tabindex="1" />

  <main data-flex-splitter-horizontal style="flex: auto;">
    <div style="width: 120px;">width: 120px</div>

    <div role="separator" tabindex="1" />

    <div data-flex-splitter-vertical style="min-width: 80px;">
      <div style="height: 4em;">min-width: 80px</div>
      <div role="separator" tabindex="1" />
      <div style="flex: auto;">flex: auto</div>
    </div>

    <div role="separator" tabindex="1" />

    <div style="flex: auto;">flex: auto</div>

    <div role="separator" tabindex="1" />

    <div style="min-width: 100px; max-width: 200px;">
      min-width: 100px<br />max-width: 200px
    </div>
  </main>

  <div role="separator" tabindex="1" />

  <footer>footer</footer>
</body>
