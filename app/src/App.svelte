<script>
  import svelteLogo from "./assets/svelte.svg";
  import Header from "./lib/Header.svelte";
  import LocalStorage from "./js-libs/settings";
  import { navOptions }  from  "./lib/Nav.svelte";
  const local_storage = new LocalStorage();
  
  let selected = navOptions[0];
  let intSelected = 0;

  function changeComponent(event) {
  	selected = navOptions[event.srcElement.id];
  	intSelected = event.srcElement.id;
  }

</script>

<div id="page">
  <div id="header">
    <Header options={navOptions} changeComponentHandler={changeComponent}/>
  </div>
  <div id="content">
    <svelte:component this={selected.component}/>
  </div>
</div>
