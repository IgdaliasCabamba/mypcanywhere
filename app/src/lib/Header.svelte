<script>
    import {
        Collapse,
        Navbar,
        NavbarToggler,
        NavbarBrand,
        Nav,
        NavItem,
        NavLink,
        Dropdown,
        DropdownToggle,
        DropdownMenu,
        DropdownItem,
    } from "sveltestrap";
    import Fa from "svelte-fa/src/fa.svelte";
    import { faDesktop, faHandPointRight } from "@fortawesome/free-solid-svg-icons/index.es";
    import { faGithub, faDiscord } from "@fortawesome/free-brands-svg-icons/index.es";

    let isOpen = false;

    function handleUpdate(event) {
        isOpen = event.detail.isOpen;
    }
    export let options;
    export let changeComponentHandler;
</script>

<Navbar color="dark" dark expand="md" fixed="top">
    <NavbarBrand href="/">
        <Fa icon={faDesktop} />
    </NavbarBrand>
    <NavbarToggler on:click={() => (isOpen = !isOpen)} />
    <Collapse {isOpen} navbar expand="md" on:update={handleUpdate}>
        <Nav class="ms-auto" navbar>
            {#each options as option, i}
                <NavItem>
                    <NavLink
                        id={i.toString()}
                        on:click={(event) => changeComponentHandler(event)}
                        href="#">{option.page}</NavLink
                    >
                </NavItem>
            {/each}
            <Dropdown nav inNavbar>
                <DropdownToggle nav caret>Help</DropdownToggle>
                <DropdownMenu end dark>
                    <DropdownItem>
                        <Fa icon={faGithub}/>&nbsp;Github
                    </DropdownItem>
                    <DropdownItem>
                        <Fa icon={faDiscord}/>&nbsp;Discord
                    </DropdownItem>
                    <DropdownItem divider />
                    <DropdownItem><Fa icon={faHandPointRight}/>&nbsp;About</DropdownItem>
                </DropdownMenu>
            </Dropdown>
        </Nav>
    </Collapse>
</Navbar>
