<script lang="ts">
    import {
        Collapse,
        Navbar,
        NavbarToggler,
        NavbarBrand,
        Nav,
        Icon,
        NavItem,
        NavLink,
        Dropdown,
        DropdownToggle,
        DropdownMenu,
        DropdownItem,
    } from "sveltestrap";
    import Fa from 'svelte-fa/src/fa.svelte'
    import { faDesktop } from '@fortawesome/free-solid-svg-icons/index.es'

    let isOpen = false;

    function handleUpdate(event) {
        isOpen = event.detail.isOpen;
    }

</script>

<Navbar color="dark" dark expand="md" fixed="top">
    <NavbarBrand href="/">
        <Fa icon={faDesktop} />
    </NavbarBrand>
    <NavbarToggler on:click={() => (isOpen = !isOpen)} />
    <Collapse {isOpen} navbar expand="md" on:update={handleUpdate}>
        <Nav class="ms-auto" navbar>
            <NavItem>
                <NavLink href="#">Home</NavLink>
            </NavItem>
            <NavItem>
                <NavLink href="#"
                    >Status</NavLink
                >
            </NavItem>
            <Dropdown nav inNavbar>
                <DropdownToggle nav caret>Help</DropdownToggle>
                <DropdownMenu end dark>
                    <DropdownItem>Github</DropdownItem>
                    <DropdownItem>Discord</DropdownItem>
                    <DropdownItem divider />
                    <DropdownItem>About</DropdownItem>
                </DropdownMenu>
            </Dropdown>
        </Nav>
    </Collapse>
</Navbar>
