<script lang="ts">
    import { Progress, Container } from 'sveltestrap';
</script>
<Container fluid>
    <div class="text-center">100%</div>
    <Progress value={100} />

    <div class="text-center">100%</div>
    <Progress value={100} />

    <div class="text-center">100%</div>
    <Progress value={100} />
</Container>