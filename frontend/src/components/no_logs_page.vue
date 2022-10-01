<template>
    <div>
        <div class="alert alert-info mx-3" role = "alert">
            <strong>You have no trackers and hence no logs. Please add one !!!</strong>
        </div> 
        <CreateTrackerModal class="mx-3"/>

    </div>
</template>
<script>
    import CreateTrackerModal from './modals/CreateTrackerModal.vue';
    export default{
        name :'NoLogs',
        components:{
            CreateTrackerModal
        }
    }
</script>