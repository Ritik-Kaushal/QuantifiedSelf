<template>
    <div>
        <div class="alert alert-info mx-3" role = "alert">
            <strong>You have no trackers. Please add one !!!</strong>
        </div> 
        <CreateTrackerModal class="mx-3"/>

    </div>
</template>
<script>
    import CreateTrackerModal from './modals/CreateTrackerModal.vue';
    export default{
        name :'NoTracker',
        components:{
            CreateTrackerModal
        }
    }
</script>