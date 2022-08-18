<script context="module">
    import HomeScreen from "./Home.svelte";
    import StatusScreen from "./Status.svelte";
    import SettingsScreen from "./Settings.svelte";
    
    export const navOptions = [
        { page: "Home", component: HomeScreen},
        { page: "Status", component: StatusScreen},
        { page: "Settings", component: SettingsScreen},
    ];
</script>
